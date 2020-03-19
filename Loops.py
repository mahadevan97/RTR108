#!/usr/bin/env python
# coding: utf-8

# In[1]:


n = 5
while n > 0:
    print(n)
    n = n - 1
print('Blastoff!')


# In[ ]:


n = 10
while True:
    print(n, end=' ')
    n = n - 1
print('Done!')


# In[ ]:


n=0
while n>0:
    print('lather')
    print('rinse')
print('blastoff')


# In[ ]:


while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')


# In[ ]:


n = 10
while True:
    print(n, end=' ')
    n = n - 1
print('Done!')


# In[ ]:


> hello there
hello there
> finished
finished
> done
Done!


# In[ ]:


friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)
print('Done!')


# In[ ]:


friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)
print('Done!')


# In[ ]:


largest = None
print('Before:', largest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if largest is None or itervar > largest :
        largest = itervar
    print('Loop:', itervar, largest)
print('Largest:', largest)


# In[ ]:


smallest = None
print('Before:', smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
    print('Loop:', itervar, smallest)
print('Smallest:', smallest)


# In[ ]:


def min(values):
    smallest = None
    for value in values:
        if smallest is None or value < smallest:
            smallest = value
    return smallest


# In[ ]:




