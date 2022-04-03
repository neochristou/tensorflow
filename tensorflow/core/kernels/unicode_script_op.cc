/* Copyright 2018 The TensorFlow Authors. All Rights Reserved.

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

#include "unicode/errorcode.h"  // from @icu
#include "unicode/uscript.h"  // from @icu
#include "tensorflow/core/framework/op_kernel.h"
#include "tensorflow/core/framework/fuzzing.h"

namespace tensorflow {

class UnicodeScriptOp : public OpKernel {
 public:
  explicit UnicodeScriptOp(OpKernelConstruction* context) : OpKernel(context) {}

  void do_UnicodeScriptOp(OpKernelContext *context){
    const Tensor* input_tensor;
    OP_REQUIRES_OK(context, context->input("input", &input_tensor));
    const auto& input_flat = input_tensor->flat<int32>();

    Tensor* output_tensor = nullptr;
    OP_REQUIRES_OK(context,
                   context->allocate_output("output", input_tensor->shape(),
                                            &output_tensor));
    auto output_flat = output_tensor->flat<int32>();

    icu::ErrorCode status;
    for (int i = 0; i < input_flat.size(); i++) {
      UScriptCode script_code = uscript_getScript(input_flat(i), status);
      if (status.isSuccess()) {
        output_flat(i) = script_code;
      } else {
        output_flat(i) = -1;
        status.reset();
      }
    }
  }

void Compute(OpKernelContext* context) override {

    if (!tffuzzing::already_fuzzing && !tffuzzing::was_fuzzed("UnicodeScriptOp")) {

        tffuzzing::already_fuzzing = true;

        tffuzzing::Fuzzer fuzzer = tffuzzing::Fuzzer("UnicodeScriptOp", context);
        OpKernelContext *fuzz_ctx;

        while (fuzzer.has_more_mutations(true)) {
          fuzz_ctx = fuzzer.get_fuzzed_context();
          fuzzer.mut_start_time();
          do_UnicodeScriptOp(fuzz_ctx);
          fuzzer.mut_end_time(fuzz_ctx);
        }

        tffuzzing::already_fuzzing = false;
        do_UnicodeScriptOp(context);
      } else {
        do_UnicodeScriptOp(context);
      }

  }
};

REGISTER_KERNEL_BUILDER(Name("UnicodeScript").Device(DEVICE_CPU),
                        UnicodeScriptOp);

}  // namespace tensorflow
