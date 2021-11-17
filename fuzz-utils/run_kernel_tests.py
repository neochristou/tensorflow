import logging
import os
import signal
import subprocess
import time
from glob import glob
from multiprocessing import Lock, Manager, Process, current_process

NUM_PARALLEL_PROCESSES = 4
#TOTAL_TESTS = 314
RES_FOLDER = "/media/tf-fuzzing/results/"
DONE_FOLDER = "/media/tf-fuzzing/done-tests/"
TEST_FOLDER = "/media/mlfuzz/tensorflow/tensorflow/python/"
ABRT_FILE = "/media/tf-fuzzing/aborted.txt"

tests = glob(TEST_FOLDER + "**/*_test*.py", recursive=True)
TOTAL_TESTS = len(tests)
running_tests = []
done_tests = 0
crashes_set = set()
aborts_set = set()


def execute(test, proc_ecodes, pidx):
    global lock
    completed = subprocess.run(["python3", test],
                               # stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL
                               )
    if completed.returncode == -signal.SIGABRT:
        logging.critical(f"Test {test} aborted")
        lock.acquire()
        try:
            f = open(ABRT_FILE, 'a')
            f.write(test + "\n")
            f.close()
        finally:
            lock.release()

    proc_ecodes[pidx] = completed.returncode


def main():
    logging.basicConfig(level=logging.DEBUG)
    lock = Lock()
    manager = Manager()
    # Used to save the test exit codes
    proc_ecodes = manager.dict()
    proc_ids = {}
    proc_id = 0

    while done_tests < TOTAL_TESTS:

        # Use this to log status if a test is done
        changed = False

        # logging.debug("Monitoring running processes")
        procs_to_remove = []
        tests_to_remove = []
        for idx, proc in enumerate(proc_ids.keys()):

            # A test has finished running, handle it
            if not proc.is_alive():
                procs_to_remove.append(proc)
                t = running_tests[idx]
                # Remove it after the loop so as not to mess with the indices
                tests_to_remove.append(t)
                # Save the exitcode in the dictionary
                exitcode = proc_ecodes[proc_ids[proc]]

                if exitcode == -signal.SIGABRT:
                    aborts_set.add(t)

                # If the test crashed, re-queue it so that it runs again
                if exitcode < 0:
                    crashes_set.add(t)
                    logging.info(
                        f"Test {t} crashed with exit code {exitcode}")
                    tests.insert(0, t)

                # If it didn't crash, it has finished
                else:
                    done_tests += 1
                    changed = True

        # Remove the finished processes and tests
        proc_ids = {p: e for p, e in proc_ids.items()
                    if p not in procs_to_remove}
        running_tests = [t for t in running_tests if t not in tests_to_remove]

        while len(running_tests) < NUM_PARALLEL_PROCESSES and done_tests < TOTAL_TESTS:
            test_to_run = tests.pop()
            logging.info(f"Preparing to run test {test_to_run}")
            running_tests.append(test_to_run)
            p = Process(target=execute, args=(
                test_to_run, proc_ecodes, proc_id))
            proc_ids[p] = proc_id
            proc_id += 1
            p.start()
            # p.join()

        if changed:
            logging.info(f"Finished tests so far: {done_tests}")
            logging.info(f"Total crashes: {len(crashes_set)}")
            # logging.info(f"Of which are aborts: {len(aborts_set)}")

        time.sleep(10)

    for p in proc_ids.keys():
        p.join()

    logging.info(f"Total tests run: {done_tests}")


if __name__ == "__main__":
    main()
