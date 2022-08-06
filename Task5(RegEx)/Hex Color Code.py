# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
in_css = False

for _ in range(n):
    a = input()
    if '{' in a:
      in_css = True
    elif '}' in a:
        in_css = False
    elif in_css:
        for color in re.findall('#[0-9a-fA-F]{3,6}',a):
            print(color) 