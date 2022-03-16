
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
#include "tensorflow/core/framework/node_def_util.h"
#include "tensorflow/core/framework/register_types.h"
#include "tensorflow/core/framework/tensor.h"
#include "tensorflow/core/framework/tensor_shape.h"
#include "tensorflow/core/framework/types.h"
#include "tensorflow/core/lib/core/status.h"

#define NMUT_UPPER_BOUND_MID 1000000
#define NMUT_LOWER_BOUND 500000
#define CRASHES_BOUND 1
#define MUTFILE_TRIES 5
#define NS_PER_SEC (1000 * 1000 * 1000)
#define TIME_THRESH_SECS 30
#define RNG_SEED 123

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
#define BUFSZ 0x100


namespace tffuzzing {

    extern bool already_fuzzing;
    extern const char *results_dir;
    extern std::string op_name;
    extern std::string attrs;

    bool was_fuzzed(const std::string& fname);
    bool was_killed(const std::string& fname);
    void create_file(const std::string& filename, std::fstream &file, std::ios_base::openmode fflags);

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
        tensorflow::OpKernelContext *original_ctx;

        std::vector<tensorflow::int32> int_mutations{ZERO_FUZZ, LARGE_INT_FUZZ, LARGE_INT_NEG_FUZZ,
            MEDIUM_INT_FUZZ, MEDIUM_INT_NEG_FUZZ, SMALL_INT_FUZZ, SMALL_INT_NEG_FUZZ};
        // Float here, converted to Eigen::half when used
        std::vector<float> half_mutations{ZERO_FUZZ, LARGE_HALF_FUZZ, LARGE_HALF_NEG_FUZZ};
        std::vector<tensorflow::int64> long_mutations{ZERO_FUZZ, LARGE_LONG_FUZZ, LARGE_LONG_NEG_FUZZ,
            LARGE_INT_FUZZ, LARGE_INT_NEG_FUZZ,
            HUGE_LONG_FUZZ, HUGE_LONG_NEG_FUZZ
        };
        std::vector<tensorflow::int8> int8_mutations{-127, ZERO_FUZZ, 127};
        std::vector<tensorflow::uint8> uint8_mutations{ZERO_FUZZ, 255};
        std::vector<float> float_mutations{ZERO_FUZZ, LARGE_FLOAT_FUZZ, LARGE_FLOAT_NEG_FUZZ};
        std::vector<double> double_mutations{ZERO_FUZZ, LARGE_DOUBLE_FUZZ, LARGE_DOUBLE_NEG_FUZZ};
        std::vector<tensorflow::tstring> string_mutations{tensorflow::tstring(""), tensorflow::tstring(LARGE_STRING)};

        std::vector<tensorflow::Tensor> original_inputs;

        std::vector<tensorflow::TensorValue> qint8_tensor_mutations;
        std::vector<tensorflow::TensorValue> qint16_tensor_mutations;
        std::vector<tensorflow::TensorValue> qint32_tensor_mutations;
        std::vector<tensorflow::TensorValue> quint8_tensor_mutations;
        std::vector<tensorflow::TensorValue> quint16_tensor_mutations;
        std::vector<tensorflow::TensorValue> int8_tensor_mutations;
        std::vector<tensorflow::TensorValue> uint8_tensor_mutations;
        std::vector<tensorflow::TensorValue> int16_tensor_mutations;
        std::vector<tensorflow::TensorValue> uint16_tensor_mutations;
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

        tensorflow::OpKernelContext *fuzz_ctx = nullptr;

        void initialize_tensor_pools();
        void calculate_total_mutations();
        void next_mutations_indices(bool log);
        void increase_num_crashes();
        inline void inc_mutations_indices(bool log);
        void restore_last_mutation(long long last_mutation, bool log_crash);
        void log_current_mutation(std::fstream &file);
        void mark_fuzzing_done();
        void mark_unknown_type(tensorflow::DataType ttype);
        tensorflow::TensorValue *get_empty_tensor_dims(tensorflow::DataType ttype, tensorflow::TensorShape dims);
        template <class T> tensorflow::TensorValue *get_constant_tensor(T value);
        template <class T> tensorflow::TensorValue *get_flat_tensor(T value, tensorflow::Tensor *tensor);
        template <class T> tensorflow::TensorValue *get_flat_tensor_dims(T value, tensorflow::DataType ttype, tensorflow::TensorShape dims);

    public:

        Fuzzer(const std::string& fname, tensorflow::OpKernelContext* ctx);
        ~Fuzzer();

        bool has_more_mutations(bool reset);
        tensorflow::TensorValue get_next_mut(tensorflow::DataType ttype, int idx);
        tensorflow::OpKernelContext *get_fuzzed_context();

        void mut_start_time();
        void mut_end_time(tensorflow::OpKernelContext *fuzz_ctx);
    };

}

/* #endif  // TENSORFLOW_CORE_FUZZING_H_ */
