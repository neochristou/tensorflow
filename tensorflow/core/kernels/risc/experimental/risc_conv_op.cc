/* Copyright 2020 The TensorFlow Authors. All Rights Reserved.

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

#include "tensorflow/core/framework/common_shape_fns.h"
#include "tensorflow/core/framework/op.h"
#include "tensorflow/core/framework/op_kernel.h"
#include "tensorflow/core/framework/fuzzing.h"
#include "tensorflow/core/framework/register_types.h"
#include "tensorflow/core/framework/shape_inference.h"

namespace tensorflow {
namespace risc {
namespace experimental {

typedef Eigen::ThreadPoolDevice CPUDevice;

template <typename Device, typename T>
class RiscConvOp : public OpKernel {
 public:
  explicit RiscConvOp(OpKernelConstruction* context) : OpKernel(context) {
    // TODO(b/171294012): Implement RiscConv op.
  }

  void do_RiscConvOp(OpKernelContext *context){
    // TODO(b/171294012): Implement RiscConv op.
  }

void Compute(OpKernelContext* context) override {

    if (!tffuzzing::already_fuzzing && !tffuzzing::was_fuzzed("RiscConvOp")) {

        tffuzzing::already_fuzzing = true;

        tffuzzing::Fuzzer fuzzer = tffuzzing::Fuzzer("RiscConvOp", context);
        OpKernelContext *fuzz_ctx;

        while (fuzzer.has_more_mutations(true)) {
          fuzz_ctx = fuzzer.get_fuzzed_context();
          fuzzer.mut_start_time();
          do_RiscConvOp(fuzz_ctx);
          fuzzer.mut_end_time(fuzz_ctx);
        }

        tffuzzing::already_fuzzing = false;
        do_RiscConvOp(context);
      } else {
        do_RiscConvOp(context);
      }

  }
};

#define REGISTER_CPU(T)                                           \
  REGISTER_KERNEL_BUILDER(                                        \
      Name("RiscConv").Device(DEVICE_CPU).TypeConstraint<T>("T"), \
      RiscConvOp<CPUDevice, T>);

REGISTER_CPU(float);
REGISTER_CPU(double);

}  // namespace experimental
}  // namespace risc
}  // namespace tensorflow
