import glob
import os

CRASHES_DIR = "/media/mlfuzz/tensorflow/crashes/"


def get_done_functions():
    done_functions = set()
    result_dirs = os.listdir(CRASHES_DIR)
    for result_dir in result_dirs:
        result_dir = CRASHES_DIR + result_dir
        for done_file in glob.glob(result_dir + "/*.done"):
            done_file = os.path.basename(done_file)
            done_functions.add(done_file)
    print(
        f"Total done functions: {len(done_functions)}")


def get_total_crashes():
    crashes = set()
    result_dirs = os.listdir(CRASHES_DIR)
    for result_dir in result_dirs:
        result_dir = CRASHES_DIR + result_dir
        for crash_file in glob.glob(result_dir + "/*_crashes.log"):
            if os.path.getsize(crash_file) > 1:
                crash_file = os.path.basename(crash_file)
                crashes.add(crash_file)
    # if not asan:
    #     print(crashes)
    print(f"Total crashes: {len(crashes)}")
    print(crashes)


if __name__ == "__main__":

    get_done_functions()
    get_total_crashes()
