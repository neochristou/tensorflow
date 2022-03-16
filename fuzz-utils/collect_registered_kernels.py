import glob
import re

TF_BASE = "/media/ivysyn/tensorflow/"
TF_KERNELS_PATH = TF_BASE + "tensorflow/core/kernels/"
OUT_FILE = TF_BASE + "fuzz-utils/kernel_regs.txt"


def main():

    kernel_regs = {}
    kernel_files = glob.glob(TF_KERNELS_PATH + "**/*.cc", recursive=True) + glob.glob(
        TF_KERNELS_PATH + "**/*.h", recursive=True
    )
    for filename in kernel_files:
        with open(filename, "r") as f:
            data = f.read().strip()
            registrations = re.findall(
                r'REGISTER_KERNEL_BUILDER\(.*?Name\("(.*?)"\).*?\),(.*?)\)', data, flags=re.DOTALL
            )
            for reg in registrations:
                parsed_reg = [re.sub("\<.*", "", x, flags=re.DOTALL)
                              for x in reg]
                parsed_reg = [re.sub("\s+", "", x) for x in parsed_reg]
                parsed_reg = [re.sub("\\\\", "", x) for x in parsed_reg]
                op_name = parsed_reg[0]
                kernel_name = parsed_reg[1]
                kernel_regs[kernel_name] = op_name
                if kernel_name.endswith("Base"):
                    kernel_regs[kernel_name.replace("Base", "")] = op_name

    kernel_regs = "\n".join([f"{k} {v}" for k, v in kernel_regs.items()])

    with open(OUT_FILE, "w") as f:
        f.write(kernel_regs)


if __name__ == "__main__":
    main()
