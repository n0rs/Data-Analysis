from scipy.stats import beta

a = 15
b = 4
p = .5

# probability of being fair coin
probability = beta.cdf(p, a, b)

# probability of being unfair
print(1 - probability)
