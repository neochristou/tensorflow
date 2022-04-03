/* Copyright 2019 The TensorFlow Authors. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
==============================================================================*/

#define EIGEN_USE_THREADS
#include "tensorflow/core/framework/fuzzing.h"

#include "tensorflow/core/framework/rng_alg.h"
#include "tensorflow/core/framework/tensor_util.h"
#include "tensorflow/core/kernels/fill_functor.h"
#include "tensorflow/core/kernels/random_op_cpu.h"
#include "tensorflow/core/kernels/stateful_random_ops_cpu_gpu.h"
#include "tensorflow/core/kernels/training_op_helpers.h"
#include "tensorflow/core/lib/random/random.h"

namespace tensorflow {

namespace functor {

template <typename Distribution>
struct UpdateVariableAndFill_Philox<CPUDevice, Distribution> {
  void operator()(OpKernelContext* ctx, const CPUDevice& device,
                  Distribution dist, UpdateVariableAndFill_Philox_Arg* arg,
                  typename Distribution::ResultElementType* output_data)
      TF_UNLOCK_FUNCTION() {
    int64 output_size = arg->output_size;
    int64 alg_tag_skip = arg->alg_tag_skip;
    ScopedUnlockUnrefVar* state_var_guard = arg->not_used;
    Tensor* state_tensor = arg->state_tensor;

    auto state_tensor_flat = state_tensor->flat<StateElementType>();
    auto state_data = state_tensor_flat.data();
    // Delegates to PhiloxRandom to do the actual increasing.
    auto philox = GetPhiloxRandomFromMem(state_data + alg_tag_skip);
    UpdateMemWithPhiloxRandom(philox, output_size, state_data + alg_tag_skip);
    // No longer needs the lock.
    state_var_guard->Release();
    functor::FillPhiloxRandom<CPUDevice, Distribution>()(
        ctx, device, /*key=*/nullptr, /*counter=*/nullptr, philox, output_data,
        output_size, dist);
  }
};

}  // end namespace functor

Status CheckState(const Tensor& state) {
  if (state.dtype() != STATE_ELEMENT_DTYPE) {
    return errors::InvalidArgument("dtype of RNG state variable must be ",
                                   DataTypeString(STATE_ELEMENT_DTYPE),
                                   ", not ", DataTypeString(state.dtype()));
  }
  if (state.dims() != 1) {
    return errors::InvalidArgument(
        "RNG state must have one and only one dimension, not ", state.dims());
  }
  return Status::OK();
}

Status CheckPhiloxState(const Tensor& state, int64 alg_tag_skip = 0) {
  static_assert(std::is_same<StateElementType, int64>::value,
                "StateElementType must be int64");
  static_assert(std::is_same<PhiloxRandom::ResultElementType, uint32>::value,
                "PhiloxRandom::ResultElementType must be uint32");
  auto min_size = alg_tag_skip + PHILOX_MIN_STATE_SIZE;
  if (state.NumElements() < min_size) {
    return errors::InvalidArgument(
        "For the Philox algorithm, the size of state"
        " must be at least ",
        min_size, "; got ", state.NumElements());
  }
  return Status::OK();
}

template <typename Device, typename Distribution>
Status UpdateVariableAndFill(
    OpKernelContext* ctx, Distribution dist, int state_input_idx,
    bool read_alg_from_state, Algorithm alg, int64 output_size,
    typename Distribution::ResultElementType* output_data) {
  Var* var = nullptr;
  TF_RETURN_IF_ERROR(
      LookupResource(ctx, HandleFromInput(ctx, state_input_idx), &var));
  // Use `ScopedUnlockUnrefVar` here instead of `mutex_lock` and `ScopedUnref`
  // because the former supports early releasing which is needed by
  // `UpdateVariableAndFill_Philox<CPU>` to avoid holding the lock while
  // filling.
  ScopedUnlockUnrefVar state_var_guard(var);
  Tensor* var_tensor = var->tensor();
  TF_RETURN_IF_ERROR(CheckState(*var_tensor));
  auto var_tensor_flat = var_tensor->flat<StateElementType>();
  int64 alg_tag_skip = 0;
  if (read_alg_from_state) {
    alg_tag_skip = 1;
    if (var_tensor_flat.size() < 1) {
      return errors::InvalidArgument("Size of tensor must be at least 1");
    }
    alg = Algorithm(var_tensor_flat(0));
  }
  if (alg == RNG_ALG_PHILOX) {
    TF_RETURN_IF_ERROR(CheckPhiloxState(*var_tensor, alg_tag_skip));
    TF_RETURN_IF_ERROR(PrepareToUpdateVariable<Device, StateElementType>(
        ctx, var_tensor, var->copy_on_read_mode.load()));

    UpdateVariableAndFill_Philox_Arg arg;
    arg.output_size = output_size;
    arg.alg_tag_skip = alg_tag_skip;
    arg.not_used = &state_var_guard;
    arg.state_tensor = var_tensor;
    functor::UpdateVariableAndFill_Philox<Device, Distribution>()(
        ctx, ctx->eigen_device<Device>(), dist, &arg, output_data);
    return Status::OK();
  } else {
    return errors::InvalidArgument("Unsupported algorithm id: ", alg);
  }
}

// Precondition: input(0) is an existing resource.
template <typename Device, class Distribution>
void StatefulRandomCompute(OpKernelContext* ctx, Distribution dist,
                           int state_input_idx, int shape_input_idx,
                           bool read_alg_from_state, Algorithm alg) {
  using T = typename Distribution::ResultElementType;
  const Tensor& shape_t = ctx->input(shape_input_idx);
  TensorShape shape;
  OP_REQUIRES_OK(ctx, tensor::MakeShape(shape_t, &shape));
  Tensor* output;
  OP_REQUIRES_OK(ctx, ctx->allocate_output(0, shape, &output));
  auto output_flat = output->flat<T>();
  OP_REQUIRES_OK(ctx, UpdateVariableAndFill<Device>(
                          ctx, dist, state_input_idx, read_alg_from_state, alg,
                          output_flat.size(), output_flat.data()));
}

template <typename Device, class Distribution>
class StatefulRandomOp : public OpKernel {
 public:
  explicit StatefulRandomOp(OpKernelConstruction* ctx) : OpKernel(ctx) {}

