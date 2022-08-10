# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

x = int(input())
n = int(input())
mean = int(input())
std_dev = int(input())

mean_sum = n * mean
std_dev_sum = math.sqrt(n) * std_dev

def cdf(x, mean, std_dev):
    A = (x - mean)/std_dev
    return 0.5*(1 + math.erf(A/(math.sqrt(2))))

print(round(cdf(x, mean_sum, std_dev_sum), 4))