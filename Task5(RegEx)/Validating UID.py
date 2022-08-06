# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for i in range(int(input())):
    a = input().strip()
    if a.isalnum() and len(a) == 10:
        if bool(re.search(r'(.*[A-Z]){2,}', a)) and bool(re.search(r'(.*[0-9]){3,}', a)):
            if re.search(r'.*(.).*\1+.*', a):
                print('Invalid')
            else:
                print('Valid')
        else:
            print('Invalid')
    else:
        print('Invalid')           
