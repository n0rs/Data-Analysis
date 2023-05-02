from scipy.stats import binom

n = 137
p = .40

probability = 0

# probability of 50 people not attending flight
for k in range(50, 138):
    probability += binom.pmf(k, n, p)

print(probability)