
#include "tensorflow/core/lib/core/fuzzing.h"

namespace tffuzzing {

    bool already_fuzzing = false;
    char* results_dir = "/media/tf-fuzzing/results";

    static std::fstream mutations_file;
    static std::fstream mutations_restore;
    static std::fstream crashes_file;
    static std::fstream num_crashes_file;

    bool was_fuzzed(std::string fname) {
        // printf("Fuzzed %s\n", fname.c_str());
        struct stat stat_buffer;
        char filename[100];
        snprintf(filename, sizeof(filename), "%s/%s_mutations.done", results_dir, fname.c_str());
        return stat(filename, &stat_buffer) == 0;
    }

    Fuzzer::Fuzzer(char *fname, tensorflow::OpKernelContext* ctx)
        : cur_fname(fname) {

        printf("Initializing fuzzer...\n");
        num_args = ctx->num_inputs();
        original_ctx = ctx;

        printf("Original arguments: \n");
        for (int i = 0; i < num_args; i++) {
          std::cout << "Argument " << i << ": " << ctx->input(i).DebugString() << "\n";
        }

        char filename[100];
        bool restore = false;
        long long last_mutation = -1;
        struct stat stat_buffer;
        bool has_tensor = false, has_intarrayref = false;

        glob_t glob_result;
        int glob_ret;
        memset(&glob_result, 0, sizeof(glob_result));
        pid_t mypid;
        char mutfile_pattern[256];
        char mutfile_prefix[256];
        char proc_filename[256];
        char *dirfile;
        char *existing_pid;
        char *prev_pid;

        tffuzzing::TFType type_enum;
        std::string type;
        va_list vals;

        tensorflow::Tensor tensor;
        tensorflow::TensorShape tensor_shape;

        mypid = ::getpid();

        memset(proc_filename, 0, sizeof(proc_filename));

        memset(mutfile_pattern, 0, sizeof(mutfile_pattern));
        snprintf(mutfile_pattern, sizeof(mutfile_pattern), "%s/%s_mutations.log.*", results_dir, fname);

        memset(mutfile_prefix, 0, sizeof(mutfile_prefix));
        snprintf(mutfile_prefix, sizeof(mutfile_prefix), "%s/%s_mutations.log", results_dir, fname);

        memset(filename, 0, sizeof(filename));
        snprintf(filename, sizeof(filename), "%s/%s_mutations.log.%d", results_dir, fname, mypid);
        mutations_logger_filename = filename;

        std::ios_base::openmode fflags = std::ios::out | std::ios::in | std::ios::trunc;

        for (int r = 0; r < MUTFILE_TRIES; r++){
            glob_ret = glob(mutfile_pattern, 0, NULL, &glob_result);
            if (glob_ret != GLOB_NOMATCH && !restore) {
                // A mutation file for the same function exists
                for(size_t i = 0; i < glob_result.gl_pathc && !restore; ++i) {
                    existing_pid = glob_result.gl_pathv[i] + strlen(mutfile_prefix) + 1;
                    snprintf(proc_filename, sizeof(proc_filename), "/proc/%s", existing_pid);
                    /* printf("%s\n", proc_filename); */
                    if (stat(proc_filename, &stat_buffer) == 0){
                        // The mutations file belongs to a running process, skip
                        /* printf("%s belongs to a running process, skipping\n", glob_result.gl_pathv[i]); */
                        total_mutations = 0;
                        is_running = true;
                        globfree(&glob_result);
                        return;
                    } else {
                        // The mutations file doesn't belong to any running process, something crashed
                        mutations_restore_filename = glob_result.gl_pathv[i];
                        /* printf("%s crashed, will restore from %s\n", fname, mutations_restore_filename.c_str()); */
                        mutations_file.open(mutations_logger_filename, fflags);
                        restore = true;
                    }
                }
            }
            globfree(&glob_result);
        }

        printf("fuzzing function %s\n", fname);

        // Disable buffering else program might crash before writing to logger
        if (!restore)
          mutations_file.open(mutations_logger_filename, fflags);
        mutations_file.rdbuf()->pubsetbuf(0, 0);

        for (int i = 0; i < num_args; i++) {
          indices.push_back(0);
          tensor = ctx->input(i);
          tensor_shape = tensor.shape();
          tensor_shapes.push_back(tensor_shape);
          tensor_types.push_back(tensor.dtype());
        }

        initialize_tensor_pool();

        calculate_total_mutations();
        bool got_last = false;
        int tries = 0;
        if (restore) {

            mutations_restore.open(mutations_restore_filename, std::ios::out | std::ios::in);
            /* mutations_restore.seekg(0, std::ios_base::beg); */
            std::string last_line;
            while (!got_last && tries < 10) {
              getline(mutations_restore, last_line);
              try {
                last_mutation = std::stoll(last_line);
                got_last = true;
              } catch (...) {
                /* printf("Error: reading %s (got %s)...\n", mutations_restore_filename.c_str(), last_line.c_str()); */
                tries++;
              }
            }
            mutations_restore.close();
            if (last_mutation > 0) {
              restore_last_mutation(last_mutation, fname);
              std::remove(mutations_restore_filename.c_str());
            }
            /* else { */
            /*   printf("Error: couldn't get last mutation number for %s\n", mutations_restore_filename.c_str()); */
            /* } */
            // Delete the file since we already logged the crash
        } else {
            indices[0] = -1;
        }
    }

