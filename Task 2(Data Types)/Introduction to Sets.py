#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def average(array):
    # your code goes here
    array = set(array)
    n = len(array)
    sums = sum(array)
    
    result = sums/n
    return result

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

