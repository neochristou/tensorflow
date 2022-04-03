skipped_reasons = {}


def get_all_kernels(lines):
    allk_lines = [x for x in lines if x.startswith("Found Compute")]
    allk_names = [x.split(" ")[-1] for x in allk_lines]
    allk_names = set(allk_names)
    return allk_names


def get_modified(lines):
    modified_lines = [x for x in lines if x.startswith("Successfully")]
    modified_names = [x.split(" ")[-1] for x in modified_lines]
    modified_names = set(modified_names)
    return modified_names


def get_skipped(lines, modified):
    skipped_lines = [x for x in lines if x.startswith("Skipping")]
    skipped = {x.split(" ")[1]: x[x.index("(") + 1 :][:-1] for x in skipped_lines}
    skipped_filtered = {x: skipped[x] for x in skipped if x not in modified}

    for reason in skipped_filtered.values():

        if reason not in skipped_reasons:
            skipped_reasons[reason] = 0

        skipped_reasons[reason] += 1

    return skipped_filtered.keys()


def main():

    with open("output.txt", "r") as f:
        lines = f.read().strip().split("\n")

    all_kernels = get_all_kernels(lines)
    modified = get_modified(lines)
    skipped = get_skipped(lines, modified)

    print(f"{len(all_kernels)} with Compute() calls\n")
    print(f"{len(modified)} instrumented\n")
    print(f"{len(skipped)} skipped. Breakdown:")
    print("\n".join([f"\t{k}: {v}" for k, v in skipped_reasons.items()]))


if __name__ == "__main__":
    main()
