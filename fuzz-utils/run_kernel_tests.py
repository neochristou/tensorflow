import logging
import os
import signal
import subprocess
import time
from glob import glob
from multiprocessing import Lock, Manager, Pool, Process

TF_BASE = "/media/ivysyn/tensorflow/"
NUM_PARALLEL_PROCESSES = 4
MAX_RESTARTS = 10
TIME_LIMIT = 900
PYTHON_TEST_FOLDER = TF_BASE + "tensorflow/python/"
CC_TEST_FOLDER = TF_BASE + "bazel-out/k8-opt/bin/tensorflow/core/kernels/"
# ABRT_FILE = "/media/tf-fuzzing/aborted.txt"
TEST_DURATION_FILE = "/media/tf-fuzzing/test_durations.txt"
BAZEL_TEST_ARGS = ['--test_output=all',
                   '--cache_test_results=no', '--runs_per_test=20', '--flaky_test_attempts=10']

EXCLUDE_TESTS = [
    # Opens connection, gets confused because of fuzzing
    '/media/ivysyn/tensorflow/tensorflow/python/eager/remote_cluster_test.py',
    '/media/ivysyn/tensorflow/tensorflow/python/keras/saving/save_weights_test.py'
]

tests_to_run = glob(PYTHON_TEST_FOLDER + "**/*_test*.py", recursive=True)
print(f"Python tests: {len(tests_to_run) - len(EXCLUDE_TESTS)}")
cc_tests = glob(CC_TEST_FOLDER + "*_test")
print(f"CPP tests: {len(cc_tests)}")
tests_to_run += cc_tests
for t in EXCLUDE_TESTS:
    tests_to_run.remove(t)

TOTAL_TESTS = len(tests_to_run)

done_tests = set()
crashes_set = set()
aborts_set = set()
killed_set = set()

restart_count = {}


def execute(test):

    args = []

    if PYTHON_TEST_FOLDER in os.path.realpath(test):
        args = ["python3", test]
    elif CC_TEST_FOLDER in os.path.realpath(test):
        bazel_test = '//tensorflow/core/kernels:' + test
        args = ["bazel", "test", bazel_test] + BAZEL_TEST_ARGS

    retcode = 0

    start_time = time.time()
    try:
        completed = subprocess.run(args,
                                   # stdout=subprocess.DEVNULL,
                                   stderr=subprocess.DEVNULL,
                                   timeout=TIME_LIMIT)
        retcode = completed.returncode
    except subprocess.TimeoutExpired as e:
        logging.debug(f"Timeout expired for {test}")
        retcode = -9
    finally:
        end_time = time.time() - start_time
        return (test, end_time, retcode)


def log_test_duration(dur, test):
    f = open(TEST_DURATION_FILE, 'a+')
    mins = int(dur) / 60
    f.write(test + " " + str(mins) + "\n")
    f.close()


def proc_finished(results):

    global restart_count

    test, running_time, exitcode = results

    log_test_duration(running_time, test)

    if exitcode == -signal.SIGABRT:
        aborts_set.add(test)

    # If the test crashed, re-queue it so that it runs again
    if exitcode < 0:

        crashes_set.add(test)

        if test not in restart_count:
            restart_count[test] = 0

        restart_count[test] += 1

        if restart_count[test] <= MAX_RESTARTS:
            logging.debug(
                f"Test {test} crashed with exit code {exitcode}, requeueing")
            tests_to_run.append(test)
    else:
        done_tests.add(test)


if __name__ == "__main__":

    # logging.basicConfig(level=logging.INFO)
    logging.basicConfig(level=logging.DEBUG)
    # lock = Lock()
    manager = Manager()
    pool = Pool(processes=NUM_PARALLEL_PROCESSES)
    last_finished = 0

    while len(done_tests) < TOTAL_TESTS:

        while len(tests_to_run) > 0:

            test_to_run = tests_to_run.pop()
            p = pool.apply_async(execute, args=(test_to_run,),
                                 callback=proc_finished,
                                 error_callback=proc_finished)

            # logging.info(f"Total crashes: {len(crashes_set)}")
            # logging.info(f"Of which are aborts: {len(aborts_set)}")
            # logging.info(f"Of which were killed: {len(killed_set)}")

        time.sleep(10)
        finished = len(done_tests)
        if finished != last_finished:
            logging.info(f"Finished tests so far: {finished}")
            last_finished = finished

    logging.info(f"Total tests run: {len(done_tests)}")