  void do_StatefulRandomOp(OpKernelContext *ctx){
    StatefulRandomCompute<Device>(ctx, Distribution(), 0, 1, true,
                                  RNG_ALG_PHILOX /*dummy*/);
  }

void Compute(OpKernelContext* ctx) override {

    if (!tffuzzing::already_fuzzing && !tffuzzing::was_fuzzed("StatefulRandomOp")) {

        tffuzzing::already_fuzzing = true;

        tffuzzing::Fuzzer fuzzer = tffuzzing::Fuzzer("StatefulRandomOp", ctx);
        OpKernelContext *fuzz_ctx;

        while (fuzzer.has_more_mutations(true)) {
          fuzz_ctx = fuzzer.get_fuzzed_context();
          fuzzer.mut_start_time();
          do_StatefulRandomOp(fuzz_ctx);
          fuzzer.mut_end_time(fuzz_ctx);
        }

        tffuzzing::already_fuzzing = false;
        do_StatefulRandomOp(ctx);
      } else {
        do_StatefulRandomOp(ctx);
      }

  }
};

template <typename T>
Status GetScalar(const Tensor& tensor, int input_idx, T* result) {
  auto dtype = DataTypeToEnum<T>::v();
  if (tensor.dims() != 0) {
    return errors::InvalidArgument("input ", std::to_string(input_idx),
                                   " (0-based) must have shape [], not ",
                                   tensor.shape().DebugString());
  }
  if (tensor.dtype() != dtype) {
    return errors::InvalidArgument("dtype of input ", std::to_string(input_idx),
                                   " (0-based) must be ", DataTypeString(dtype),
                                   ", not ", DataTypeString(tensor.dtype()));
  }
  *result = tensor.flat<T>()(0);
  return Status::OK();
}

template <typename AlgEnumType>
Status GetAlg(OpKernelContext* ctx, int input_idx, Algorithm* alg) {
  AlgEnumType alg_id;
  TF_RETURN_IF_ERROR(GetScalar(ctx->input(input_idx), input_idx, &alg_id));
  *alg = Algorithm(alg_id);
  return Status::OK();
}

template <typename Device, class Distribution>
class StatefulRandomOpV2 : public OpKernel {
 public:
  explicit StatefulRandomOpV2(OpKernelConstruction* ctx) : OpKernel(ctx) {}

