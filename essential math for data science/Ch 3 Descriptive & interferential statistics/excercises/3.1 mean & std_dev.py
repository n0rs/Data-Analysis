from math import sqrt

sample = [1.78, 1.75, 1.72, 1.74, 1.77]

mean = sum(sample) / len(sample)
std_dev = sqrt(sum((v - mean) ** 2 for v in sample) / len(sample))

print(f"Mean: {mean}")
print(f"Standard deviation: {std_dev}")