    Fuzzer::~Fuzzer() {

/*         for (auto &tensor_val : tensor_mutations) { */
/*           //TODO check this */
/*           delete &tensor_val; */
/*         } */
        mutations_file.close();

    }

    void Fuzzer::log_backtrace(char *fname) {
      int nptrs;
      void *buffer[0x80];
      char **strings;
      int p = 0;
      int t;
      char addr[0x200];
      char command[0x300];
      char backtrace_filename[0x100];

      memset(backtrace_filename, 0, sizeof(backtrace_filename));
      snprintf(backtrace_filename, sizeof(backtrace_filename), "%s/%s_backtrace.log", results_dir, fname);

      nptrs = backtrace(buffer, 0x80);

      strings = backtrace_symbols(buffer, nptrs);

      for (int i = 0; i < nptrs; i++) {

        p = 0;
        /* printf("%s\n", strings[i]); */

        while(strings[i][p] != '(' && strings[i][p] != ' '
                && strings[i][p] != 0)
            ++p;

        t = p+1;
        while(strings[i][t] != ')' && strings[i][t] != 0)
          ++t;


        strings[i][t] = '\0';
        memset(addr, 0, 0x200);
        memcpy(addr, &strings[i][p+1], t);

        char *plus = strchr(addr, '+');
        int plusidx = (int) (plus - addr);

        if (plusidx > 0) {
          *plus = '\0';
          sprintf(command,"c++filt %s >> %s 2> /dev/null", addr,  backtrace_filename);
        } else {
          sprintf(command,"addr2line -C -f '%s' -e '%.*s' >> %s 2> /dev/null", addr, p, strings[i], backtrace_filename);
        }

        /* printf("p: %d, t: %d, string: %s, addr: %s\n", p, t, strings[i], addr); */

        /* printf("%d\n%s\n", plusidx, command); */
        system(command);

      }

      memset(command, 0, sizeof(command));
      snprintf(command, sizeof(command), "echo '==========================' >> %s", backtrace_filename);
      /* printf("%s\n", command); */
      system(command);

      free(strings);

    }

