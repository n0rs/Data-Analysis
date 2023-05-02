from math import sqrt
from scipy.stats import norm

mean = 1.715588
std_dev = 0.029252
n =  34
p = .99

def critical_z_value(p):
    norm_dist = norm(loc=0.0, scale=1.0)
    lower_area = (1.0 - p) / 2.0
    upper_area = 1.0 - ((1.0 - p) / 2.0)
    return norm_dist.ppf(lower_area), norm_dist.ppf(upper_area)

def confidence(p, mean, std_dev, n):
    lower, upper = critical_z_value(p)

    lower_ci = lower * (std_dev / sqrt(n))
    upper_ci = upper * (std_dev / sqrt(n))

    return mean + lower_ci, mean + upper_ci

print(confidence(p, mean, std_dev, n))
