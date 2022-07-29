#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    happiness = 0
    
    n,m = map(int, input().strip().split(' '))
    array = list(map(int, input().strip().split(' ')))
    
    good = set(map(int, input().strip().split(' ')))
    bad = set(map(int, input().strip().split(' ')))
    
    for i in array:
        if i in good:
            happiness += 1
        elif i in bad:
            happiness -= 1
    print(happiness)    

