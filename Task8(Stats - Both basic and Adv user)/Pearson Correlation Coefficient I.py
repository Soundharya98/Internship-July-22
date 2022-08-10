# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

n = int(input())
x = list(map(float,input().strip().split()))
y = list(map(float,input().strip().split()))

mean_x = sum(x)/n
mean_y = sum(y)/n

std_dev_x = (sum([(i-mean_x)**2 for i in x])/n)**0.5
std_dev_y = (sum([(i-mean_y)**2 for i in y])/n)**0.5

covariance = sum([(x[i]-mean_x) * (y[i]-mean_y) for i in range(n)])
correlation_coefficient = covariance/(n*std_dev_x*std_dev_y)

print(round(correlation_coefficient, 3))