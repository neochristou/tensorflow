
#include "tensorflow/core/framework/fuzzing.h"

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
    int retval;
    char *stat_filename = new char[FILENAME_SZ];
    memset(stat_filename, 0, FILENAME_SZ);
    snprintf(stat_filename, FILENAME_SZ, "%s/%s_mutations.done", results_dir, fname.c_str());
    retval = stat(stat_filename, &stat_buffer) == 0;
    delete[] stat_filename;
    return retval;
  }

  Fuzzer::Fuzzer(char *fname, tensorflow::OpKernelContext* ctx)
    : cur_fname(fname) {

      /* printf("Initializing fuzzer...\n"); */
      num_args = ctx->num_inputs();
      original_ctx = ctx;

      filename = new char[FILENAME_SZ];

      /* printf("Original arguments: \n"); */
      /* for (int i = 0; i < num_args; i++) { */
      /*   std::cout << "Argument " << i << ": " << ctx->input(i).DebugString() << "\n"; */
      /* } */

      bool restore = false;
      long long last_mutation = -1;
      struct stat stat_buffer;
      bool has_tensor = false, has_intarrayref = false;

      glob_t glob_result;
      int glob_ret;
      pid_t mypid;
      char *dirfile;
      char *existing_pid;
      char *prev_pid;

      memset(&glob_result, 0, sizeof(glob_result));

      tensorflow::Tensor tensor;
      tensorflow::TensorShape tensor_shape;

      mypid = ::getpid();

      char *mutfile_pattern = new char[BUFSZ];
      char *mutfile_prefix = new char[BUFSZ];
      char *proc_filename = new char[BUFSZ];

      memset(proc_filename, 0, BUFSZ);
      memset(mutfile_pattern, 0, BUFSZ);
      memset(mutfile_prefix, 0, BUFSZ);
      memset(filename, 0, FILENAME_SZ);

      snprintf(mutfile_pattern, BUFSZ, "%s/%s_mutations.log.*", results_dir, fname);
      snprintf(mutfile_prefix, BUFSZ, "%s/%s_mutations.log", results_dir, fname);
      snprintf(filename, BUFSZ, "%s/%s_mutations.log.%d", results_dir, fname, mypid);

      mutations_logger_filename = filename;

      std::ios_base::openmode fflags = std::ios::out | std::ios::in | std::ios::trunc;

      for (int r = 0; r < MUTFILE_TRIES; r++){
        glob_ret = glob(mutfile_pattern, 0, NULL, &glob_result);
        if (glob_ret != GLOB_NOMATCH && !restore) {
          // A mutation file for the same function exists
          /* std::cout << "Found mutation file for " << fname << std::endl << std::flush; */
          for(size_t i = 0; i < glob_result.gl_pathc && !restore; ++i) {
            existing_pid = glob_result.gl_pathv[i] + strlen(mutfile_prefix) + 1;
            snprintf(proc_filename, BUFSZ, "/proc/%s", existing_pid);
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
              printf("%s crashed, will restore from %s\n", fname, mutations_restore_filename.c_str());
              mutations_file.open(mutations_logger_filename, fflags);
              restore = true;
            }
          }
        }
        /* else { */
        /* std::cout << "No mutation file found for " << fname << std::endl << std::flush; */
        /* } */
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
        /* std::cout << "Type: " << tensor.dtype() << "\n"; */
      }

      initialize_tensor_pools();
      calculate_total_mutations();

      bool got_last = false;
      int tries = 0;
      if (restore) {

        mutations_restore.open(mutations_restore_filename, std::ios::out | std::ios::in);
        std::string last_line;
        while (!got_last && tries < 10) {
          getline(mutations_restore, last_line);
          /* last_line.erase(std::find(last_line.begin(), last_line.end(), '\0'), last_line.end()); */
          /* std::cout << "Got " << last_line << " with length " << last_line.length() << std::endl << std::flush; */
          if (last_line.length() > 0) {
            char *line_end;
            last_mutation = std::strtoll(last_line.c_str(), &line_end, 10);
            /* std::cout << "Crashing mutation: " << last_mutation << std::endl << std::flush; */
            got_last = true;
          } else {
            printf("Error: reading %s (got %s)...\n", mutations_restore_filename.c_str(), last_line.c_str());
            tries++;
          }
        }
        mutations_restore.close();
        if (last_mutation > 0) {
          restore_last_mutation(last_mutation, fname);
          // Delete the file since we already logged the crash
          /* std::cout << "Removing " << mutations_restore_filename << std::endl << std::flush; */
          if (std::remove(mutations_restore_filename.c_str()) != 0) {
            /* std::cout << "Couldn't remove " << mutations_restore_filename << std::flush; */
          }
        }
        /* else { */
        /*   printf("Error: couldn't get last mutation number for %s\n", mutations_restore_filename.c_str()); */
        /* } */
      } else {
        indices[0] = -1;
      }

      delete[] mutfile_pattern;
      delete[] mutfile_prefix;
      delete[] proc_filename;
    }

  Fuzzer::~Fuzzer() {

    /*         for (auto &tensor_val : tensor_mutations) { */
    /*           //TODO check this */
    /*           delete &tensor_val; */
    /*         } */
    mutations_file.close();
    delete[] filename;

  }

  void Fuzzer::log_backtrace(char *fname) {
    int nptrs;
    void *buffer[0x80];
    char **strings;
    int p = 0;
    int t;

    char *addr = new char[0x200];
    char *command = new char[0x300];
    char *backtrace_filename = new char[BUFSZ];

    memset(backtrace_filename, 0, BUFSZ);
    snprintf(backtrace_filename, BUFSZ, "%s/%s_backtrace.log", results_dir, fname);

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

    memset(command, 0, 0x300);
    snprintf(command, 0x300, "echo '==========================' >> %s", backtrace_filename);
    /* printf("%s\n", command); */
    system(command);

    free(strings);
    delete[] addr;
    delete[] command;
    delete[] backtrace_filename;

  }

  void Fuzzer::restore_last_mutation(long long last_mutation, char *fname) {

    tensorflow::TensorValue tensor_val;
    tensorflow::Tensor tensor;
    tensorflow::DataType ttype;

    // Handle the case where mutations were already done for this test
    // by just giving back one mutation so that the test doesn't crash
    if (last_mutation <= 0) {
      total_mutations = 1;
      return;
    }

    printf("Restoring from mutation %lld\n", last_mutation);

    log_backtrace(fname);

    char *crashes_filename = new char[BUFSZ];
    char *logbuf = new char[LOGBUFSZ];
    long last_crash; // Used to bound number of crashes
    struct stat stat_buffer;
    std::ios_base::openmode fflags = std::ios::out | std::ios::in;

    snprintf(crashes_filename, BUFSZ, "%s/%s_crashes.log", results_dir, fname);
    crashes_logger_filename = crashes_filename;
    crashes_file.rdbuf()->pubsetbuf(0, 0);
    crashes_file.open(crashes_logger_filename, std::ios::out | std::ios::app);

    memset(filename, 0, FILENAME_SZ);
    snprintf(filename, FILENAME_SZ, "%s/%s_crashes_num.log", results_dir, fname);

    if (stat(filename, &stat_buffer) == 0){
      num_crashes_file.open(filename, fflags);
      std::string last_line;
      getline(num_crashes_file, last_line);
      if (last_line.length() > 0) {
        char *line_end;
        last_crash = std::strtoll(last_line.c_str(), &line_end, 10);
      } else {
        std::cout << "Error while reading file with number of crashes..." << std::flush;
      }
    } else {
      last_crash = 0;
      fflags |= std::ios::trunc;
      num_crashes_file.open(filename, fflags);
    }
    last_crash++;

    memset(logbuf, 0, LOGBUFSZ);
    snprintf(logbuf, LOGBUFSZ, "%ld\n", last_crash);

    num_crashes_file.seekp(0, std::ios::beg);
    num_crashes_file.write(logbuf, LOGBUFSZ);
    num_crashes_file.flush();
    num_crashes_file.close();

    while (total_mutations != last_mutation) {
      next_mutations_indices(false);
    }

    /* next_mutations_indices(true); */

    for (int idx = 0; idx < num_args; idx++) {
      ttype = tensor_types.at(idx);
      switch (ttype) {
        default: {
                   std::cout << "\033[1;31mUnknown type:\033[0m " << ttype << std::endl << std::flush;
                   abort();
                 }
        case tensorflow::DataType::DT_INT32: {
                                               tensor_val = get_next_mut_int();
                                               break;
                                             }
        case tensorflow::DataType::DT_INT64: {
                                               tensor_val = get_next_mut_long();
                                               break;
                                             }
        case tensorflow::DataType::DT_UINT32: {
                                               tensor_val = get_next_mut_uint();
                                               break;
                                             }
        case tensorflow::DataType::DT_UINT64: {
                                               tensor_val = get_next_mut_ulong();
                                               break;
                                             }
        case tensorflow::DataType::DT_FLOAT: {
                                               tensor_val = get_next_mut_float();
                                               break;
                                             }
        case tensorflow::DataType::DT_HALF: {
                                               tensor_val = get_next_mut_half();
                                               break;
                                             }
        case tensorflow::DataType::DT_DOUBLE: {
                                                tensor_val = get_next_mut_double();
                                                break;
                                              }
        case tensorflow::DataType::DT_BOOL: {
                                              tensor_val = get_next_mut_bool();
                                              break;
                                            }
        case tensorflow::DataType::DT_STRING: {
                                              tensor_val = get_next_mut_string();
                                              break;
                                            }
        case tensorflow::DataType::DT_VARIANT:
        case tensorflow::DataType::DT_COMPLEX64:
        case tensorflow::DataType::DT_COMPLEX128:
        case tensorflow::DataType::DT_RESOURCE: {
                                              tensor = tensorflow::Tensor(original_ctx->input(idx));
                                              tensor_val = tensorflow::TensorValue(&tensor);
                                              break;
                                            }
      }
      crashes_file << tensor_val.tensor->DebugString() << "\n";
    }

    crashes_file << "\n--------------------------------------\n";
    crashes_file.close();

    if (last_crash >= CRASHES_BOUND) {
      printf("Function %s crashed %d times, skipping rest of fuzzing\n", fname, CRASHES_BOUND);
      total_mutations = 0;
      return;
    }

    next_mutations_indices(true);
    printf("Mutations left after restoration: %llu\n", total_mutations);

    delete[] crashes_filename;
    delete[] logbuf;

  }

  void Fuzzer::calculate_total_mutations() {

    long long nmut_fuzz;

    for (auto &ttype : tensor_types) {
      switch (ttype) {
        default: {
                   std::cout << "\033[1;31mUnknown type:\033[0m " << ttype << std::endl << std::flush;
                   abort();
                 }
        case tensorflow::DataType::DT_INT32: {
                                               total_mutations *= int_tensor_mutations.size();
                                               pool_sizes.push_back(int_tensor_mutations.size());
                                               break;
                                             }
        case tensorflow::DataType::DT_INT64: {
                                               total_mutations *= long_tensor_mutations.size();
                                               pool_sizes.push_back(long_tensor_mutations.size());
                                               break;
                                             }
        case tensorflow::DataType::DT_UINT32: {
                                               total_mutations *= uint_tensor_mutations.size();
                                               pool_sizes.push_back(uint_tensor_mutations.size());
                                               break;
                                             }
        case tensorflow::DataType::DT_UINT64: {
                                               total_mutations *= ulong_tensor_mutations.size();
                                               pool_sizes.push_back(ulong_tensor_mutations.size());
                                               break;
                                             }
        case tensorflow::DataType::DT_HALF: {
                                               total_mutations *= half_tensor_mutations.size();
                                               pool_sizes.push_back(half_tensor_mutations.size());
                                               break;
                                             }
        case tensorflow::DataType::DT_FLOAT: {
                                               total_mutations *= float_tensor_mutations.size();
                                               pool_sizes.push_back(float_tensor_mutations.size());
                                               break;
                                             }
        case tensorflow::DataType::DT_DOUBLE: {
                                                total_mutations *= double_tensor_mutations.size();
                                                pool_sizes.push_back(double_tensor_mutations.size());
                                                break;
                                              }
        case tensorflow::DataType::DT_BOOL: {
                                              total_mutations *= bool_tensor_mutations.size();
                                              pool_sizes.push_back(bool_tensor_mutations.size());
                                              break;
                                            }
        case tensorflow::DataType::DT_STRING: {
                                              total_mutations *= string_tensor_mutations.size();
                                              pool_sizes.push_back(string_tensor_mutations.size());
                                              break;
                                            }
        case tensorflow::DataType::DT_VARIANT:
        case tensorflow::DataType::DT_COMPLEX64:
        case tensorflow::DataType::DT_COMPLEX128:
        case tensorflow::DataType::DT_RESOURCE: {
                                              break;
                                            }
      }
    }

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
    /* printf("Step size: %lu\n", num_mut_skip); */

  }

  void Fuzzer::initialize_tensor_pools(){

    /* printf("Initializing pools...\n"); */

    tensorflow::Tensor *tensor;
    tensorflow::TensorValue *tensor_val;
    tensorflow::DataType tensor_type;
    tensorflow::TensorShape dims;
    std::vector<int64_t> fuzz_dims_vec = {};
    int64_t rand_dim, rand_size;
    int idx;
    int rand_int;
    long rand_long;
    float rand_float;
    Eigen::half rand_half;
    double rand_double;
    tensorflow::tstring rand_string;

    // Random generators
    std::mt19937 rngenerator(123);
    std::uniform_int_distribution<> dims_distr(0, LARGE_TENSOR_DIMS_FUZZ);
    std::uniform_int_distribution<> int_distr(0, int_mutations.size() - 1);
    std::uniform_int_distribution<> long_distr(0, long_mutations.size() - 1);
    std::uniform_int_distribution<> float_distr(0, float_mutations.size() - 1);
    std::uniform_int_distribution<> half_distr(0, half_mutations.size() - 1);
    std::uniform_int_distribution<> double_distr(0, double_mutations.size() - 1);
    std::uniform_int_distribution<> string_distr(0, string_mutations.size() - 1);
    std::uniform_int_distribution<> flip(0, 1);

    /* std::cout << "Creating mutations same as input\n" << std::flush; */
    // Copy original arguments
    for (int i = 0; i < num_args; i++) {
      tensor = new tensorflow::Tensor(original_ctx->input(i));
      tensor_val = new tensorflow::TensorValue(tensor);
      tensor_type = tensor_types.at(i);
      switch (tensor_type) {
        default: {
                   std::cout << "\033[1;31mUnknown type:\033[0m " << tensor_type << std::endl << std::flush;
                   abort();
                 }
        case tensorflow::DataType::DT_INT32: {
                                               int_tensor_mutations.push_back(*tensor_val);
                                               break;
                                             }
        case tensorflow::DataType::DT_INT64: {
                                               long_tensor_mutations.push_back(*tensor_val);
                                               break;
                                             }
        case tensorflow::DataType::DT_UINT32: {
                                               uint_tensor_mutations.push_back(*tensor_val);
                                               break;
                                             }
        case tensorflow::DataType::DT_UINT64: {
                                               ulong_tensor_mutations.push_back(*tensor_val);
                                               break;
                                             }
        case tensorflow::DataType::DT_HALF: {
                                               half_tensor_mutations.push_back(*tensor_val);
                                               break;
                                             }
        case tensorflow::DataType::DT_FLOAT: {
                                               float_tensor_mutations.push_back(*tensor_val);
                                               break;
                                             }
        case tensorflow::DataType::DT_DOUBLE: {
                                                double_tensor_mutations.push_back(*tensor_val);
                                                break;
                                              }
        case tensorflow::DataType::DT_STRING: {
                                                string_tensor_mutations.push_back(*tensor_val);
                                                break;
                                              }
        case tensorflow::DataType::DT_BOOL: // Will just create both later
        // We don't create mutations for these
        case tensorflow::DataType::DT_VARIANT:
        case tensorflow::DataType::DT_COMPLEX64:
        case tensorflow::DataType::DT_COMPLEX128:
        case tensorflow::DataType::DT_RESOURCE: {
                                              break;
                                            }
      }
    }

    // Create tensors with the same shapes as the original
    // but change values by picking a random value from the
    // mutations of the corresponding data type
    // plus a Tensor with zeroes for the integral types
    idx = 0;
    for (auto &tshape : tensor_shapes) {
      tensor_type = tensor_types.at(idx++);

      tensor = new tensorflow::Tensor(tensor_type, tshape);
      switch (tensor_type) {
        default: {
                   std::cout << "\033[1;31mUnknown type:\033[0m " << tensor_type << std::endl << std::flush;
                   abort();
                 }
        case tensorflow::DataType::DT_INT32: {
                                               rand_int = int_mutations.at(int_distr(rngenerator));
                                               tensor->flat<int>().setConstant(rand_int);
                                               tensor_val = new tensorflow::TensorValue(tensor);
                                               int_tensor_mutations.push_back(*tensor_val);

                                               tensor = new tensorflow::Tensor(tensor_type, tshape);
                                               tensor->flat<int>().setConstant(0);
                                               tensor_val = new tensorflow::TensorValue(tensor);
                                               int_tensor_mutations.push_back(*tensor_val);
                                               break;
                                             }
        case tensorflow::DataType::DT_INT64: {
                                               rand_long = long_mutations.at(long_distr(rngenerator));
                                               tensor->flat<long>().setConstant(rand_long);
                                               tensor_val = new tensorflow::TensorValue(tensor);
                                               long_tensor_mutations.push_back(*tensor_val);

                                               tensor = new tensorflow::Tensor(tensor_type, tshape);
                                               tensor->flat<long>().setConstant(0);
                                               tensor_val = new tensorflow::TensorValue(tensor);
                                               long_tensor_mutations.push_back(*tensor_val);
                                               break;
                                             }
        case tensorflow::DataType::DT_UINT32: {
                                               rand_int = int_mutations.at(int_distr(rngenerator));
                                               tensor->flat<unsigned int>().setConstant(rand_int);
                                               tensor_val = new tensorflow::TensorValue(tensor);
                                               uint_tensor_mutations.push_back(*tensor_val);

                                               tensor = new tensorflow::Tensor(tensor_type, tshape);
                                               tensor->flat<unsigned int>().setConstant(0);
                                               tensor_val = new tensorflow::TensorValue(tensor);
                                               uint_tensor_mutations.push_back(*tensor_val);
                                               break;
                                             }
        case tensorflow::DataType::DT_UINT64: {
                                               rand_long = long_mutations.at(long_distr(rngenerator));
                                               tensor->flat<unsigned long>().setConstant(rand_long);
                                               tensor_val = new tensorflow::TensorValue(tensor);
                                               ulong_tensor_mutations.push_back(*tensor_val);

                                               tensor = new tensorflow::Tensor(tensor_type, tshape);
                                               tensor->flat<unsigned long>().setConstant(0);
                                               tensor_val = new tensorflow::TensorValue(tensor);
                                               ulong_tensor_mutations.push_back(*tensor_val);
                                               break;
                                             }
        case tensorflow::DataType::DT_HALF: {
                                               rand_half = Eigen::half(half_mutations.at(half_distr(rngenerator)));
                                               tensor->flat<Eigen::half>().setConstant(rand_half);
                                               tensor_val = new tensorflow::TensorValue(tensor);
                                               half_tensor_mutations.push_back(*tensor_val);

                                               tensor = new tensorflow::Tensor(tensor_type, tshape);
                                               tensor->flat<Eigen::half>().setConstant(Eigen::half(0.0));
                                               tensor_val = new tensorflow::TensorValue(tensor);
                                               half_tensor_mutations.push_back(*tensor_val);
                                               break;
                                             }
        case tensorflow::DataType::DT_FLOAT: {
                                               rand_float = float_mutations.at(float_distr(rngenerator));
                                               tensor->flat<float>().setConstant(rand_float);
                                               tensor_val = new tensorflow::TensorValue(tensor);
                                               float_tensor_mutations.push_back(*tensor_val);

                                               tensor = new tensorflow::Tensor(tensor_type, tshape);
                                               tensor->flat<float>().setConstant(0);
                                               tensor_val = new tensorflow::TensorValue(tensor);
                                               float_tensor_mutations.push_back(*tensor_val);
                                               break;
                                             }
        case tensorflow::DataType::DT_DOUBLE: {
                                                rand_double = double_mutations.at(double_distr(rngenerator));
                                                tensor->flat<double>().setConstant(rand_double);
                                                tensor_val = new tensorflow::TensorValue(tensor);
                                                double_tensor_mutations.push_back(*tensor_val);

                                                tensor = new tensorflow::Tensor(tensor_type, tshape);
                                                tensor->flat<double>().setConstant(0);
                                                tensor_val = new tensorflow::TensorValue(tensor);
                                                double_tensor_mutations.push_back(*tensor_val);
                                                break;
                                              }
        case tensorflow::DataType::DT_BOOL: // Will just create both later
        // Don't create other mutations for these
        case tensorflow::DataType::DT_VARIANT:
        case tensorflow::DataType::DT_STRING:
        case tensorflow::DataType::DT_COMPLEX64:
        case tensorflow::DataType::DT_COMPLEX128:
        case tensorflow::DataType::DT_RESOURCE: {
                                              break;
                                            }
      }

      /* std::cout  << tensor_val->tensor->DebugString() << std::endl; */
    }

    /* for (int i = 0; i < TENSOR_NUM_DIMS_FUZZ; i++) { */
    /*     tensor = at::ones(fuzz_dims_vec); */
    /*     tensor_mutations.push_back(tensor); */
    /*     tensor_contents.push_back(1); */
    /*     for (int j = 0; j < TENSOR_DIM_SIZE_FUZZ; j++) { */
    /*         fuzz_dims_vec.push_back(2); */
    /*     } */
    /* } */

    /* std::cout << "Creating mutations single value\n" << std::flush; */
    // Create tensors with single value and no value
    for (auto &fuzzval : int_mutations) {
      tensor = new tensorflow::Tensor(fuzzval);
      tensor_val = new tensorflow::TensorValue(tensor);
      int_tensor_mutations.push_back(*tensor_val);

      dims = tensorflow::TensorShape();
      dims.AddDim(0);
      tensor = new tensorflow::Tensor(tensorflow::DataType::DT_INT32, dims);
      tensor_val = new tensorflow::TensorValue(tensor);
      int_tensor_mutations.push_back(*tensor_val);
    }
    for (auto &fuzzval : long_mutations) {
      tensor = new tensorflow::Tensor(fuzzval);
      tensor_val = new tensorflow::TensorValue(tensor);
      long_tensor_mutations.push_back(*tensor_val);

      dims = tensorflow::TensorShape();
      dims.AddDim(0);
      tensor = new tensorflow::Tensor(tensorflow::DataType::DT_INT64, dims);
      tensor_val = new tensorflow::TensorValue(tensor);
      long_tensor_mutations.push_back(*tensor_val);
    }
    for (auto &fuzzval : half_mutations) {
      tensor = new tensorflow::Tensor(Eigen::half(fuzzval));
      tensor_val = new tensorflow::TensorValue(tensor);
      half_tensor_mutations.push_back(*tensor_val);

      dims = tensorflow::TensorShape();
      dims.AddDim(0);
      tensor = new tensorflow::Tensor(tensorflow::DataType::DT_HALF, dims);
      tensor_val = new tensorflow::TensorValue(tensor);
      half_tensor_mutations.push_back(*tensor_val);
    }
    for (auto &fuzzval : float_mutations) {
      tensor = new tensorflow::Tensor(fuzzval);
      tensor_val = new tensorflow::TensorValue(tensor);
      float_tensor_mutations.push_back(*tensor_val);

      dims = tensorflow::TensorShape();
      dims.AddDim(0);
      tensor = new tensorflow::Tensor(tensorflow::DataType::DT_FLOAT, dims);
      tensor_val = new tensorflow::TensorValue(tensor);
      float_tensor_mutations.push_back(*tensor_val);
    }
    for (auto &fuzzval : double_mutations) {
      tensor = new tensorflow::Tensor(fuzzval);
      tensor_val = new tensorflow::TensorValue(tensor);
      double_tensor_mutations.push_back(*tensor_val);

      dims = tensorflow::TensorShape();
      dims.AddDim(0);
      tensor = new tensorflow::Tensor(tensorflow::DataType::DT_DOUBLE, dims);
      tensor_val = new tensorflow::TensorValue(tensor);
      int_tensor_mutations.push_back(*tensor_val);
    }
    for (auto &fuzzval : string_mutations) {
      tensor = new tensorflow::Tensor(fuzzval);
      tensor_val = new tensorflow::TensorValue(tensor);
      string_tensor_mutations.push_back(*tensor_val);

      dims = tensorflow::TensorShape();
      dims.AddDim(0);
      tensor = new tensorflow::Tensor(tensorflow::DataType::DT_STRING, dims);
      tensor_val = new tensorflow::TensorValue(tensor);
      string_tensor_mutations.push_back(*tensor_val);
    }
    tensor = new tensorflow::Tensor(true);
    tensor_val = new tensorflow::TensorValue(tensor);
    bool_tensor_mutations.push_back(*tensor_val);
    tensor = new tensorflow::Tensor(false);
    tensor_val = new tensorflow::TensorValue(tensor);
    bool_tensor_mutations.push_back(*tensor_val);

    // Create tensors with increasing number of dimensions, random values
    for (int cur_ndims = 1; cur_ndims < TENSOR_NUM_DIMS_FUZZ; cur_ndims++) {
      dims = tensorflow::TensorShape();
      for (int i = 0; i < cur_ndims; i++) {
        rand_dim = dims_distr(rngenerator);
        dims.AddDim(rand_dim);
      }


      tensor = new tensorflow::Tensor(tensorflow::DataType::DT_INT32, dims);
      rand_int = int_mutations.at(int_distr(rngenerator));
      tensor->flat<int>().setConstant(rand_int);
      tensor_val = new tensorflow::TensorValue(tensor);
      int_tensor_mutations.push_back(*tensor_val);

      tensor = new tensorflow::Tensor(tensorflow::DataType::DT_INT64, dims);
      rand_long = long_mutations.at(long_distr(rngenerator));
      tensor->flat<long>().setConstant(rand_long);
      tensor_val = new tensorflow::TensorValue(tensor);
      long_tensor_mutations.push_back(*tensor_val);

      tensor = new tensorflow::Tensor(tensorflow::DataType::DT_UINT32, dims);
      rand_int = int_mutations.at(int_distr(rngenerator));
      tensor->flat<unsigned int>().setConstant(rand_int);
      tensor_val = new tensorflow::TensorValue(tensor);
      uint_tensor_mutations.push_back(*tensor_val);

      tensor = new tensorflow::Tensor(tensorflow::DataType::DT_UINT64, dims);
      rand_long = long_mutations.at(long_distr(rngenerator));
      tensor->flat<unsigned long>().setConstant(rand_long);
      tensor_val = new tensorflow::TensorValue(tensor);
      ulong_tensor_mutations.push_back(*tensor_val);

      tensor = new tensorflow::Tensor(tensorflow::DataType::DT_FLOAT, dims);
      rand_float = float_mutations.at(float_distr(rngenerator));
      tensor->flat<float>().setConstant(rand_float);
      tensor_val = new tensorflow::TensorValue(tensor);
      float_tensor_mutations.push_back(*tensor_val);

      tensor = new tensorflow::Tensor(tensorflow::DataType::DT_HALF, dims);
      rand_half = Eigen::half(half_mutations.at(half_distr(rngenerator)));
      tensor->flat<Eigen::half>().setConstant(rand_half);
      tensor_val = new tensorflow::TensorValue(tensor);
      half_tensor_mutations.push_back(*tensor_val);

      tensor = new tensorflow::Tensor(tensorflow::DataType::DT_DOUBLE, dims);
      rand_double = double_mutations.at(double_distr(rngenerator));
      tensor->flat<double>().setConstant(rand_double);
      tensor_val = new tensorflow::TensorValue(tensor);
      double_tensor_mutations.push_back(*tensor_val);
    }


  }

  bool Fuzzer::has_more_mutations(bool reset){

    if (reset) {
      cur_idx = 0;
      next_mutations_indices(true);
    }

    bool has_more = total_mutations > 0;

    if (!has_more && !is_running) {
      memset(filename, 0, FILENAME_SZ);
      snprintf(filename, FILENAME_SZ, "%s/%s_mutations.done", results_dir, cur_fname.c_str());
      std::ofstream output(filename);
      /* output.rdbuf()->pubsetbuf(0, 0); */
      remove(mutations_logger_filename.c_str());
    }

    return has_more;
  }

  // Skips ahead num_mut_skip mutations to bound the total mutations
  void Fuzzer::next_mutations_indices(bool log){

    /* printf("Mutations left: %lu\n", total_mutations); */

    if (total_mutations <= 0) {
      return;
    }

    total_mutations -= num_mut_skip;

    long long passed = all_mutations - total_mutations;
    for (int i = 0; i < num_args; i++) {
      indices[i] = passed % pool_sizes[i];
      passed = passed / pool_sizes[i];
    }

    if (log) {
      char *logbuf = new char[LOGBUFSZ];
      memset(logbuf, 0, LOGBUFSZ);
      snprintf(logbuf, LOGBUFSZ, "%llu", total_mutations);
      mutations_file.seekp(0, std::ios::beg);
      mutations_file.write(logbuf, LOGBUFSZ);
      mutations_file.flush();
      delete[] logbuf;
    }

  }

  tensorflow::TensorValue Fuzzer::get_next_mut_int() {
    return int_tensor_mutations.at(indices[cur_idx++]);
  }

  tensorflow::TensorValue Fuzzer::get_next_mut_long() {
    return long_tensor_mutations.at(indices[cur_idx++]);
  }

  tensorflow::TensorValue Fuzzer::get_next_mut_uint() {
    return uint_tensor_mutations.at(indices[cur_idx++]);
  }

  tensorflow::TensorValue Fuzzer::get_next_mut_ulong() {
    return ulong_tensor_mutations.at(indices[cur_idx++]);
  }


  tensorflow::TensorValue Fuzzer::get_next_mut_float() {
    return float_tensor_mutations.at(indices[cur_idx++]);
  }

  tensorflow::TensorValue Fuzzer::get_next_mut_half() {
    return half_tensor_mutations.at(indices[cur_idx++]);
  }

  tensorflow::TensorValue Fuzzer::get_next_mut_double() {
    return double_tensor_mutations.at(indices[cur_idx++]);
  }

  tensorflow::TensorValue Fuzzer::get_next_mut_bool() {
    return bool_tensor_mutations.at(indices[cur_idx++]);
  }

  tensorflow::TensorValue Fuzzer::get_next_mut_string() {
    return string_tensor_mutations.at(indices[cur_idx++]);
  }

  tensorflow::OpKernelContext *Fuzzer::get_fuzzed_context() {

    tensorflow::DataType ttype;

    if (fuzz_ctx) {
      /* delete (*fuzz_ctx->get_params()).inputs; */
      delete last_fuzz_inputs;
      delete fuzz_ctx;
    }

    tensorflow::OpKernelContext::Params *fuzz_ctx_params = original_ctx->get_params();
    std::vector<tensorflow::TensorValue> fuzz_vec;
    tensorflow::TensorValue fuzz_tensval;
    tensorflow::Tensor tensor;

    /* std::cout << "Fuzzed context contents:\n"; */

    for (int idx = 0; idx < num_args; idx++) {
      ttype = tensor_types.at(idx);
      switch (ttype) {
        default: {
                   std::cout << "\033[1;31mUnknown type:\033[0m " << ttype << std::endl << std::flush;
                   abort();
                 }
        case tensorflow::DataType::DT_INT32: {
                                               fuzz_tensval = get_next_mut_int();
                                               break;
                                             }
        case tensorflow::DataType::DT_INT64: {
                                               fuzz_tensval = get_next_mut_long();
                                               break;
                                             }
        case tensorflow::DataType::DT_UINT32: {
                                               fuzz_tensval = get_next_mut_uint();
                                               break;
                                             }
        case tensorflow::DataType::DT_UINT64: {
                                               fuzz_tensval = get_next_mut_ulong();
                                               break;
                                             }
        case tensorflow::DataType::DT_HALF: {
                                               fuzz_tensval = get_next_mut_half();
                                               break;
                                             }
        case tensorflow::DataType::DT_FLOAT: {
                                               fuzz_tensval = get_next_mut_float();
                                               break;
                                             }
        case tensorflow::DataType::DT_DOUBLE: {
                                                fuzz_tensval = get_next_mut_double();
                                                break;
                                              }
        case tensorflow::DataType::DT_BOOL: {
                                              fuzz_tensval = get_next_mut_bool();
                                              break;
                                            }
        case tensorflow::DataType::DT_STRING: {
                                              fuzz_tensval = get_next_mut_string();
                                              break;
                                            }
        case tensorflow::DataType::DT_VARIANT:
        case tensorflow::DataType::DT_COMPLEX64:
        case tensorflow::DataType::DT_COMPLEX128:
        case tensorflow::DataType::DT_RESOURCE: {
                                              tensor = tensorflow::Tensor(original_ctx->input(idx));
                                              fuzz_tensval = *(new tensorflow::TensorValue(&tensor));
                                              break;
                                            }
      }
      fuzz_vec.push_back(fuzz_tensval);
      /* std::cout << "Argument " << i << ": " << fuzz_tensval.tensor->DebugString() << "\n"; */
    }

    tensorflow::gtl::InlinedVector<tensorflow::TensorValue, 4> *fuzz_inputs = new
      tensorflow::gtl::InlinedVector<tensorflow::TensorValue, 4>(fuzz_vec.begin(), fuzz_vec.end());
    last_fuzz_inputs = fuzz_inputs;
    fuzz_ctx_params->inputs = fuzz_inputs;
    fuzz_ctx = new tensorflow::OpKernelContext(fuzz_ctx_params);

    return fuzz_ctx;

  }

  /* double Fuzzer::get_tensor_contents() { */
  /*     return tensor_contents.at(indices[cur_idx - 1]); */
  /* } */

}
