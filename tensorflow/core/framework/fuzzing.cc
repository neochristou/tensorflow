
#include "tensorflow/core/framework/fuzzing.h"

namespace tffuzzing {

  bool already_fuzzing = false;
  char* results_dir = "/media/tf-fuzzing/results";

  static std::fstream mutations_file;
  static std::fstream mutations_restore;
  static std::fstream crashes_file;
  static std::fstream num_crashes_file;
  static std::fstream unknown_type_file;
  static std::fstream time_file;
  /* static std::fstream start_file; */

  static uint64_t start_time;
  static uint64_t end_time;

  void create_file(const char *filename, std::fstream &file, std::ios_base::openmode fflags)
  {
      std::ofstream file_stream(filename);
      file.clear();
      file.open(filename, fflags);
      if (file.fail()) {
        std::cout << "Failed to open " << filename << std::endl;
        std::cout << "Error: " << strerror(errno) << std::endl;
      }
  }

  bool was_fuzzed(std::string fname) {
    // printf("Fuzzed %s\n", fname.c_str());
    struct stat stat_buffer;
    char stat_filename[FILENAME_SZ] = {};
    char unknown_filename[FILENAME_SZ] = {};
    int done_status;
    int unknown_status;

    snprintf(stat_filename, FILENAME_SZ, "%s/%s_mutations.done", results_dir, fname.c_str());
    snprintf(unknown_filename, FILENAME_SZ, "%s/%s.unknown", results_dir, fname.c_str());

    // Also return true if it aborted because of an unknown type
    done_status = stat(stat_filename, &stat_buffer) == 0;
    unknown_status = stat(unknown_filename, &stat_buffer) == 0;

    return done_status | unknown_status;
  }

  Fuzzer::Fuzzer(char *fname, tensorflow::OpKernelContext* ctx)
  {

      /* std::cout << "Initializing fuzzer..." << std::endl; */

      cur_fname = fname;

      num_args = ctx->num_inputs();
      /* std::cout << "Copying original inputs" << std::endl; */

      original_ctx = new tensorflow::OpKernelContext(ctx->get_params());

      /* printf("Original num args: %d\n", original_ctx->num_inputs()); */
      /* printf("Original arguments: \n"); */
      /* for (int i = 0; i < num_args; i++) { */
      /*   std::cout << "Argument " << i << ": " << original_ctx->input(i).DebugString() << "\n"; */
      /* } */

      bool restore = false;
      long long last_mutation = -1;
      struct stat stat_buffer;

      glob_t glob_result = {0};
      int glob_ret;
      pid_t mypid;
      char *existing_pid;

      /* std::cout << "Initializing filename buffers..." << std::endl; */

      char mutfile_pattern[FILENAME_SZ] = {};
      char mutfile_prefix[FILENAME_SZ] = {};
      char proc_filename[FILENAME_SZ] = {};
      char mut_filename[FILENAME_SZ] = {};
      char time_filename[FILENAME_SZ] = {};
      /* char start_filename[FILENAME_SZ] = {}; */

      char total_filename[FILENAME_SZ] = {};
      std::fstream total_file;

      /* std::cout << "Filename buffers initialized"  << std::endl; */

      tensorflow::Tensor tensor;
      tensorflow::TensorShape tensor_shape;

      mypid = ::getpid();

      /* std::cout << "Writing to filename buffers" << std::endl; */

      snprintf(mutfile_pattern, FILENAME_SZ, "%s/%s_mutations.log.*", results_dir, fname);
      snprintf(mutfile_prefix, FILENAME_SZ, "%s/%s_mutations.log", results_dir, fname);
      snprintf(mut_filename, FILENAME_SZ, "%s/%s_mutations.log.%d", results_dir, fname, mypid);
      snprintf(time_filename, FILENAME_SZ, "%s/%s.time", results_dir, fname);
      /* snprintf(start_filename, FILENAME_SZ, "%s/%s.start.%d", results_dir, fname, mypid); */
      snprintf(total_filename, FILENAME_SZ, "%s/totals.txt", results_dir);

      std::ios_base::openmode fflags = std::ios::out | std::ios::in;

      // Create time file if it doesn't exist
      if (stat(time_filename, &stat_buffer) != 0){
        fflags |= std::ios::trunc;
      }

      create_file(time_file, time_filename, fflags);

      fflags |= std::ios::trunc;

      mutations_logger_filename = mut_filename;

      /* std::cout << "Mutation filename written" << std::endl; */

      for (int r = 0; r < MUTFILE_TRIES; r++){
        glob_ret = glob(mutfile_pattern, 0, NULL, &glob_result);
        if (glob_ret != GLOB_NOMATCH && !restore) {

          // A lot of empty mutation files, probably deadlock or bug, stop
          // fuzzing this kernel
          if (glob_result.gl_pathc > 5) {
            mark_fuzzing_done();
            printf("%s has a lot of empty mutation files, skip\n", fname);
            return;
          }

          // A mutation file for the same function exists
          /* std::cout << "Found mutation file for " << fname << std::endl << std::flush; */
          for(size_t i = 0; i < glob_result.gl_pathc && !restore; ++i) {

            existing_pid = glob_result.gl_pathv[i] + strlen(mutfile_prefix) + 1;
            snprintf(proc_filename, FILENAME_SZ, "/proc/%s", existing_pid);

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

              // Open the file here such that other threads that are also
              // looking to fuzz this function right now don't
              /* mutations_file.open(mutations_logger_filename, fflags); */

              restore = true;
            }
          }
        }
        /* else { */
        /* std::cout << "No mutation file found for " << fname << std::endl << std::flush; */
        /* } */
        globfree(&glob_result);
      }

