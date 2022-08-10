# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

num_tickets = float(input())
num_students = float(input())
mean = num_students * float(input())
std_dev = math.sqrt(num_students) * float(input())

print(round(0.5*(1+math.erf((num_tickets - mean)/(std_dev * math.sqrt(2)))),4))