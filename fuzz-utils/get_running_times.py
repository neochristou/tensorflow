import os
import statistics
from glob import glob

RESULTS_DIR = "/media/mlfuzz/tensorflow/crashes/run_feb01_2/"
NS_PER_SEC = (1000 * 1000 * 1000)
wrong_timings = 0


def get_timings_sums(files):
    global wrong_timings

    total_time_per_kernel = {}

    for filename in files:

        fname = filename[:filename.index('.')].split('/')[-1]

        if fname not in total_time_per_kernel:
            total_time_per_kernel[fname] = 0

        with open(filename, 'r') as f:
            timings = f.read().strip()
            timings = timings.split('\n')

        if len(timings) == 0:
            continue

        for tpair in timings:
            if ':' not in tpair:
                wrong_timings += 1
                continue
            tpair = [x for x in tpair.split(':') if x != '']
            if len(tpair) != 2:
                wrong_timings += 1
                continue
            t = tpair[1]
            if len(t) > 8:
                wrong_timings += 1
                continue
            total_time_per_kernel[fname] += int(t)

    return total_time_per_kernel


if __name__ == "__main__":

    timing_files = glob(RESULTS_DIR + "*.failed*") + \
        glob(RESULTS_DIR + "*.time*")
    total_time_per_kernel = get_timings_sums(timing_files)

    max_time = max(total_time_per_kernel.values())
    max_time_kernel_name = max(
        total_time_per_kernel, key=total_time_per_kernel.get)

    min_time = min(total_time_per_kernel.values())
    min_time_kernel_name = min(
        total_time_per_kernel, key=total_time_per_kernel.get)

    total_time_perk_kernel_no_zeros = dict(
        filter(lambda elem: elem[1] != 0, total_time_per_kernel.items()))
    min_time_no_zeros = min(total_time_perk_kernel_no_zeros.values())
    min_time_kernel_name_no_zeros = min(
        total_time_perk_kernel_no_zeros, key=total_time_perk_kernel_no_zeros.get)

    total_time = sum(total_time_per_kernel.values())
    avg_time = total_time / len(total_time_per_kernel.keys())

    stdev = statistics.stdev(total_time_per_kernel.values())

    total_times_secs = [(x / NS_PER_SEC)
                        for x in total_time_per_kernel.values()]
    stdev_secs = statistics.stdev(total_times_secs)

    print(
        f"Max time: {max_time_kernel_name} -- {max_time // NS_PER_SEC} seconds ({max_time} ns)")
    print(
        f"Min time: {min_time_kernel_name} -- {min_time // NS_PER_SEC} seconds ({min_time} ns)")
    print(
        f"Min time no zeros: {min_time_kernel_name_no_zeros} -- {min_time_no_zeros // NS_PER_SEC} seconds ({min_time_no_zeros} ns)")
    print(
        f"Average time per kernel: {avg_time // NS_PER_SEC} seconds ({avg_time} ns)")
    print(f"Stdev: {stdev}")
    print(f"Stdev in seconds: {stdev_secs}")
    print(f"Wrong timinigs {wrong_timings}")
