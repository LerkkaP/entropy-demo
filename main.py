from collections import Counter
from math import log2

file_name = "sample.txt"
with open(file_name, "r") as f:
    file_content = f.read()

N = len(file_content)
char_counts = Counter(file_content)
entropy = -sum((c/N) * log2(c/N) for c in char_counts.values())

print(f"Entropy of the given text file is {entropy:.2f}.")