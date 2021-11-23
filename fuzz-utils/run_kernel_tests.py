import logging
import os
import signal
import subprocess
import time
from glob import glob
from multiprocessing import Lock, Manager, Pool, Process

NUM_PARALLEL_PROCESSES = 5
NUM_CRASHES = 3
TIME_LIMIT = 900
PYTHON_TEST_FOLDER = "/media/mlfuzz/tensorflow/tensorflow/python/"
CC_TEST_FOLDER = "/media/mlfuzz/tensorflow/bazel-out/k8-opt/bin/tensorflow/core/kernels/"
# ABRT_FILE = "/media/tf-fuzzing/aborted.txt"
TEST_DURATION_FILE = "/media/tf-fuzzing/test_durations.txt"

tests_to_run = glob(PYTHON_TEST_FOLDER + "**/*_test*.py", recursive=True)
tests_to_run += glob(CC_TEST_FOLDER + "*_test")

TOTAL_TESTS = len(tests_to_run)

done_tests = set()
crashes_set = set()
aborts_set = set()
killed_set = set()

crash_counts = {}


def execute(test):

    args = [test]

    if PYTHON_TEST_FOLDER in os.path.realpath(test):
        args.insert(0, "python3")

    retcode = 0

    start_time = time.time()
    try:
        completed = subprocess.run(args,
                                   stdout=subprocess.DEVNULL,
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
    f = open(TEST_DURATION_FILE, 'a')
    mins = int(dur) / 60
    f.write(test + " " + str(mins) + "\n")
    f.close()


def proc_finished(results):

    test, running_time, exitcode = results

    done_tests.add(test)
    log_test_duration(running_time, test)

    if exitcode == -signal.SIGABRT:
        aborts_set.add(test)

    # If the test crashed, re-queue it so that it runs again
    if exitcode < 0:

        if test not in crash_counts:
            crash_counts[test] = 0

        crash_counts[test] += 1
        crashes_set.add(test)
        logging.debug(
            f"Test {test} crashed with exit code {exitcode}, requeueing")

        if crash_counts[test] < NUM_CRASHES:
            tests_to_run.append(test)


if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO)
    # logging.basicConfig(level=logging.DEBUG)
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
