#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
N1 = int(input())
storage1 = set(input().split())

N2 = int(input())
storage2 = set(input().split())

storage3 = storage1.symmetric_difference(storage2)
print(len(storage3))