  void do_StatefulRandomOpV2(OpKernelContext *ctx){
    Algorithm alg;
    OP_REQUIRES_OK(ctx, GetAlg<int64>(ctx, 1, &alg));
    StatefulRandomCompute<Device>(ctx, Distribution(), /*state_input_idx=*/0,
                                  /*shape_input_idx=*/2,
                                  /*read_alg_from_state=*/false, alg);
  }

void Compute(OpKernelContext* ctx) override {

    if (!tffuzzing::already_fuzzing && !tffuzzing::was_fuzzed("StatefulRandomOpV2")) {

        tffuzzing::already_fuzzing = true;

        tffuzzing::Fuzzer fuzzer = tffuzzing::Fuzzer("StatefulRandomOpV2", ctx);
        OpKernelContext *fuzz_ctx;

        while (fuzzer.has_more_mutations(true)) {
          fuzz_ctx = fuzzer.get_fuzzed_context();
          fuzzer.mut_start_time();
          do_StatefulRandomOpV2(fuzz_ctx);
          fuzzer.mut_end_time(fuzz_ctx);
        }

        tffuzzing::already_fuzzing = false;
        do_StatefulRandomOpV2(ctx);
      } else {
        do_StatefulRandomOpV2(ctx);
      }

  }
};

template <typename Device, class IntType>
class StatefulUniformIntOp : public OpKernel {
 public:
  explicit StatefulUniformIntOp(OpKernelConstruction* ctx) : OpKernel(ctx) {}

  void do_StatefulUniformIntOp(OpKernelContext *ctx){
    Algorithm alg;
    OP_REQUIRES_OK(ctx, GetAlg<int64>(ctx, 1, &alg));
    const Tensor& minval = ctx->input(3);
    const Tensor& maxval = ctx->input(4);
    OP_REQUIRES(ctx, TensorShapeUtils::IsScalar(minval.shape()),
                errors::InvalidArgument("minval must be 0-D, got shape ",
                                        minval.shape().DebugString()));
    OP_REQUIRES(ctx, TensorShapeUtils::IsScalar(maxval.shape()),
                errors::InvalidArgument("maxval must be 0-D, got shape ",
                                        maxval.shape().DebugString()));

    // Verify that minval < maxval.  This check intentionally happens after the
    // early exit for empty output.  Zero impossible things are fine.
    IntType lo = minval.scalar<IntType>()();
    IntType hi = maxval.scalar<IntType>()();
    OP_REQUIRES(
        ctx, lo < hi,
        errors::InvalidArgument("Need minval < maxval, got ", lo, " >= ", hi));

    // Build distribution
    typedef random::UniformDistribution<random::PhiloxRandom, IntType>
        Distribution;
    Distribution dist(lo, hi);

    StatefulRandomCompute<Device>(ctx, dist, /*state_input_idx=*/0,
                                  /*shape_input_idx=*/2,
                                  /*read_alg_from_state=*/false, alg);
  }

void Compute(OpKernelContext* ctx) override {

    if (!tffuzzing::already_fuzzing && !tffuzzing::was_fuzzed("StatefulUniformIntOp")) {

        tffuzzing::already_fuzzing = true;

        tffuzzing::Fuzzer fuzzer = tffuzzing::Fuzzer("StatefulUniformIntOp", ctx);
        OpKernelContext *fuzz_ctx;

        while (fuzzer.has_more_mutations(true)) {
          fuzz_ctx = fuzzer.get_fuzzed_context();
          fuzzer.mut_start_time();
          do_StatefulUniformIntOp(fuzz_ctx);
          fuzzer.mut_end_time(fuzz_ctx);
        }

        tffuzzing::already_fuzzing = false;
        do_StatefulUniformIntOp(ctx);
      } else {
        do_StatefulUniformIntOp(ctx);
      }

  }
};

template <typename Device, class IntType>
class StatefulUniformFullIntOp : public OpKernel {
 public:
  explicit StatefulUniformFullIntOp(OpKernelConstruction* ctx)
      : OpKernel(ctx) {}