    void Fuzzer::restore_last_mutation(long long last_mutation, char *fname) {

      tensorflow::TensorValue tensor_val;

        // Handle the case where mutations were already done for this test
        // by just giving back one mutation so that the test doesn't crash
        if (last_mutation <= 0) {
            total_mutations = 1;
            return;
        }


        printf("Restoring from mutation %lld\n", last_mutation);

        // TODO will eventually use this
        log_backtrace(fname);

        char crashes_filename[100];
        snprintf(crashes_filename, sizeof(crashes_filename), "%s/%s_crashes.log", results_dir, fname);
        crashes_logger_filename = crashes_filename;
        crashes_file.rdbuf()->pubsetbuf(0, 0);
        crashes_file.open(crashes_logger_filename, std::ios::out | std::ios::app);

        // Used to bound number of crashes
        char filename[100];
        long last_crash;
        struct stat stat_buffer;
        std::ios_base::openmode fflags = std::ios::out | std::ios::in;

        memset(filename, 0, sizeof(filename));
        snprintf(filename, sizeof(filename), "%s/%s_crashes_num.log", results_dir, fname);

        if (stat(filename, &stat_buffer) == 0){
            num_crashes_file.open(filename, fflags);
            num_crashes_file.seekg(0, std::ios_base::beg);
            std::string last_line;
            getline(num_crashes_file, last_line);
            try {
              last_crash = std::stoll(last_line);
            } catch (...) {
              printf("Error while reading file with number of crashes...");
            }
        } else {
            last_crash = 0;
            fflags |= std::ios::trunc;
            num_crashes_file.open(filename, fflags);
        }
        last_crash++;
        char logbuf[20];
        snprintf(logbuf, sizeof(logbuf), "%ld\n", last_crash);
        num_crashes_file.seekg(0, std::ios::beg);
        num_crashes_file << logbuf;
        num_crashes_file.flush();
        num_crashes_file.close();

        while (total_mutations != last_mutation) {
            next_mutations_indices(false);
        }

        next_mutations_indices(true);

        for (int i = 0; i < num_args; i++) {
            tensor_val = get_next_mut();
            crashes_file << tensor_val.tensor->DebugString() << ";\n";
        }

        crashes_file << "\n--------------------------------------\n";
        crashes_file.close();

        if (last_crash >= CRASHES_BOUND) {
            printf("Function %s crashed %d times, skipping rest of fuzzing\n", fname, CRASHES_BOUND);
            total_mutations = 0;
            return;
        }

        /* next_mutations_indices(true); */
        printf("Mutations left after restoration: %llu\n", total_mutations);

    }

    void Fuzzer::calculate_total_mutations() {

        tffuzzing::TFType type_enum;
        long long nmut_fuzz;

        total_mutations = pow(tensor_mutations.size(), num_args);

        if (total_mutations <= NMUT_LOWER_BOUND) {
          num_mut_skip = 1;
        } else {
          nmut_fuzz = total_mutations / 100 * NMUT_PERCENT;
          if (nmut_fuzz > NMUT_UPPER_BOUND) {
            nmut_fuzz = NMUT_UPPER_BOUND;
          }
          num_mut_skip = total_mutations / nmut_fuzz;
        }

        all_mutations = total_mutations;
        printf("Total mutations: %llu\n", total_mutations);
        printf("Step size: %lu\n", num_mut_skip);

    }

    void Fuzzer::initialize_tensor_pool(){

        printf("Initializing pool...\n");

        tensorflow::Tensor *tensor;
        tensorflow::TensorValue *tensor_val;
        tensorflow::DataType tensor_type;
        std::vector<int64_t> fuzz_dims_vec = {};
        int64_t rand_dim, rand_size;
        int idx;

        // Random generators
        std::mt19937 rngenerator(123);
        std::uniform_int_distribution<> dims_distr(0, LARGE_TENSOR_DIMS_FUZZ);
        /* std::uniform_int_distribution<> dtypes_distr(0, tensor_dtypes.size() - 1); */
        std::uniform_int_distribution<> flip(0, 1);

        for (int i = 0; i < num_args; i++) {
          tensor = new tensorflow::Tensor(original_ctx->input(i));
          tensor_val = new tensorflow::TensorValue(tensor);
          tensor_mutations.push_back(*tensor_val);
        }

        // Create tensors with the same shapes and types as the original
        idx = 0;
        for (auto &tshape : tensor_shapes) {
            tensor_type = tensor_types.at(idx++);
            std::vector<double> contents(tshape.num_elements(), 1.0);
            tensorflow::TensorBuffer *tensor_buf((tensorflow::TensorBuffer *) &contents[0]);
            tensor = new tensorflow::Tensor(tensor_type, tshape, tensor_buf);
            tensor_val = new tensorflow::TensorValue(tensor);
            tensor_mutations.push_back(*tensor_val);
            /* tensor_contents.push_back(1); */
        }

        /* for (int i = 0; i < TENSOR_NUM_DIMS_FUZZ; i++) { */
        /*     tensor = at::ones(fuzz_dims_vec); */
        /*     tensor_mutations.push_back(tensor); */
        /*     tensor_contents.push_back(1); */
        /*     for (int j = 0; j < TENSOR_DIM_SIZE_FUZZ; j++) { */
        /*         fuzz_dims_vec.push_back(2); */
        /*     } */
        /* } */

        // Create tensors with weird data and random options
        for (auto &fuzzval : long_mutations) {
            tensor = new tensorflow::Tensor(fuzzval);
            tensor_val = new tensorflow::TensorValue(tensor);
            tensor_mutations.push_back(*tensor_val);
            /* for (int cur_ndims = 1; cur_ndims < TENSOR_NUM_DIMS_FUZZ; cur_ndims++) { */
            /*   long int dims_vec[cur_ndims]; */
            /*   for (int i = 0; i < cur_ndims; i++) { */
            /*     dims_vec[i] = dims_distr(rngenerator); */
            /*   } */
            /*   at::IntArrayRef dims = at::IntArrayRef(dims_vec, cur_ndims); */
            /*   tensor = at::full(dims, fuzzval, options); */
            /*   tensor_mutations.push_back(tensor); */
            /*   tensor_contents.push_back( (double) fuzzval); */
            /* } */
        }

        /* // Random dimensions number */
        /* fuzz_dims_vec = {}; */
        /* /1* auto ndims = dims_distr(rngenerator); *1/ */
        /* /1* auto dimsz = dims_distr(rngenerator); *1/ */
        /* for (int i = 0; i < TENSOR_NUM_DIMS_FUZZ; i++) { */
        /*     fuzz_dims_vec.push_back(TENSOR_DIM_SIZE_FUZZ); */
        /* } */
        /* auto options = c10::TensorOptions() */
        /*     .dtype(c10::kDouble) */
        /*     .layout(c10::kStrided) */
        /*     .device(c10::kCPU) */
        /*     .requires_grad(flip(rngenerator) ? true : false); */
        /* tensor = at::full(fuzz_dims_vec, LARGE_FLOAT_FUZZ ,options); */
        /* tensor_mutations.push_back(tensor); */
        /* tensor_contents.push_back( (double) LARGE_FLOAT_FUZZ); */

        printf("Pool inizialized\n");

    }