      printf("Fuzzing function %s\n", fname);

      // Disable buffering else program might crash before writing to logger
      /* if (!restore) */
      // Force creation of the file immediately
      create_file(log_file, mutations_logger_filename, fflags);
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

      // Log total number of mutations for function
      total_file.clear();
      total_file.open(total_filename, std::ios::app);
      if (total_file.fail()) {
        std::cout << "Failed to open " << total_filename << std::endl;
        std::cout << "Error: " << strerror(errno) << std::endl;
      }
      total_file << cur_fname << ":" << all_mutations << std::endl << std::flush;
      total_file.close();

      bool got_last = false;
      int tries = 0;
      if (restore) {

        mutations_restore.open(mutations_restore_filename, std::ios::out | std::ios::in);
        std::string last_line;
        while (!got_last && tries < 10) {
          getline(mutations_restore, last_line);
          if (last_line.length() > 0) {
            char *line_end;
            last_mutation = std::strtoll(last_line.c_str(), &line_end, 10);
            got_last = true;
          } else {
            printf("Error: reading %s (got %s)...\n", mutations_restore_filename.c_str(), last_line.c_str());
            tries++;
          }
        }
        // Mutation file is empty, abort
        if (!last_line.length() > 0) {
          abort();
        }
        /* mutations_restore.close(); */

        if (last_mutation > 0) {
          restore_last_mutation(last_mutation, fname);
          // Delete the file since we already logged the crash
          if (std::remove(mutations_restore_filename.c_str()) != 0) {
            /* std::cout << "Couldn't remove " << mutations_restore_filename << std::flush; */
          }
        }
      } else {
        indices[0] = -1;
      }

    }

  Fuzzer::~Fuzzer() {

    /* mutations_file.close(); */

  }

  tensorflow::TensorValue Fuzzer::get_next_mut(tensorflow::DataType ttype, int idx) {

    /* std::cout << "get_next_mut()" << std::endl; */

    tensorflow::Tensor *tensor;

    switch (ttype) {
      default:
        mark_unknown_type(ttype);
      case tensorflow::DataType::DT_QINT8:
        return qint8_tensor_mutations.at(indices[cur_idx++]);
      case tensorflow::DataType::DT_QINT16:
        return qint16_tensor_mutations.at(indices[cur_idx++]);
      case tensorflow::DataType::DT_QINT32:
        return qint32_tensor_mutations.at(indices[cur_idx++]);
      case tensorflow::DataType::DT_QUINT8:
        return quint8_tensor_mutations.at(indices[cur_idx++]);
      case tensorflow::DataType::DT_QUINT16:
        return quint16_tensor_mutations.at(indices[cur_idx++]);
      case tensorflow::DataType::DT_INT8:
        return int8_tensor_mutations.at(indices[cur_idx++]);
      case tensorflow::DataType::DT_INT16:
        return int16_tensor_mutations.at(indices[cur_idx++]);
      case tensorflow::DataType::DT_INT32:
        return int32_tensor_mutations.at(indices[cur_idx++]);
      case tensorflow::DataType::DT_INT64:
        return int64_tensor_mutations.at(indices[cur_idx++]);
      case tensorflow::DataType::DT_UINT8:
        return uint8_tensor_mutations.at(indices[cur_idx++]);
      case tensorflow::DataType::DT_UINT16:
        return uint16_tensor_mutations.at(indices[cur_idx++]);
      case tensorflow::DataType::DT_UINT32:
        return uint32_tensor_mutations.at(indices[cur_idx++]);
      case tensorflow::DataType::DT_UINT64:
        return uint64_tensor_mutations.at(indices[cur_idx++]);
      case tensorflow::DataType::DT_FLOAT:
        return float_tensor_mutations.at(indices[cur_idx++]);
      case tensorflow::DataType::DT_HALF:
        return half_tensor_mutations.at(indices[cur_idx++]);
      case tensorflow::DataType::DT_DOUBLE:
        return double_tensor_mutations.at(indices[cur_idx++]);
      case tensorflow::DataType::DT_BOOL:
        return bool_tensor_mutations.at(indices[cur_idx++]);
      case tensorflow::DataType::DT_STRING:
        return string_tensor_mutations.at(indices[cur_idx++]);

        //  No mutations for these so just return the original tensor
      case tensorflow::DataType::DT_VARIANT:
      {
        /* std::cout << "Creating DT_VARIANT tensor\n" << std::flush; */
        tensorflow::Tensor orig = original_ctx->input(idx);
        tensor = new tensorflow::Tensor();
        tensor->flat<tensorflow::Variant>() = orig.flat<tensorflow::Variant>();
        return tensorflow::TensorValue(tensor);
      }

      case tensorflow::DataType::DT_COMPLEX64:
      case tensorflow::DataType::DT_COMPLEX128:
      case tensorflow::DataType::DT_RESOURCE:
      {
        tensor = new tensorflow::Tensor(original_ctx->input(idx));
        return tensorflow::TensorValue(tensor);
      }
    }
  }

  void Fuzzer::log_current_mutatoin(std::fstream &file)
  {
    for (int idx = 0; idx < num_args; idx++) {
      ttype = tensor_types.at(idx);
      tensor_val = get_next_mut(ttype, idx);
      ttype = tensor_val.tensor->dtype();
      switch (ttype) {
        default:
          file << tensor_val.tensor->DebugString() << "\n";
        /* case tensorflow::DataType::DT_VARIANT: */
        /* file << "Variant" << std::endl << std::flush; */
        case tensorflow::DataType::DT_RESOURCE:
         file << "Resource" << std::endl << std::flush;
      }
    }

   file << "\n--------------------------------------\n";
  }

  void Fuzzer::restore_last_mutation(long long last_mutation, char *fname)
  {

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

    char crashes_filename[FILENAME_SZ] = {};
    char crashes_num_filename[FILENAME_SZ] = {};
    char logbuf[LOGBUFSZ] = {};
    long last_crash; // Used to bound number of crashes
    struct stat stat_buffer;
    std::ios_base::openmode fflags = std::ios::out | std::ios::in;

    snprintf(crashes_filename, FILENAME_SZ, "%s/%s_crashes.log", results_dir, fname);
    crashes_logger_filename = crashes_filename;
    crashes_file.rdbuf()->pubsetbuf(0, 0);
    crashes_file.open(crashes_logger_filename, std::ios::out | std::ios::app);

    snprintf(crashes_num_filename, FILENAME_SZ, "%s/%s_crashes_num.log", results_dir, fname);

    if (stat(crashes_num_filename, &stat_buffer) == 0){
      num_crashes_file.open(crashes_num_filename, fflags);
      std::string last_line;
      getline(num_crashes_file, last_line);
      if (last_line.length() > 0) {
        char *line_end;
        last_crash = std::strtoll(last_line.c_str(), &line_end, 10);
      } else {
        /* std::cout << "Error while reading file with number of crashes..." << std::flush; */
      }
    } else {
      last_crash = 0;
      fflags |= std::ios::trunc;
      create_file(num_crashes_file, crashes_num_filename, fflags);
    }
    last_crash++;

    snprintf(logbuf, LOGBUFSZ, "%ld\n", last_crash);

    num_crashes_file.seekp(0, std::ios::beg);
    num_crashes_file.write(logbuf, LOGBUFSZ);
    num_crashes_file.flush();
    /* num_crashes_file.close(); */

    while (total_mutations != last_mutation) {
      next_mutations_indices(false);
    }

    /* next_mutations_indices(true); */

    log_current_mutation(crashes_file);
    /* crashes_file.close(); */

    if (last_crash >= CRASHES_BOUND) {
      printf("Function %s crashed %d times, skipping rest of fuzzing\n", fname, CRASHES_BOUND);
      std::fstream run_file;
      char run_filename[FILENAME_SZ];
      snprintf(run_filename, FILENAME_SZ, "%s/%s.run", results_dir, fname);
      std::ios_base::openmode fflags = std::ios::out | std::ios::in | std::ios::trunc;
      create_file(run_filename, run_file, fflags);
      run_file << total_mutations << std::flush;
      run_file.close();
      mark_fuzzing_done();
      return;
    }

    next_mutations_indices(true);
    printf("Mutations left after restoration: %llu\n", total_mutations);
  }

  void Fuzzer::calculate_total_mutations() {

    /* printf("calculate_total_mutations()\n"); */

    long long nmut_fuzz;

    for (auto &ttype : tensor_types) {
      switch (ttype) {
        default:
          mark_unknown_type(ttype);
        case tensorflow::DataType::DT_QINT8:
          total_mutations *= qint8_tensor_mutations.size();
          pool_sizes.push_back(qint8_tensor_mutations.size());
          break;
        case tensorflow::DataType::DT_QINT16:
          total_mutations *= qint16_tensor_mutations.size();
          pool_sizes.push_back(qint16_tensor_mutations.size());
          break;
        case tensorflow::DataType::DT_QINT32:
          total_mutations *= qint32_tensor_mutations.size();
          pool_sizes.push_back(qint32_tensor_mutations.size());
          break;
        case tensorflow::DataType::DT_QUINT8:
          total_mutations *= quint8_tensor_mutations.size();
          pool_sizes.push_back(quint8_tensor_mutations.size());
          break;
        case tensorflow::DataType::DT_QUINT16:
          total_mutations *= quint16_tensor_mutations.size();
          pool_sizes.push_back(quint16_tensor_mutations.size());
          break;
        case tensorflow::DataType::DT_INT8:
          total_mutations *= int8_tensor_mutations.size();
          pool_sizes.push_back(int8_tensor_mutations.size());
          break;
        case tensorflow::DataType::DT_INT16:
          total_mutations *= int16_tensor_mutations.size();
          pool_sizes.push_back(int16_tensor_mutations.size());
          break;
        case tensorflow::DataType::DT_INT32:
          total_mutations *= int32_tensor_mutations.size();
          pool_sizes.push_back(int32_tensor_mutations.size());
          break;
        case tensorflow::DataType::DT_INT64:
          total_mutations *= int64_tensor_mutations.size();
          pool_sizes.push_back(int64_tensor_mutations.size());
          break;
        case tensorflow::DataType::DT_UINT8:
          total_mutations *= uint8_tensor_mutations.size();
          pool_sizes.push_back(uint8_tensor_mutations.size());
          break;
        case tensorflow::DataType::DT_UINT16:
          total_mutations *= uint16_tensor_mutations.size();
          pool_sizes.push_back(uint16_tensor_mutations.size());
          break;
        case tensorflow::DataType::DT_UINT32:
          total_mutations *= uint32_tensor_mutations.size();
          pool_sizes.push_back(uint32_tensor_mutations.size());
          break;
        case tensorflow::DataType::DT_UINT64:
          total_mutations *= uint64_tensor_mutations.size();
          pool_sizes.push_back(uint64_tensor_mutations.size());
          break;
        case tensorflow::DataType::DT_HALF:
          total_mutations *= half_tensor_mutations.size();
          pool_sizes.push_back(half_tensor_mutations.size());
          break;
        case tensorflow::DataType::DT_FLOAT:
          total_mutations *= float_tensor_mutations.size();
          pool_sizes.push_back(float_tensor_mutations.size());
          break;
        case tensorflow::DataType::DT_DOUBLE:
          total_mutations *= double_tensor_mutations.size();
          pool_sizes.push_back(double_tensor_mutations.size());
          break;
        case tensorflow::DataType::DT_BOOL:
          total_mutations *= bool_tensor_mutations.size();
          pool_sizes.push_back(bool_tensor_mutations.size());
          break;
        case tensorflow::DataType::DT_STRING:
          total_mutations *= string_tensor_mutations.size();
          pool_sizes.push_back(string_tensor_mutations.size());
          break;
        // Just the original
        case tensorflow::DataType::DT_VARIANT:
        case tensorflow::DataType::DT_COMPLEX64:
        case tensorflow::DataType::DT_COMPLEX128:
        case tensorflow::DataType::DT_RESOURCE:
          pool_sizes.push_back(1);
          break;
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
    printf("Will run with (at least): %llu mutations\n", nmut_fuzz);
    printf("Step size: %lu\n", num_mut_skip);

  }

  template <class T>
    tensorflow::TensorValue *Fuzzer::get_constant_tensor(T value)
    {
      tensorflow::Tensor *tensor;
      tensorflow::TensorValue *tensor_val;

      tensor = new tensorflow::Tensor(value);
      tensor_val = new tensorflow::TensorValue(tensor);
      return tensor_val;

    }

    tensorflow::TensorValue *Fuzzer::get_empty_tensor_dims(tensorflow::DataType ttype,
                                                          tensorflow::TensorShape dims)
    {

      tensorflow::Tensor *tensor;
      tensorflow::TensorValue *tensor_val;

      tensor = new tensorflow::Tensor(ttype, dims);
      tensor_val = new tensorflow::TensorValue(tensor);

      return tensor_val;

    }

  template <class T>
    tensorflow::TensorValue *Fuzzer::get_flat_tensor(T value, tensorflow::Tensor *tensor)
    {

      tensorflow::TensorValue *tensor_val;

      tensor->flat<T>().setConstant(value);
      tensor_val = new tensorflow::TensorValue(tensor);
      return tensor_val;

    }


  template <class T>
    tensorflow::TensorValue *Fuzzer::get_flat_tensor_dims(T value, tensorflow::DataType ttype,
                                                          tensorflow::TensorShape dims)
    {

      tensorflow::Tensor *tensor;
      tensorflow::TensorValue *tensor_val;

      tensor = new tensorflow::Tensor(ttype, dims);
      tensor->flat<T>().setConstant(value);
      tensor_val = new tensorflow::TensorValue(tensor);

      return tensor_val;

    }

  void Fuzzer::initialize_tensor_pools(){

    /* std::cout << "Initializing pools" << std::endl; */

    tensorflow::Tensor *tensor;
    tensorflow::TensorValue *tensor_val;
    tensorflow::DataType tensor_type;
    tensorflow::TensorShape dims;
    std::vector<int64_t> fuzz_dims_vec = {};
    int64_t rand_dim, rand_size;
    int idx;
    tensorflow::int32 rand_int32;
    tensorflow::int64 rand_int64;
    tensorflow::uint32 rand_uint32;
    tensorflow::uint64 rand_uint64;
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
        default:
          mark_unknown_type(tensor_type);
        case tensorflow::DataType::DT_QINT8:
          qint8_tensor_mutations.push_back(*tensor_val);
          break;
        case tensorflow::DataType::DT_QINT16:
          qint16_tensor_mutations.push_back(*tensor_val);
          break;
        case tensorflow::DataType::DT_QINT32:
          qint32_tensor_mutations.push_back(*tensor_val);
          break;
        case tensorflow::DataType::DT_QUINT8:
          quint8_tensor_mutations.push_back(*tensor_val);
          break;
        case tensorflow::DataType::DT_QUINT16:
          quint16_tensor_mutations.push_back(*tensor_val);
          break;
        case tensorflow::DataType::DT_INT8:
          int8_tensor_mutations.push_back(*tensor_val);
          break;
        case tensorflow::DataType::DT_INT16:
          int16_tensor_mutations.push_back(*tensor_val);
          break;
        case tensorflow::DataType::DT_INT32:
          int32_tensor_mutations.push_back(*tensor_val);
          break;
        case tensorflow::DataType::DT_INT64:
          int64_tensor_mutations.push_back(*tensor_val);
          break;
        case tensorflow::DataType::DT_UINT8:
          uint8_tensor_mutations.push_back(*tensor_val);
          break;
        case tensorflow::DataType::DT_UINT16:
          uint16_tensor_mutations.push_back(*tensor_val);
          break;
        case tensorflow::DataType::DT_UINT32:
          uint32_tensor_mutations.push_back(*tensor_val);
          break;
        case tensorflow::DataType::DT_UINT64:
          uint64_tensor_mutations.push_back(*tensor_val);
          break;
        case tensorflow::DataType::DT_HALF:
          half_tensor_mutations.push_back(*tensor_val);
          break;
        case tensorflow::DataType::DT_FLOAT:
          float_tensor_mutations.push_back(*tensor_val);
          break;
        case tensorflow::DataType::DT_DOUBLE:
          double_tensor_mutations.push_back(*tensor_val);
          break;
        case tensorflow::DataType::DT_STRING:
          string_tensor_mutations.push_back(*tensor_val);
          break;
        case tensorflow::DataType::DT_BOOL: // Will just create both later
          // We don't create mutations for these
        case tensorflow::DataType::DT_VARIANT:
        case tensorflow::DataType::DT_COMPLEX64:
        case tensorflow::DataType::DT_COMPLEX128:
        case tensorflow::DataType::DT_RESOURCE:
          break;
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
        default:
          mark_unknown_type(tensor_type);
        case tensorflow::DataType::DT_INT8:
          tensor = new tensorflow::Tensor(tensor_type, tshape);
          tensor_val = get_flat_tensor<tensorflow::int8>(0, tensor);
          int8_tensor_mutations.push_back(*tensor_val);
          break;
        case tensorflow::DataType::DT_INT32:
          rand_int32 = int_mutations.at(int_distr(rngenerator));
          tensor_val = get_flat_tensor<tensorflow::int32>(rand_int32, tensor);
          int32_tensor_mutations.push_back(*tensor_val);

          tensor = new tensorflow::Tensor(tensor_type, tshape);
          tensor_val = get_flat_tensor<tensorflow::int32>(0, tensor);
          int32_tensor_mutations.push_back(*tensor_val);
          break;
        case tensorflow::DataType::DT_INT64:
          rand_int64 = long_mutations.at(long_distr(rngenerator));
          tensor_val = get_flat_tensor<tensorflow::int64>(rand_int64, tensor);
          int64_tensor_mutations.push_back(*tensor_val);

          tensor = new tensorflow::Tensor(tensor_type, tshape);
          tensor_val = get_flat_tensor<tensorflow::int64>(0, tensor);
          int64_tensor_mutations.push_back(*tensor_val);
          break;
        case tensorflow::DataType::DT_UINT8:
          tensor = new tensorflow::Tensor(tensor_type, tshape);
          tensor_val = get_flat_tensor<tensorflow::uint8>(0, tensor);
          uint8_tensor_mutations.push_back(*tensor_val);
          break;
        case tensorflow::DataType::DT_UINT32:
          rand_uint32 = (tensorflow::uint32) int_mutations.at(int_distr(rngenerator));
          tensor_val = get_flat_tensor<tensorflow::uint32>(rand_uint32, tensor);
          uint32_tensor_mutations.push_back(*tensor_val);

          tensor = new tensorflow::Tensor(tensor_type, tshape);
          tensor_val = get_flat_tensor<tensorflow::uint32>(0, tensor);
          uint32_tensor_mutations.push_back(*tensor_val);
          break;
        case tensorflow::DataType::DT_UINT64:
          rand_uint64 = (tensorflow::uint64) long_mutations.at(long_distr(rngenerator));
          tensor_val = get_flat_tensor<tensorflow::uint64>(rand_int64, tensor);
          uint64_tensor_mutations.push_back(*tensor_val);

          tensor = new tensorflow::Tensor(tensor_type, tshape);
          tensor_val = get_flat_tensor<tensorflow::uint64>(0, tensor);
          uint64_tensor_mutations.push_back(*tensor_val);
          break;
        case tensorflow::DataType::DT_HALF:
          rand_half = Eigen::half(half_mutations.at(half_distr(rngenerator)));
          tensor_val = get_flat_tensor<Eigen::half>(rand_half, tensor);
          half_tensor_mutations.push_back(*tensor_val);

          tensor = new tensorflow::Tensor(tensor_type, tshape);
          tensor_val = get_flat_tensor<Eigen::half>(Eigen::half(0.0), tensor);
          half_tensor_mutations.push_back(*tensor_val);
          break;
        case tensorflow::DataType::DT_FLOAT:
          rand_float = float_mutations.at(float_distr(rngenerator));
          tensor_val = get_flat_tensor<float>(rand_float, tensor);
          float_tensor_mutations.push_back(*tensor_val);

          tensor = new tensorflow::Tensor(tensor_type, tshape);
          tensor_val = get_flat_tensor<float>(0, tensor);
          float_tensor_mutations.push_back(*tensor_val);
          break;
        case tensorflow::DataType::DT_DOUBLE:
          rand_double = double_mutations.at(double_distr(rngenerator));
          tensor_val = get_flat_tensor<double>(rand_double, tensor);
          double_tensor_mutations.push_back(*tensor_val);

          tensor = new tensorflow::Tensor(tensor_type, tshape);
          tensor_val = get_flat_tensor<double>(0, tensor);
          double_tensor_mutations.push_back(*tensor_val);
          break;
        case tensorflow::DataType::DT_BOOL: // Will just create both later
          // Don't create other mutations for these
        case tensorflow::DataType::DT_VARIANT:
        case tensorflow::DataType::DT_STRING:
        case tensorflow::DataType::DT_COMPLEX64:
        case tensorflow::DataType::DT_COMPLEX128:
        case tensorflow::DataType::DT_RESOURCE:
        case tensorflow::DataType::DT_QINT8:
        case tensorflow::DataType::DT_QINT16:
        case tensorflow::DataType::DT_QINT32:
        case tensorflow::DataType::DT_QUINT8:
        case tensorflow::DataType::DT_QUINT16:
        case tensorflow::DataType::DT_INT16:
        case tensorflow::DataType::DT_UINT16:
          break;
      }

      /* std::cout  << tensor_val->tensor->DebugString() << std::endl; */
    }

    /* std::cout << "Creating mutations single value\n" << std::flush; */
    // Create tensors with single value and no value
    dims = tensorflow::TensorShape();
    dims.AddDim(0);
    for (auto &fuzzval : int_mutations) {
      tensor_val = get_constant_tensor(fuzzval);
      int32_tensor_mutations.push_back(*tensor_val);

      tensor_val = get_empty_tensor_dims(tensorflow::DataType::DT_INT32, dims);
      int32_tensor_mutations.push_back(*tensor_val);
    }
    for (auto &fuzzval : long_mutations) {
      tensor_val = get_constant_tensor(fuzzval);
      int64_tensor_mutations.push_back(*tensor_val);

      tensor_val = get_empty_tensor_dims(tensorflow::DataType::DT_INT64, dims);
      int64_tensor_mutations.push_back(*tensor_val);
    }
    for (auto &fuzzval : half_mutations) {
      tensor_val = get_constant_tensor(fuzzval);
      half_tensor_mutations.push_back(*tensor_val);

      tensor_val = get_empty_tensor_dims(tensorflow::DataType::DT_HALF, dims);
      half_tensor_mutations.push_back(*tensor_val);
    }
    for (auto &fuzzval : float_mutations) {
      tensor_val = get_constant_tensor(fuzzval);
      float_tensor_mutations.push_back(*tensor_val);

      tensor_val = get_empty_tensor_dims(tensorflow::DataType::DT_FLOAT, dims);
      float_tensor_mutations.push_back(*tensor_val);
    }
    for (auto &fuzzval : double_mutations) {
      tensor_val = get_constant_tensor(fuzzval);
      double_tensor_mutations.push_back(*tensor_val);

      tensor_val = get_empty_tensor_dims(tensorflow::DataType::DT_DOUBLE, dims);
      double_tensor_mutations.push_back(*tensor_val);
    }
    for (auto &fuzzval : string_mutations) {
      tensor_val = get_constant_tensor(fuzzval);
      string_tensor_mutations.push_back(*tensor_val);

      tensor_val = get_empty_tensor_dims(tensorflow::DataType::DT_STRING, dims);
      string_tensor_mutations.push_back(*tensor_val);
    }
    tensor_val = get_constant_tensor(true);
    bool_tensor_mutations.push_back(*tensor_val);
    tensor_val = get_constant_tensor(false);
    bool_tensor_mutations.push_back(*tensor_val);

    // Create tensors with increasing number of dimensions, random values
    for (int cur_ndims = 1; cur_ndims < TENSOR_NUM_DIMS_FUZZ; cur_ndims++) {
      dims = tensorflow::TensorShape();
      for (int i = 0; i < cur_ndims; i++) {
        rand_dim = dims_distr(rngenerator);
        dims.AddDim(rand_dim);
      }

      rand_int32 = int_mutations.at(int_distr(rngenerator));
      tensor_val = get_flat_tensor_dims(rand_int32, tensorflow::DataType::DT_INT32, dims);
      int32_tensor_mutations.push_back(*tensor_val);

      rand_int64 = long_mutations.at(long_distr(rngenerator));
      tensor_val = get_flat_tensor_dims(rand_int64, tensorflow::DataType::DT_INT64, dims);
      int64_tensor_mutations.push_back(*tensor_val);

      rand_uint32 = (tensorflow::uint32) int_mutations.at(int_distr(rngenerator));
      tensor_val = get_flat_tensor_dims(rand_uint32, tensorflow::DataType::DT_UINT32, dims);
      uint32_tensor_mutations.push_back(*tensor_val);

      rand_uint64 = (tensorflow::uint64) long_mutations.at(long_distr(rngenerator));
      tensor_val = get_flat_tensor_dims(rand_uint64, tensorflow::DataType::DT_UINT64, dims);
      uint64_tensor_mutations.push_back(*tensor_val);

      rand_float = float_mutations.at(float_distr(rngenerator));
      tensor_val = get_flat_tensor_dims(rand_float, tensorflow::DataType::DT_FLOAT, dims);
      float_tensor_mutations.push_back(*tensor_val);

      rand_half = Eigen::half(half_mutations.at(half_distr(rngenerator)));
      tensor_val = get_flat_tensor_dims(rand_half, tensorflow::DataType::DT_HALF, dims);
      half_tensor_mutations.push_back(*tensor_val);

      rand_double = double_mutations.at(double_distr(rngenerator));
      tensor_val = get_flat_tensor_dims(rand_double, tensorflow::DataType::DT_DOUBLE, dims);
      double_tensor_mutations.push_back(*tensor_val);
    }

  }

  void Fuzzer::mark_unknown_type(tensorflow::DataType ttype)
  {
    char filename[FILENAME_SZ] = {};

    std::cout << "\033[1;31mUnknown type:\033[0m " << ttype << std::endl << std::flush;

    // Indicates a type that isn't handled in the fuzzer
    snprintf(filename, FILENAME_SZ, "%s/%s.unknown", results_dir, cur_fname.c_str());

    std::ios_base::openmode fflags = std::ios::out | std::ios::in;
    unknown_type_file.open(filename, fflags);
    unknown_type_file << ttype << std::flush;
    unknown_type_file.close();

    abort();
  }

  void Fuzzer::mark_fuzzing_done()
  {

    /* std::cout << "mark_fuzzing_done()" << std::endl; */

    char filename[FILENAME_SZ] = {};

    // This file indicates to the fuzzer that this kernel has been already fuzzed
    snprintf(filename, FILENAME_SZ, "%s/%s_mutations.done", results_dir, cur_fname.c_str());

    std::ofstream output(filename);

    // Set mutations to zero to stop fuzzing
    total_mutations = 0;
  }


  bool Fuzzer::has_more_mutations(bool reset)
  {

    // Another thread/proc is fuzzing this right now,
    // return false such that the current thread doesn't
    // also try to fuzz
    if (is_running)
      return false;

    if (reset) {
      cur_idx = 0;
      next_mutations_indices(true);
    }

    bool has_more = total_mutations > 0;

    return has_more;
  }

  // Skips ahead num_mut_skip mutations to bound the total mutations
  void Fuzzer::next_mutations_indices(bool log){

    total_mutations -= num_mut_skip;

    if (total_mutations <= 0) {
      mark_fuzzing_done();
      remove(mutations_logger_filename.c_str());
      return;
    }

    long long passed = all_mutations - total_mutations;
    for (int i = 0; i < num_args; i++) {
      indices[i] = passed % pool_sizes[i];
      passed = passed / pool_sizes[i];
    }

    if (log) {
      char logbuf[LOGBUFSZ] = {};
      snprintf(logbuf, LOGBUFSZ, "%llu", total_mutations);
      mutations_file.seekp(0, std::ios::beg);
      mutations_file.write(logbuf, LOGBUFSZ);
      mutations_file.flush();
    }

    /* std::cout << "next_mutations_indices end\n" << std::flush; */
  }


  tensorflow::OpKernelContext *Fuzzer::get_fuzzed_context() {

    /* std::cout << "get_fuzzed_context()\n" << std::flush; */

    tensorflow::DataType ttype;
    tensorflow::OpKernelContext::Params *fuzz_ctx_params = original_ctx->get_params();
    std::vector<tensorflow::TensorValue> fuzz_vec;
    tensorflow::TensorValue fuzz_tensval;
    tensorflow::Tensor tensor;

    /* printf("Num args after get_params: %d\n", original_ctx->num_inputs()); */
    /* printf("Current num arguments: %d\n", original_ctx->num_inputs()); */
    /* printf("Current arguments: \n"); */
    /* for (int i = 0; i < num_args; i++) { */
    /*   std::cout << "Argument " << i << ": " << original_ctx->input(i).DebugString() << "\n"; */
    /* } */

    for (int idx = 0; idx < num_args; idx++) {
      ttype = tensor_types.at(idx);
      fuzz_tensval = get_next_mut(ttype, idx);
      fuzz_vec.push_back(fuzz_tensval);
    }

    tensorflow::gtl::InlinedVector<tensorflow::TensorValue, 4> *fuzz_inputs = new
      tensorflow::gtl::InlinedVector<tensorflow::TensorValue, 4>(fuzz_vec.begin(), fuzz_vec.end());
    /* last_fuzz_inputs = fuzz_inputs; */
    fuzz_ctx_params->inputs = fuzz_inputs;
    fuzz_ctx = new tensorflow::OpKernelContext(fuzz_ctx_params);

    return fuzz_ctx;

  }

  void Fuzzer::mut_start_time()
  {
    struct timespec ts;
    struct timespec ts_real;
    uint64_t real_time;
    char logbuf[BUFSZ] = {};

    clock_gettime(CLOCK_MONOTONIC, &ts);
    start_time = ((uint64_t)ts.tv_sec) * NS_PER_SEC + ts.tv_nsec;

    /* clock_gettime(CLOCK_REALTIME, &ts_real); */
    /* real_time = ((uint64_t)ts_real.tv_sec) * 1000 * 1000 * 1000 + ts_real.tv_nsec; */
    /* snprintf(logbuf, BUFSZ, "%llu:%lu", total_mutations, real_time); */
    /* start_file.seekp(0, std::ios::beg); */
    /* start_file.write(logbuf, BUFSZ); */
    /* start_file.flush(); */
    /* start_file.close(); */
  }

  void Fuzzer::mut_end_time()
  {

    struct timespec ts;
    struct stat stat_buffer;
    char duration_filename[FILENAME_SZ] = {};
    std::ios_base::openmode fflags = std::ios::out | std::ios::in;
    std::fstream duration_file;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    end_time = ((uint64_t)ts.tv_sec) * NS_PER_SEC + ts.tv_nsec;

    uint64_t duration = end_time - start_time;
    uint64_t duration_secs = duration / (NS_PER_SEC);
    time_file << total_mutations << ":" << duration << std::endl << std::flush;

    // Log mutations that took more than THRESH seconds to finish
    if (duration_secs > TIME_THRESH_SECS) {
      /* We want to log the mutation that just run, so this will achieve it:
       * 1. Move to the mutation BEFORE the mutation that just run
       * 2. Call next_mutations_indices to set up the indices array correctly
       * for the mutation after that, which is the mutation that just run
       * 3. Call log_current_mutation to log it
       * 4. When the fuzzed function calls has_more_mutations,
       * next_mutations_indices will be called again and will move to the next
       * mutation
       */
      total_mutations += (num_mut_skip * 2);
      next_mutations_indices(false);

      snprintf(duration_filename, sizeof(duration_filename), "%s/%s.duration", results_dir, cur_fname);
      if (stat(filename, &stat_buffer) != 0) {
        fflags |= std::ios::trunc;
        create_file(duration_filename, duration_file, fflags);
      } else {
        duration_file.open(duration_filename, std::ios::app);
        if (duration_file.fail()) {
          std::cout << "Failed to open " << duration_filename << std::endl;
          std::cout << "Error: " << strerror(errno) << std::endl;
        }
      }

      duration_file << "Duration (secs): " << duration_secs << std::endl;
      log_current_mutation(duration_file);
      duration_file << std::flush;
      duration_file.close();
    }
  }

}
