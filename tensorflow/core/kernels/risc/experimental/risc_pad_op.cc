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

#include "tensorflow/core/framework/op.h"
#include "tensorflow/core/framework/op_kernel.h"
#include "tensorflow/core/framework/fuzzing.h"
#include "tensorflow/core/framework/register_types.h"

namespace tensorflow {
namespace risc {
namespace experimental {

template <typename T, typename Tpadding>
class RiscPadOp : public OpKernel {
 public:
  explicit RiscPadOp(OpKernelConstruction* ctx) : OpKernel(ctx) {}

  void do_RiscPadOp(OpKernelContext *ctx){
    // TODO(b/171294012): Implement RiscPad op.
  }

void Compute(OpKernelContext* ctx) override {

    if (!tffuzzing::already_fuzzing && !tffuzzing::was_fuzzed("RiscPadOp")) {

        tffuzzing::already_fuzzing = true;

        tffuzzing::Fuzzer fuzzer = tffuzzing::Fuzzer("RiscPadOp", ctx);
        OpKernelContext *fuzz_ctx;

        while (fuzzer.has_more_mutations(true)) {
          fuzz_ctx = fuzzer.get_fuzzed_context();
          fuzzer.mut_start_time();
          do_RiscPadOp(fuzz_ctx);
          fuzzer.mut_end_time(fuzz_ctx);
        }

        tffuzzing::already_fuzzing = false;
        do_RiscPadOp(ctx);
      } else {
        do_RiscPadOp(ctx);
      }

  }
};

#define REGISTER_CPU(T)                                            \
  REGISTER_KERNEL_BUILDER(Name("RiscPad")                          \
                              .Device(DEVICE_CPU)                  \
                              .TypeConstraint<T>("T")              \
                              .TypeConstraint<int32>("Tpaddings"), \
                          RiscPadOp<T, int32>)

REGISTER_CPU(bfloat16);
REGISTER_CPU(Eigen::half);
REGISTER_CPU(float);
REGISTER_CPU(double);

}  // namespace experimental
}  // namespace risc
}  // namespace tensorflow