    bool Fuzzer::has_more_mutations(bool reset){
        if (reset) {
            cur_idx = 0;
            next_mutations_indices(true);
        }

        bool has_more = total_mutations > 0;

        if (!has_more && !is_running) {
            char filename[100];
            snprintf(filename, sizeof(filename), "%s/%s_mutations.done", results_dir, cur_fname.c_str());
            std::ofstream output(filename);
            /* output.rdbuf()->pubsetbuf(0, 0); */
            remove(mutations_logger_filename.c_str());
        }

        return has_more;
    }

    // Skips ahead num_mut_skip mutations to bound the total mutations
    void Fuzzer::next_mutations_indices(bool log){

        size_t pool_size = tensor_mutations.size();
        /* printf("Mutations left: %lu\n", total_mutations); */

        if (total_mutations <= 0) {
            return;
        }

        total_mutations -= num_mut_skip;

        long long passed = all_mutations - total_mutations;
        for (int i = 0; i < num_args; i++) {
            indices[i] = passed % pool_size;
            passed = passed / pool_size;
        }

        if (log) {
            char logbuf[100];
            memset(logbuf, 0, sizeof(logbuf));
            snprintf(logbuf, 100, "%llu", total_mutations);
            mutations_file.seekp(0, std::ios::beg);
            mutations_file << logbuf;
            /* mutations_file.flush(); */
        }

    }

    tensorflow::TensorValue Fuzzer::get_next_mut() {
        return tensor_mutations.at(indices[cur_idx++]);
    }

    tensorflow::OpKernelContext *Fuzzer::get_fuzzed_context() {

      tensorflow::OpKernelContext::Params *fuzz_ctx_params = original_ctx->get_params();
      std::vector<tensorflow::TensorValue> fuzz_vec;
      tensorflow::TensorValue fuzz_tensval;

      /* std::cout << "Fuzzed context contents:\n"; */

      for (int i = 0; i < num_args; i++) {
        fuzz_tensval = get_next_mut();
        fuzz_vec.push_back(fuzz_tensval);
        /* std::cout << "Argument " << i << ": " << fuzz_tensval.tensor->DebugString() << "\n"; */
      }

      tensorflow::gtl::InlinedVector<tensorflow::TensorValue, 4> *fuzz_inputs = new
        tensorflow::gtl::InlinedVector<tensorflow::TensorValue, 4>(fuzz_vec.begin(), fuzz_vec.end());
      fuzz_ctx_params->inputs = fuzz_inputs;
      tensorflow::OpKernelContext *fuzz_ctx = new tensorflow::OpKernelContext(fuzz_ctx_params);

      return fuzz_ctx;

    }

    double Fuzzer::get_tensor_contents() {
        return tensor_contents.at(indices[cur_idx - 1]);
    }

}
