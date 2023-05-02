from scipy.stats import norm

mean = 10345
std_dev = 552

p1 = 1.0 - norm.cdf(11641, mean, std_dev)

p2 = p1

p_value = p1 + p2

print(f"Two-tailed P-value: {p_value}")
if p_value <= .05:
    print("Passes two-tailed test")
else:
    print("Does not pass two-tailed test")