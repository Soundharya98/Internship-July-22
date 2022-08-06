# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())

for _ in range(n):
    a, b = input().split(' ')
    x = re.match(r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>', b)
    
    if x:
      print(a,b)