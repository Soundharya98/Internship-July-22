#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath;

num = complex(input())
Z = complex(num)

print (cmath.polar(Z)[0])
print (cmath.polar(Z)[1])

