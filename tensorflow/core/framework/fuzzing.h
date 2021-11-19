
/* #ifndef TENSORFLOW_CORE_FUZZING_H_ */
/* #define TENSORFLOW_CORE_FUZZING_H_ */

#pragma once

#include <array>
#include <cstdarg>
#include <cstdio>
#include <vector>
#include <unordered_map>
#include <string>
#include <iostream>
#include <initializer_list>
#include <fstream>
#include <filesystem>
#include <random>
#include <execinfo.h>
#include <sys/stat.h>
#include <unistd.h>
#include <glob.h>
#include <stdio.h>

#include "third_party/eigen3/unsupported/Eigen/CXX11/Tensor"
#include "tensorflow/core/framework/op_kernel.h"
#include "tensorflow/core/framework/register_types.h"
#include "tensorflow/core/framework/tensor.h"
#include "tensorflow/core/framework/tensor_shape.h"
#include "tensorflow/core/framework/types.h"

#define NMUT_UPPER_BOUND 5000000
#define NMUT_LOWER_BOUND 500000
#define NMUT_PERCENT 10
#define CRASHES_BOUND 3
#define MUTFILE_TRIES 5
#define MEDIUM_INT_FUZZ 0x20000000
#define MEDIUM_INT_NEG_FUZZ -0x20000000
#define LARGE_INT_FUZZ 0x70000000
#define LARGE_INT_NEG_FUZZ -0x70000000
#define LARGE_LONG_FUZZ 0x12345678abc
#define LARGE_LONG_NEG_FUZZ -0x12345678abc
#define HUGE_LONG_FUZZ 0x7777777777777777
#define HUGE_LONG_NEG_FUZZ -0x7777777777777777
#define LARGE_FLOAT_FUZZ 3.5e+035
#define LARGE_FLOAT_NEG_FUZZ -3.5e+035
#define LARGE_DOUBLE_FUZZ 1.5e+300
#define LARGE_DOUBLE_NEG_FUZZ -1.5e+300
#define LARGE_HALF_FUZZ 65000
#define LARGE_HALF_NEG_FUZZ -65000
#define LARGE_STRING "aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaabhaabiaabjaabkaablaabmaabnaaboaabpaabqaabraabsaabtaabuaabvaabwaabxaabyaabzaacbaaccaacdaaceaacfaacgaachaaciaacjaackaaclaacmaacnaacoaacpaacqaacraacsaactaacuaacvaacwaacxaacyaac"
#define ZERO_FUZZ 0
#define SMALL_INT_FUZZ 0xfffe
#define SMALL_INT_NEG_FUZZ -0xfffe

#define TENSOR_NUM_DIMS_FUZZ 5
#define TENSOR_DIM_SIZE_FUZZ 5
#define LARGE_TENSOR_DIMS_FUZZ 30

#define FILENAME_SZ 0x100
#define LOGBUFSZ 0x20

namespace tffuzzing {

    extern bool already_fuzzing;
    extern char* results_dir;

    bool was_fuzzed(std::string fname);

    class Fuzzer {
    private:

        unsigned long num_mut_skip;
        bool is_running = false;
        long long total_mutations = 1;
        long long all_mutations;
        int cur_idx = 0;
        int num_args;
        std::string cur_fname;
        std::string mutations_logger_filename;
        std::string mutations_restore_filename;
        std::string crashes_logger_filename;
        std::vector<int> indices;
        std::vector<tensorflow::TensorShape> tensor_shapes;
        std::vector<tensorflow::DataType> tensor_types;
        /* std::vector<TFType> func_types; */
        tensorflow::OpKernelContext *original_ctx;
        tensorflow::gtl::InlinedVector<tensorflow::TensorValue, 4> *last_fuzz_inputs;

        std::vector<tensorflow::int32> int_mutations = {ZERO_FUZZ, LARGE_INT_FUZZ, LARGE_INT_NEG_FUZZ,
            MEDIUM_INT_FUZZ, MEDIUM_INT_NEG_FUZZ, SMALL_INT_FUZZ, SMALL_INT_NEG_FUZZ};
        std::vector<float> half_mutations = {ZERO_FUZZ, LARGE_HALF_FUZZ, LARGE_HALF_NEG_FUZZ};
        std::vector<tensorflow::int64> long_mutations = {ZERO_FUZZ, LARGE_LONG_FUZZ, LARGE_LONG_NEG_FUZZ,
            LARGE_INT_FUZZ, LARGE_INT_NEG_FUZZ,
            HUGE_LONG_FUZZ, HUGE_LONG_NEG_FUZZ
            /* MEDIUM_INT_FUZZ, MEDIUM_INT_NEG_FUZZ, */
        };
        std::vector<tensorflow::uint8> int8_mutations = {-127, ZERO_FUZZ, 127};
        std::vector<tensorflow::uint8> uint8_mutations = {ZERO_FUZZ, 255};
        std::vector<float> float_mutations = {ZERO_FUZZ, LARGE_FLOAT_FUZZ, LARGE_FLOAT_NEG_FUZZ};
        std::vector<double> double_mutations = {ZERO_FUZZ, LARGE_DOUBLE_FUZZ, LARGE_DOUBLE_NEG_FUZZ};
        std::vector<tensorflow::tstring> string_mutations = {tensorflow::tstring(""), tensorflow::tstring(LARGE_STRING)};
        std::vector<tensorflow::TensorValue> qint8_tensor_mutations;
        std::vector<tensorflow::TensorValue> qint16_tensor_mutations;
        std::vector<tensorflow::TensorValue> qint32_tensor_mutations;
        std::vector<tensorflow::TensorValue> quint8_tensor_mutations;
        std::vector<tensorflow::TensorValue> quint16_tensor_mutations;
        std::vector<tensorflow::TensorValue> int8_tensor_mutations;
        std::vector<tensorflow::TensorValue> uint8_tensor_mutations;
        std::vector<tensorflow::TensorValue> int32_tensor_mutations;
        std::vector<tensorflow::TensorValue> uint32_tensor_mutations;
        std::vector<tensorflow::TensorValue> int64_tensor_mutations;
        std::vector<tensorflow::TensorValue> uint64_tensor_mutations;
        std::vector<tensorflow::TensorValue> half_tensor_mutations;
        std::vector<tensorflow::TensorValue> float_tensor_mutations;
        std::vector<tensorflow::TensorValue> double_tensor_mutations;
        std::vector<tensorflow::TensorValue> bool_tensor_mutations;
        std::vector<tensorflow::TensorValue> string_tensor_mutations;
        std::vector<int> pool_sizes;
        /* std::vector<double> tensor_contents; */

        void log_backtrace(char *fname);
        void initialize_tensor_pools();
        void calculate_total_mutations();
        void next_mutations_indices(bool log);
        inline void inc_mutations_indices(bool log);
        void restore_last_mutation(long long last_mutation, char *fname);
        tensorflow::OpKernelContext *fuzz_ctx = nullptr;
        void mark_fuzzing_done();
        void mark_unknown_type(tensorflow::DataType ttype);
        template <class T> tensorflow::TensorValue *get_constant_tensor(T value, tensorflow::Tensor *tensor);

    public:

        Fuzzer(char *fname, tensorflow::OpKernelContext* ctx);
        ~Fuzzer();

        bool has_more_mutations(bool reset);
        tensorflow::TensorValue get_next_mut(tensorflow::DataType ttype, int idx);
        tensorflow::OpKernelContext *get_fuzzed_context();
    };

}

/* #endif  // TENSORFLOW_CORE_FUZZING_H_ */
