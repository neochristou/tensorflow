
modified_kernels_file = open('./modified_kernels_parsed.txt', 'r')
raw_ops_file = open('./raw_ops.txt', 'r')

modified_kernels = modified_kernels_file.read().split('\n')
raw_ops = raw_ops_file.read().split('\n')

non_modified = [x for x in raw_ops if x not in modified_kernels]

print("Kernels in raw ops that were not instrumented:")
print('\n'.join(non_modified))
print()
print(f"Total: {len(non_modified)}")

modified_kernels_file.close()
raw_ops_file.close()
