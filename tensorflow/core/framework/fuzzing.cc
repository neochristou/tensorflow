
#include "tensorflow/core/framework/fuzzing.h"

namespace tffuzzing {

  bool already_fuzzing = false;
  const char *results_dir = "/media/tf-fuzzing/results";
  std::string attrs;
  std::string op_name;

  static std::fstream mutations_file;
  static std::fstream mutations_restore;
  static std::fstream crashes_file;
  static std::fstream num_crashes_file;
  static std::fstream unknown_type_file;
  static std::fstream time_file;
  static std::fstream except_file;

  static uint64_t start_time;
  static uint64_t end_time;

  void create_file(const std::string& filename, std::fstream &file, std::ios_base::openmode fflags)
  {
    std::ofstream file_stream(filename);
    if (file.is_open()) {
      file.close();
    }
    file.clear();
    file.open(filename, fflags);
    if (file.fail()) {
      std::cout << "Failed to open " << filename << std::endl;
      std::cout << "Error: " << strerror(errno) << std::endl;
    }
  }

  bool was_fuzzed(const std::string& fname) {
    struct stat stat_buffer = {};
    std::string stat_filename;
    std::string unknown_filename;
    int done_status = 0;
    int unknown_status = 0;

    stat_filename = std::string(results_dir) + "/" + fname + ".done";
    unknown_filename = std::string(results_dir) + "/" + fname + ".unknown";

    // Also return true if it aborted because of an unknown type
    done_status = stat(stat_filename.c_str(), &stat_buffer) == 0;
    unknown_status = stat(unknown_filename.c_str(), &stat_buffer) == 0;

    return done_status | unknown_status;
  }

  bool was_killed(const std::string& fname)
  {
    struct stat stat_buffer = {};
    int exists = 0;
    std::string filename = std::string(results_dir) + "/" + fname + ".killed";
    exists = stat(filename.c_str(), &stat_buffer) == 0;
    // Delete it here such that other threads don't also resume
    if (exists) {
      std::remove(filename.c_str());
    }
    return exists;
  }


