#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input(). split())
for i in range(1,n,2):
    print(str('.|.'*i).center(m, '-'))
print('WELCOME'.center(m, '-'))
for i in range(n-2, -1, -2):
    print(str('.|.'*i).center(m, '-'))