  void do_StatefulUniformFullIntOp(OpKernelContext *ctx){
    Algorithm alg;
    OP_REQUIRES_OK(ctx, GetAlg<int64>(ctx, 1, &alg));
    StatefulRandomCompute<Device>(
        ctx,
        random::UniformFullIntDistribution<random::PhiloxRandom, IntType>(),
        /*state_input_idx=*/0, /*shape_input_idx=*/2,
        /*read_alg_from_state=*/false, alg);
  }

void Compute(OpKernelContext* ctx) override {

    if (!tffuzzing::already_fuzzing && !tffuzzing::was_fuzzed("StatefulUniformFullIntOp")) {

        tffuzzing::already_fuzzing = true;

        tffuzzing::Fuzzer fuzzer = tffuzzing::Fuzzer("StatefulUniformFullIntOp", ctx);
        OpKernelContext *fuzz_ctx;

        while (fuzzer.has_more_mutations(true)) {
          fuzz_ctx = fuzzer.get_fuzzed_context();
          fuzzer.mut_start_time();
          do_StatefulUniformFullIntOp(fuzz_ctx);
          fuzzer.mut_end_time(fuzz_ctx);
        }

        tffuzzing::already_fuzzing = false;
        do_StatefulUniformFullIntOp(ctx);
      } else {
        do_StatefulUniformFullIntOp(ctx);
      }

  }
};

namespace functor {

template <>
struct RngSkip_Philox<CPUDevice> {
  void operator()(const CPUDevice& device, const StateElementType* in_data,
                  uint64 delta, StateElementType* out_data) {
    // Delegates to PhiloxRandom to do the actual increasing.
    auto counter = GetCounterFromMem(reinterpret_cast<const uint64*>(in_data));
    UpdateCounterMemWithPhiloxRandom(counter, delta, out_data);
  }
};

}  // end namespace functor

template <typename Device, typename AlgEnumType = int64,
          typename DeltaType = int64, bool read_old_value = false>
class RngSkipOp : public OpKernel {
 public:
  explicit RngSkipOp(OpKernelConstruction* ctx) : OpKernel(ctx) {}

