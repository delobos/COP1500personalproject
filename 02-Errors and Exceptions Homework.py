#!/usr/bin/env python
# coding: utf-8

# # Errors and Exceptions Homework

# ### Problem 1
# Handle the exception thrown by the code below by using <code>try</code> and <code>except</code> blocks.

# In[6]:


try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print("sorry cant multiply a string")


# ### Problem 2
# Handle the exception thrown by the code below by using <code>try</code> and <code>except</code> blocks. Then use a <code>finally</code> block to print 'All Done.'

# In[2]:


x = 5
y = 0
try:
    z = x/y
except ZeroDivisionError:
    print("Cant divide by 0")
finally:
    print("All Done")


# ### Problem 3
# Write a function that asks for an integer and prints the square of it. Use a <code>while</code> loop with a <code>try</code>, <code>except</code>, <code>else</code> block to account for incorrect inputs.

# In[7]:


def ask():
    while True:
        try:
            number = int(input('Enter a number: '))
        except:
            print('Please enter a number')
        else:
            print(number**2)
            break


# In[8]:


ask()


# # Great Job!
