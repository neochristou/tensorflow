import logging
import os
import signal
import subprocess
import time
from glob import glob
from multiprocessing import Lock, Process

NUM_PARALLEL_PROCESSES = 4
TOTAL_TESTS = 4
# TOTAL_TESTS = 314
RES_FOLDER = "/media/tf-fuzzing/results/"
DONE_FOLDER = "/media/tf-fuzzing/done-tests/"
TEST_FOLDER = "/media/mlfuzz/tensorflow/tensorflow/python/kernel_tests/"
ABRT_FILE = "/media/tf-fuzzing/aborted.txt"

tests = glob(TEST_FOLDER + "**/*_test.py", recursive=True)
running_tests = []
done_tests = 0

processes = []


def execute(test):
    global lock
    completed = subprocess.run(["python3", test],
                               # stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL)
    if completed.returncode == -signal.SIGABRT:
        logging.critical(f"Test {test} aborted")
        lock.acquire()
        try:
            f = open(ABRT_FILE, 'a')
            f.write(test + "\n")
            f.close()
        finally:
            lock.release()
    return completed.returncode


logging.basicConfig(level=logging.DEBUG)
lock = Lock()

while done_tests < TOTAL_TESTS:

    logging.debug("Monitoring running processes")
    procs_to_remove = []
    tests_to_remove = []
    for idx, proc in enumerate(processes):
        if not proc.is_alive():
            procs_to_remove.append(proc)
            t = running_tests[idx]
            tests_to_remove.append(t)
            if proc.exitcode < 0:
                logging.info(
                    f"Test {t} crashed with exit code {proc.exitcode}")
                tests.insert(0, t)
            else:
                done_tests += 1

    processes = [p for p in processes if p not in procs_to_remove]
    running_tests = [p for p in running_tests if p not in tests_to_remove]

    while len(running_tests) < NUM_PARALLEL_PROCESSES and done_tests < TOTAL_TESTS:
        test_to_run = tests.pop()
        logging.info(f"Preparing to run test {test_to_run}")
        running_tests.append(test_to_run)
        p = Process(target=execute, args=(test_to_run, ))
        processes.append(p)
        p.start()

    time.sleep(10)