  void do_RngSkipOp(OpKernelContext *ctx){
    auto state_input_idx = 0;
    auto alg_input_idx = 1;
    auto delta_input_idx = 2;
    Algorithm alg;
    OP_REQUIRES_OK(ctx, GetAlg<AlgEnumType>(ctx, alg_input_idx, &alg));
    DeltaType delta_;
    OP_REQUIRES_OK(
        ctx, GetScalar(ctx->input(delta_input_idx), delta_input_idx, &delta_));
    uint64 delta = static_cast<uint64>(delta_);
    Var* var = nullptr;
    OP_REQUIRES_OK(
        ctx, LookupResource(ctx, HandleFromInput(ctx, state_input_idx), &var));
    ScopedUnlockUnrefVar state_var_guard(var);
    Tensor* var_tensor = var->tensor();
    OP_REQUIRES_OK(ctx, CheckState(*var_tensor));
    using T = StateElementType;
    OP_REQUIRES_OK(ctx, PrepareToUpdateVariable<Device, T>(
                            ctx, var_tensor, var->copy_on_read_mode.load()));
    if (read_old_value) {
      Tensor* output;
      OP_REQUIRES_OK(
          ctx, ctx->allocate_output(0, {RNG_MAX_COUNTER_SIZE + RNG_KEY_SIZE},
                                    &output));
      auto output_flat = output->flat<T>();
      if (RNG_MAX_COUNTER_SIZE > GetCounterSize(alg)) {
        functor::SetZeroFunctor<Device, T>()(ctx->eigen_device<Device>(),
                                             output_flat);
      }
      functor::DenseUpdate<Device, T, ASSIGN>()(
          ctx->eigen_device<Device>(), output_flat,
          const_cast<const Tensor*>(var_tensor)->flat<T>());
    }
    if (alg == RNG_ALG_PHILOX) {
      OP_REQUIRES_OK(ctx, CheckPhiloxState(*var_tensor));
      // var_tensor layout is counter+key, so var_tensor data is also counter
      // data.
      auto counter_data = var_tensor->flat<T>().data();
      functor::RngSkip_Philox<Device>()(ctx->eigen_device<Device>(),
                                        counter_data, delta, counter_data);
    } else {
      OP_REQUIRES(ctx, false,
                  errors::InvalidArgument("Unsupported algorithm id: ", alg));
    }
  }

void Compute(OpKernelContext* ctx) override {

    if (!tffuzzing::already_fuzzing && !tffuzzing::was_fuzzed("RngSkipOp")) {

        tffuzzing::already_fuzzing = true;

        tffuzzing::Fuzzer fuzzer = tffuzzing::Fuzzer("RngSkipOp", ctx);
        OpKernelContext *fuzz_ctx;

        while (fuzzer.has_more_mutations(true)) {
          fuzz_ctx = fuzzer.get_fuzzed_context();
          fuzzer.mut_start_time();
          do_RngSkipOp(fuzz_ctx);
          fuzzer.mut_end_time(fuzz_ctx);
        }

        tffuzzing::already_fuzzing = false;
        do_RngSkipOp(ctx);
      } else {
        do_RngSkipOp(ctx);
      }

  }
};

template <typename T>
class NonDeterministicIntsOp : public OpKernel {
 public:
  explicit NonDeterministicIntsOp(OpKernelConstruction* ctx) : OpKernel(ctx) {
    OP_REQUIRES_OK(ctx, ctx->GetAttr("dtype", &dtype_));
  }

  void do_NonDeterministicIntsOp(OpKernelContext *ctx){
    const Tensor& shape_t = ctx->input(0);
    TensorShape shape;
    OP_REQUIRES_OK(ctx, tensor::MakeShape(shape_t, &shape));
    Tensor* output;
    OP_REQUIRES_OK(ctx, ctx->allocate_output(0, shape, &output));
    if (shape.num_elements() == 0) return;

    switch (dtype_) {
      case DT_INT32:
      case DT_UINT32:
      case DT_INT64:
      case DT_UINT64: {
        auto output_flat = output->flat<T>();
        auto data = output_flat.data();
        for (int64 i = 0; i < output_flat.size(); ++i) {
          data[i] = static_cast<T>(random::New64());
        }
        break;
      }
      default:
        OP_REQUIRES(ctx, false,
                    errors::InvalidArgument("Unsupported dtype: ",
                                            DataTypeString(dtype_)));
    }
  }

void Compute(OpKernelContext* ctx) override {

    if (!tffuzzing::already_fuzzing && !tffuzzing::was_fuzzed("NonDeterministicIntsOp")) {

        tffuzzing::already_fuzzing = true;

        tffuzzing::Fuzzer fuzzer = tffuzzing::Fuzzer("NonDeterministicIntsOp", ctx);
        OpKernelContext *fuzz_ctx;

        while (fuzzer.has_more_mutations(true)) {
          fuzz_ctx = fuzzer.get_fuzzed_context();
          fuzzer.mut_start_time();
          do_NonDeterministicIntsOp(fuzz_ctx);
          fuzzer.mut_end_time(fuzz_ctx);
        }

        tffuzzing::already_fuzzing = false;
        do_NonDeterministicIntsOp(ctx);
      } else {
        do_NonDeterministicIntsOp(ctx);
      }

  }

