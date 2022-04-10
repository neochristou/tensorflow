
def get_lines(filename):

    with open(filename, "r") as f:
        lines = f.read().strip().split('\n')

    return lines


def write_lines(filename, lines):

    with open(filename, "w") as f:
        f.write("\n".join(lines))


def main():

    cpu_all = get_lines("cpu_all.txt")
    gpu_all = get_lines("gpu_all.txt")
    all_all = set(cpu_all + gpu_all)

    cpu_modified = get_lines("cpu_modified.txt")
    gpu_modified = get_lines("gpu_modified.txt")
    all_modified = set(cpu_modified + gpu_modified)

    cpu_skipped = get_lines("cpu_skipped.txt")
    gpu_skipped = get_lines("gpu_skipped.txt")
    all_skipped = set(cpu_skipped + gpu_skipped)

    cpu_fuzzed = get_lines("cpu_fuzzed.txt")
    gpu_fuzzed = get_lines("gpu_fuzzed.txt")
    all_fuzzed = set(cpu_fuzzed + gpu_fuzzed)

    print(f"Total kernels: {len(all_all)}")
    print(f"Total modified: {len(all_modified)}")
    print(f"Total skipped: {len(all_skipped)}")
    print(f"Total fuzzed: {len(all_fuzzed)}")


if __name__ == "__main__":
    main()
