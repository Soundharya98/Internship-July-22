#!/bin/python3

import re
a, b = map(int,input().split())
character_ar = [''] * (a*b)

for i in range(a):
   line = input()
   for j in range(b):
    character_ar[i+(j*a)]=line[j]
    
decoded_str = ''.join(character_ar)
final_decoded_str = re.sub(r'(?<=[A-Za-z0-9])([ !@#$%&]+)(?=[A-Za-z0-9])',' ',decoded_str)
print(final_decoded_str)
