import os
from glob import glob

RESULTS_DIR = "/media/mlfuzz/tensorflow/crashes/run_jan14/"
COVERAGE_PERCENT_THRESH = 1.0
MUTATIONS_BOUND = 1000000

all_mutations = {}
run_mutations = {}
failed_mutations = {}
total_mutations = {}
no_total = set()
empty_crash_funcs = []
below_thresh_funcs = []
above_thresh_funcs = []


def get_all_mutations():
    with open(RESULTS_DIR + "totals.txt", 'r') as f:
        totals = f.read().strip().split('\n')
        for tup in totals:
            fname, total = tup.split(':')
            total = int(total)
            run_file_name = RESULTS_DIR + fname + '.run'
            if os.path.isfile(run_file_name):
                # Only total - run mutations actually run
                with open(run_file_name, 'r') as r:
                    total = total - int(r.read())
            all_mutations[fname] = total


def get_failed_mutations():
    for filename in glob(RESULTS_DIR + "*.failed.*"):
        fname = filename[:filename.index(".failed")].replace(RESULTS_DIR, '')
        if fname not in failed_mutations:
            failed_mutations[fname] = 0
        with open(filename, 'r') as f:
            muts = f.read().strip('\n').split('\n')
            if len(muts) == 1:
                if muts[0] == '':
                    nmuts = 0
            else:
                nmuts = len(muts)
            failed_mutations[fname] += nmuts


def get_run_mutations():
    for filename in glob(RESULTS_DIR + "*.time.*"):
        fname = filename[:filename.index(".time")].replace(RESULTS_DIR, '')
        if fname not in run_mutations:
            run_mutations[fname] = 0
        with open(filename, 'r') as f:
            muts = f.read().strip('\n').split('\n')
            nmuts = len(muts)
            if len(muts) == 1:
                if muts[0] == '':
                    nmuts = 0
            else:
                nmuts = len(muts)
            run_mutations[fname] += nmuts


def get_total_mutations():
    for fname, tot in run_mutations.items():
        if fname not in total_mutations:
            total_mutations[fname] = 0
        total_mutations[fname] += tot
    for fname, tot in failed_mutations.items():
        if fname not in total_mutations:
            total_mutations[fname] = 0
        total_mutations[fname] += tot


def get_percentages():
    global below_thresh_funcs, above_thresh_funcs
    run_sum = 0
    total_sum = 0
    above_bound = 0
    max_mutations_num = 0
    max_mutations_func = ''
    for fname, total in total_mutations.items():

        if fname not in all_mutations:
            no_total.add(fname)
            continue

        all_muts = all_mutations[fname]

        if all_muts > MUTATIONS_BOUND:
            above_bound += 1

        if fname in run_mutations:

            run = run_mutations[fname]

            if run > max_mutations_num:
                max_mutations_num = run
                max_mutations_func = fname

            if total == 0:
                percent = 0
            else:
                percent = run / total * 100
            print(f"{fname}: {percent}% ({run}/{total})")

            if percent < COVERAGE_PERCENT_THRESH:
                below_thresh_funcs.append(fname)
            else:
                above_thresh_funcs.append(fname)

            run_sum += run
            total_sum += total
        else:
            print(f"{fname} not in run mutations")

    avg_percent = run_sum / total_sum * 100
    avg_muts_per_func = run_sum / len(run_mutations.keys())
    print(
        f"Most successful mutations by a single function: {max_mutations_num} ({max_mutations_func})")
    print(
        f"Number of functions with more than {MUTATIONS_BOUND} total mutations: {above_bound}")
    print(f"Average coverage: {avg_percent}%")
    print(f"Average mutations per function: {avg_muts_per_func}")
    print(
        f"Total covered above {COVERAGE_PERCENT_THRESH}%: {len(above_thresh_funcs)}")


def get_below_thresh():
    global below_thresh_funcs

    have_crashes_funcs = []

    for fname in below_thresh_funcs:
        crash_filename = fname + '_crashes.log'
        if os.path.isfile(RESULTS_DIR + crash_filename):
            if os.path.getsize(RESULTS_DIR + crash_filename) > 1:
                have_crashes_funcs.append(fname)
            else:
                empty_crash_funcs.append(fname)

    print(
        f"Functions below {COVERAGE_PERCENT_THRESH}% coverage: {' '.join(below_thresh_funcs)}")
    print(f"Of which have crashes: {' '.join(have_crashes_funcs)}")
    print(f"Total functions below threshold: {len(below_thresh_funcs)}")
    print(
        f"Of which have crashes: {len(have_crashes_funcs)} ({len(below_thresh_funcs) - len(have_crashes_funcs)} without crashes)")
    print(f"Fuctions with empty crash files: {len(empty_crash_funcs)}")


if __name__ == "__main__":

    get_all_mutations()

    get_failed_mutations()
    get_run_mutations()
    get_total_mutations()

    get_percentages()
    get_below_thresh()

    print(f"Total functions that didn't log total mutations: {len(no_total)}")
    print(f"Total successful mutations: {sum(run_mutations.values())}")
