from scipy.stats import norm

mean = 42
std_dev = 8

p = norm.cdf(30, mean, std_dev) - norm.cdf(20, mean, std_dev)

print(p)