  Fuzzer::Fuzzer(const std::string& fname, tensorflow::OpKernelContext* ctx)
  {

    std::string mutfile_pattern;
    std::string mutfile_prefix;
    std::string proc_filename;
    std::string mut_filename;
    std::string time_filename;
    std::string except_filename;
    std::string total_filename;

    std::fstream total_file;
    std::ios_base::openmode fflags;

    bool restore = false, do_resume = false;
    long long last_mutation = -1;
    struct stat stat_buffer = {};

    glob_t glob_result = {0};
    int glob_ret = {};
    pid_t mypid = 0;
    char *existing_pid;
    bool got_last = false;
    int tries = 0;
    bool log_crash;

    tensorflow::Tensor tensor;
    tensorflow::TensorShape tensor_shape;

    /* tensorflow::LogAllRegisteredKernels(); */

    cur_fname = fname;
    op_name = ctx->op_kernel().def().name();
    attrs = tensorflow::SummarizeAttrs(ctx->op_kernel().def());

    num_args = ctx->num_inputs();

    original_ctx = new tensorflow::OpKernelContext(ctx->get_params());

    /* printf("Original num args: %d\n", original_ctx->num_inputs()); */
    /* printf("Original arguments: \n"); */
    /* for (int i = 0; i < num_args; i++) { */
    /*   std::cout << "Argument " << i << ": " << original_ctx->input(i).DebugString() << "\n"; */
    /* } */

    mypid = ::getpid();

    mutfile_pattern = std::string(results_dir) + "/" + cur_fname + "_mutations.log.*";
    mutfile_prefix = std::string(results_dir) + "/" + cur_fname + "_mutations.log";
    mut_filename = std::string(results_dir) + "/" + cur_fname + "_mutations.log." + std::to_string(mypid);
    time_filename = std::string(results_dir) + "/" + cur_fname + ".time." + std::to_string(mypid);
    except_filename = std::string(results_dir) + "/" + cur_fname + ".failed." + std::to_string(mypid);
    total_filename = std::string(results_dir) + "/totals.txt";

    fflags = std::ios::out | std::ios::in | std::ios::trunc;

    create_file(time_filename, time_file, fflags);
    create_file(except_filename, except_file, fflags);

    mutations_logger_filename = mut_filename;

    for (int r = 0; r < MUTFILE_TRIES; r++){
      glob_ret = glob(mutfile_pattern.c_str(), 0, NULL, &glob_result);
      if (glob_ret != GLOB_NOMATCH && !restore) {

        // A lot of empty mutation files, probably deadlock or bug, stop
        // fuzzing this kernel
        if (glob_result.gl_pathc > 5) {
          mark_fuzzing_done();
          std::cout << cur_fname << " has a lot of empty mutation files, skipping" << std::endl;
          return;
        }

        // A mutation file for the same function exists
        for(size_t i = 0; i < glob_result.gl_pathc && !restore; ++i) {

          existing_pid = glob_result.gl_pathv[i] + mutfile_prefix.length() + 1;
          proc_filename = "/proc/" + std::string(existing_pid);

          if (stat(proc_filename.c_str(), &stat_buffer) == 0){
            // The mutations file belongs to a running process, skip
            /* printf("%s belongs to a running process, skipping\n", glob_result.gl_pathv[i]); */
            total_mutations = 0;
            is_running = true;
            globfree(&glob_result);
            return;
          } else {
            // The mutations file doesn't belong to any running process, something crashed
            mutations_restore_filename = glob_result.gl_pathv[i];
            /* std::cout << cur_fname << "crashed, will restore from " << mutations_restore_filename << std::endl; */
            restore = true;

            if (was_killed(cur_fname)) {
              do_resume = true;
            }

          }
        }
      }
      globfree(&glob_result);
    }

    if (do_resume) {
      std::cout << mypid << ": " << cur_fname << " was killed, will resume from " << mutations_restore_filename << std::endl;
    } else if (restore) {
      std::cout << mypid << ": " << cur_fname << " crashed, will restore from " << mutations_restore_filename << std::endl;
    }
    std::cout << "Fuzzing function " << cur_fname << std::endl;

    // Disable buffering else program might crash before writing to logger
    // Force creation of the file immediately
    create_file(mutations_logger_filename, mutations_file, fflags);
    mutations_file.rdbuf()->pubsetbuf(nullptr, 0);

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

    if (restore) {

      mutations_restore.open(mutations_restore_filename, std::ios::out | std::ios::in);
      std::string last_line;
      while (!got_last && tries < 10) {
        getline(mutations_restore, last_line);
        if (last_line.length() > 0) {
          last_mutation = std::stoll(last_line);
          got_last = true;
        } else {
          std::cout << "Error while reading " << mutations_restore_filename << " (got " << last_line << ") ..." << std::endl;
          tries++;
        }
      }

      if (last_mutation > 0) {

        restore_last_mutation(last_mutation, do_resume);
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

  }

  tensorflow::TensorValue Fuzzer::get_next_mut(tensorflow::DataType ttype, int idx) {

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

  void Fuzzer::log_current_mutation(std::fstream &file)
  {
    tensorflow::DataType ttype;
    tensorflow::TensorValue tensor_val;
    std::string out_str;

    /* file << op_name << std::endl; */
    out_str += attrs + "\n";
    for (int idx = 0; idx < num_args; idx++) {
      ttype = tensor_types.at(idx);
      tensor_val = get_next_mut(ttype, idx);
      ttype = tensor_val.tensor->dtype();
      switch (ttype) {
        default:
          out_str += tensor_val.tensor->DebugString() + "\n";
          /* case tensorflow::DataType::DT_VARIANT: */
          /* file << "Variant" << std::endl << std::flush; */
          break;
        case tensorflow::DataType::DT_RESOURCE:
          out_str += "Resource\n";
          break;
      }
    }

    out_str += "\n--------------------------------------\n";
    file << out_str << std::flush;
  }

  void Fuzzer::increase_num_crashes()
  {

    long long num_crashes = 0; // Used to bound number of crashes
    struct stat stat_buffer = {};
    std::ios_base::openmode fflags = std::ios::out | std::ios::in;
    std::string crashes_num_filename;
    std::fstream run_file;
    std::string run_filename;
    std::string last_line;

    crashes_num_filename = std::string(results_dir) + "/" + cur_fname + "_crashes_num.log";

    if (stat(crashes_num_filename.c_str(), &stat_buffer) == 0){
      num_crashes_file.open(crashes_num_filename, fflags);
      getline(num_crashes_file, last_line);
      if (last_line.length() > 0) {
        num_crashes = std::stoll(last_line);
      } else {
        std::cout << "Error while reading file with number of crashes..." << std::flush;
      }
    } else {
      num_crashes = 0;
      fflags |= std::ios::trunc;
      create_file(crashes_num_filename, num_crashes_file,  fflags);
    }
    num_crashes++;

    num_crashes_file.seekp(0, std::ios::beg);
    num_crashes_file << num_crashes;
    num_crashes_file.flush();
    /* num_crashes_file.close(); */

    if (num_crashes >= CRASHES_BOUND) {
      std::cout << "Function " << cur_fname << " crashed " << CRASHES_BOUND << " times, skipping rest of fuzzing" << std::endl;

      run_filename = std::string(results_dir) + "/" + cur_fname + ".run";
      create_file(run_filename, run_file, fflags);

      run_file << total_mutations << std::flush;
      run_file.close();
      mark_fuzzing_done();
      return;
    }


  }

  void Fuzzer::restore_last_mutation(long long last_mutation, bool do_resume)
  {

    std::string crashes_filename;

    crashes_filename = std::string(results_dir) + "/" + cur_fname + "_crashes.log";
    crashes_logger_filename = crashes_filename;
    crashes_file.rdbuf()->pubsetbuf(nullptr, 0);

    // Handle the case where mutations were already done for this test
    // by just giving back one mutation so that the test doesn't crash
    if (last_mutation <= 0) {
      total_mutations = 1;
      return;
    }

    std::cout << "Resuming from mutation " << last_mutation << std::endl;

    while (total_mutations != last_mutation) {
      if (total_mutations < last_mutation) {
        std::cout << "\033[1;31mError: didn't match last mutation, aborting\n\033[0m " << cur_fname << std::endl << std::flush;
        mark_fuzzing_done();
        return;
      }
      next_mutations_indices(false);
    }

    crashes_file.open(crashes_logger_filename, std::ios::out | std::ios::app);

    /* If we weren't killed, also log the crash */
    if (!do_resume) {
      log_current_mutation(crashes_file);
    }

    increase_num_crashes();

    next_mutations_indices(true);
    std::cout << "Mutations left: " << total_mutations << std::endl;
  }

  void Fuzzer::calculate_total_mutations() {

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

    nmut_fuzz = total_mutations;
    if (total_mutations <= NMUT_LOWER_BOUND) {
      num_mut_skip = 1;
    } else {

      if (nmut_fuzz > NMUT_UPPER_BOUND_MID) {
        nmut_fuzz = NMUT_UPPER_BOUND_MID;
      }
      num_mut_skip = total_mutations / nmut_fuzz;
    }

    all_mutations = total_mutations;
    std::cout << "Total mutations: " << total_mutations << std::endl;
    std::cout << "Will run with (at least): " << total_mutations << " mutations"<< std::endl;
    std::cout << "Step size: " << num_mut_skip << std::endl;

    // To avoid off by one on first mutation
    total_mutations += num_mut_skip;

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
    std::mt19937 rngenerator(RNG_SEED);
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
    std::string filename;

    std::cout << "\033[1;31mUnknown type:\033[0m " << ttype << std::endl << std::flush;

    // Indicates a type that isn't handled in the fuzzer
    filename = std::string(results_dir) + "/" + cur_fname + ".unknown";

    std::ios_base::openmode fflags = std::ios::out | std::ios::in;
    unknown_type_file.open(filename, fflags);
    unknown_type_file << ttype << std::flush;
    unknown_type_file.close();

    abort();
  }

  void Fuzzer::mark_fuzzing_done()
  {

    std::string filename;

    // This file indicates to the fuzzer that this kernel has been already fuzzed
    filename = std::string(results_dir) + "/" + cur_fname + ".done";
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
      mutations_file.seekp(0, std::ios::beg);
      mutations_file << total_mutations;
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

    clock_gettime(CLOCK_MONOTONIC, &ts);
    start_time = ((uint64_t)ts.tv_sec) * NS_PER_SEC + ts.tv_nsec;

  }

  void Fuzzer::mut_end_time(tensorflow::OpKernelContext *fuzz_ctx)
  {

    struct timespec ts = {};
    struct stat stat_buffer = {};
    std::string duration_filename;
    std::ios_base::openmode fflags = std::ios::out | std::ios::in;
    std::fstream duration_file;

    clock_gettime(CLOCK_MONOTONIC, &ts);
    end_time = ((uint64_t)ts.tv_sec) * NS_PER_SEC + ts.tv_nsec;

    uint64_t duration = end_time - start_time;
    uint64_t duration_secs = duration / (NS_PER_SEC);

    if (fuzz_ctx->status() == tensorflow::Status::OK()) {
      time_file << total_mutations << ":" << duration << std::endl << std::flush;
    } else {
      except_file << total_mutations << ":" << duration << std::endl << std::flush;
    }


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

      duration_filename = std::string(results_dir) + "/" + cur_fname + ".duration";
      if (stat(duration_filename.c_str(), &stat_buffer) != 0) {
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