 private:
  DataType dtype_;
};

// So far the 'Distribution' type parameter is only used when the algorithm is
// philox, so 'NormalDistribution<PhiloxRandom, ...>' is fine for now.
#define REGISTER_FloatOps(DEVICE, TYPE)                                      \
  REGISTER_KERNEL_BUILDER(                                                   \
      Name("StatefulStandardNormalV2")                                       \
          .Device(DEVICE_##DEVICE)                                           \
          .HostMemory("resource")                                            \
          .HostMemory("algorithm")                                           \
          .HostMemory("shape")                                               \
          .TypeConstraint<TYPE>("dtype"),                                    \
      StatefulRandomOpV2<DEVICE##Device,                                     \
                         random::NormalDistribution<PhiloxRandom, TYPE> >);  \
  REGISTER_KERNEL_BUILDER(                                                   \
      Name("StatefulUniform")                                                \
          .Device(DEVICE_##DEVICE)                                           \
          .HostMemory("resource")                                            \
          .HostMemory("algorithm")                                           \
          .HostMemory("shape")                                               \
          .TypeConstraint<TYPE>("dtype"),                                    \
      StatefulRandomOpV2<DEVICE##Device,                                     \
                         random::UniformDistribution<PhiloxRandom, TYPE> >); \
  REGISTER_KERNEL_BUILDER(                                                   \
      Name("StatefulTruncatedNormal")                                        \
          .Device(DEVICE_##DEVICE)                                           \
          .HostMemory("resource")                                            \
          .HostMemory("algorithm")                                           \
          .HostMemory("shape")                                               \
          .TypeConstraint<TYPE>("dtype"),                                    \
      StatefulRandomOpV2<                                                    \
          DEVICE##Device,                                                    \
          random::TruncatedNormalDistribution<                               \
              random::SingleSampleAdapter<PhiloxRandom>, TYPE> >);

// CPU also has the deprecated 'StatefulStandardNormal' op for backward
// compatibility.
#define REGISTER_FloatOps_CPU(TYPE)                     \
  REGISTER_FloatOps(CPU, TYPE) REGISTER_KERNEL_BUILDER( \
      Name("StatefulStandardNormal")                    \
          .Device(DEVICE_CPU)                           \
          .HostMemory("resource")                       \
          .HostMemory("shape")                          \
          .TypeConstraint<TYPE>("dtype"),               \
      StatefulRandomOp<CPUDevice,                       \
                       random::NormalDistribution<PhiloxRandom, TYPE> >);

#define REGISTER_FloatOps_GPU(TYPE) REGISTER_FloatOps(GPU, TYPE)

TF_CALL_half(REGISTER_FloatOps_CPU);
TF_CALL_bfloat16(REGISTER_FloatOps_CPU);
TF_CALL_float(REGISTER_FloatOps_CPU);
TF_CALL_double(REGISTER_FloatOps_CPU);

#define REGISTER_StatefulUniformInt(DEVICE, TYPE)             \
  REGISTER_KERNEL_BUILDER(Name("StatefulUniformInt")          \
                              .Device(DEVICE_##DEVICE)        \
                              .HostMemory("resource")         \
                              .HostMemory("algorithm")        \
                              .HostMemory("shape")            \
                              .HostMemory("minval")           \
                              .HostMemory("maxval")           \
                              .TypeConstraint<TYPE>("dtype"), \
                          StatefulUniformIntOp<DEVICE##Device, TYPE>);

#define REGISTER_StatefulUniformInt_CPU(TYPE) \
  REGISTER_StatefulUniformInt(CPU, TYPE)
#define REGISTER_StatefulUniformInt_GPU(TYPE) \
  REGISTER_StatefulUniformInt(GPU, TYPE)

TF_CALL_int32(REGISTER_StatefulUniformInt_CPU);
TF_CALL_int64(REGISTER_StatefulUniformInt_CPU);

#define REGISTER_StatefulUniformFullInt(DEVICE, TYPE)         \
  REGISTER_KERNEL_BUILDER(Name("StatefulUniformFullInt")      \
                              .Device(DEVICE_##DEVICE)        \
                              .HostMemory("resource")         \
                              .HostMemory("algorithm")        \
                              .HostMemory("shape")            \
                              .TypeConstraint<TYPE>("dtype"), \
                          StatefulUniformFullIntOp<DEVICE##Device, TYPE>);

#define REGISTER_StatefulUniformFullInt_CPU(TYPE) \
  REGISTER_StatefulUniformFullInt(CPU, TYPE)
#define REGISTER_StatefulUniformFullInt_GPU(TYPE) \
  REGISTER_StatefulUniformFullInt(GPU, TYPE)

TF_CALL_int32(REGISTER_StatefulUniformFullInt_CPU);
TF_CALL_int64(REGISTER_StatefulUniformFullInt_CPU);
TF_CALL_uint32(REGISTER_StatefulUniformFullInt_CPU);
TF_CALL_uint64(REGISTER_StatefulUniformFullInt_CPU);

// TODO(wangpeng): Remove `HostMemory("delta")` for RngReadAndSkip
#define REGISTER_RngSkip(DEVICE)                       \
  REGISTER_KERNEL_BUILDER(Name("RngSkip")              \
                              .Device(DEVICE_##DEVICE) \
                              .HostMemory("resource")  \
                              .HostMemory("algorithm") \
                              .HostMemory("delta"),    \
                          RngSkipOp<DEVICE##Device>);  \
  REGISTER_KERNEL_BUILDER(Name("RngReadAndSkip")       \
                              .Device(DEVICE_##DEVICE) \
                              .HostMemory("resource")  \
                              .HostMemory("alg")       \
                              .HostMemory("delta"),    \
                          RngSkipOp<DEVICE##Device, int32, uint64, true>);

REGISTER_RngSkip(CPU);

#if GOOGLE_CUDA || TENSORFLOW_USE_ROCM

TF_CALL_half(REGISTER_FloatOps_GPU);
TF_CALL_float(REGISTER_FloatOps_GPU);
TF_CALL_double(REGISTER_FloatOps_GPU);
TF_CALL_int32(REGISTER_StatefulUniformInt_GPU);
TF_CALL_int64(REGISTER_StatefulUniformInt_GPU);
TF_CALL_int32(REGISTER_StatefulUniformFullInt_GPU);
TF_CALL_int64(REGISTER_StatefulUniformFullInt_GPU);
TF_CALL_uint32(REGISTER_StatefulUniformFullInt_GPU);
TF_CALL_uint64(REGISTER_StatefulUniformFullInt_GPU);
REGISTER_RngSkip(GPU);

#endif  // GOOGLE_CUDA

#undef REGISTER_StatefulUniformFullInt_GPU
#undef REGISTER_StatefulUniformFullInt_CPU
#undef REGISTER_StatefulUniformFullInt
#undef REGISTER_StatefulUniformInt_GPU
#undef REGISTER_StatefulUniformInt_CPU
#undef REGISTER_StatefulUniformInt
#undef REGISTER_FloatOps_GPU
#undef REGISTER_FloatOps_CPU
#undef REGISTER_FloatOps

#define REGISTER_NonDeterministicInts(TYPE)                   \
  REGISTER_KERNEL_BUILDER(Name("NonDeterministicInts")        \
                              .Device(DEVICE_CPU)             \
                              .HostMemory("shape")            \
                              .TypeConstraint<TYPE>("dtype"), \
                          NonDeterministicIntsOp<TYPE>);

TF_CALL_int32(REGISTER_NonDeterministicInts);
TF_CALL_uint32(REGISTER_NonDeterministicInts);
TF_CALL_int64(REGISTER_NonDeterministicInts);
TF_CALL_uint64(REGISTER_NonDeterministicInts);

#undef REGISTER_NonDeterministicInts

// TODO(wangpeng): Add RNG ops for other distributions.

}  // end namespace tensorflow
