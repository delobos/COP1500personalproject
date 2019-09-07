#!/usr/bin/env python
# coding: utf-8

# # Objects and Data Structures Assessment Test

# ## Test your knowledge. 
# 
# ** Answer the following questions **

# Write a brief description of all the following Object Types and Data Structures we've learned about: 

# Numbers: integers that have a value that you can add, subtract, divide, multiple, add exponents to, and assign to various functions.
# 
# Strings: a sequence where all the elements are kept in order inputted
# 
# Lists: a grouping or sequencing of integers, strings, or both that can be changed.
# 
# Tuples: immutable list that only counts unique items in it
# 
# Dictionaries: lists that can uses mapping or keys to return information needed and where you do not need to know the place the information is in just the key
# 

# ## Numbers
# 
# Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.
# 
# Hint: This is just to test your memory of the basic arithmetic commands, work backwards from 100.25

# In[1]:


5 ** 2 * 8 / 2 + 1 -.75


# Answer these 3 questions without typing code. Then type code to check your answer.
# 
#     What is the value of the expression 4 * (6 + 5)
#     
#     What is the value of the expression 4 * 6 + 5 
#     
#     What is the value of the expression 4 + 6 * 5 

# In[8]:


"4 * (6 + 5) = 44"
a = 4 * (6 + 5)

"4 * 6 + 5 = 29"
b = 4 * 6 + 5

"4 + 6 * 5 = 34"
c = 4 + 6 * 5
print(a , b ,c)


# What is the *type* of the result of the expression 3 + 1.5 + 4?<br><br>
# Float

# What would you use to find a number’s square root, as well as its square?
# put 1/2 as the exponent for square root and 2 if im squaring it

# In[11]:


# Square root: x ** (1/2)


# In[ ]:


# Square: x ** 2


# ## Strings

# Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:

# In[13]:


s = 'hello'
# Print out 'e' using indexing
print(s[1])


# Reverse the string 'hello' using slicing:

# In[24]:


s ='hello'
# Reverse the string using slicing

print(s[::-1])


# Given the string hello, give two methods of producing the letter 'o' using indexing.

# In[18]:


s ='hello'
# Print out the 'o'

# Method 1:

print(s[-1:])


# In[19]:


# Method 2:

print(s[4:])


# ## Lists

# Build this list [0,0,0] two separate ways.

# In[77]:


# Method 1:
method1 = [0,0,0]
method1


# In[79]:


# Method 2:
method2 = [0] *3
method2


# Reassign 'hello' in this nested list to say 'goodbye' instead:

# In[42]:


list3 = [1,2,[3,4,'hello']]
list3[2][2] = "goodbye"
list3


# Sort the list below:

# In[44]:


list4 = [5,3,4,6,1]

list4.sort()
list4


# ## Dictionaries

# Using keys and indexing, grab the 'hello' from the following dictionaries:

# In[46]:


d = {'simple_key':'hello'}
# Grab 'hello'
d['simple_key']


# In[50]:


d = {'k1':{'k2':'hello'}}
# Grab 'hello'
d['k1']['k2']


# In[80]:


# Getting a little tricker
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}

#Grab hello
d['k1'][0]["nest_key"][1][0]


# In[81]:


# This will be hard and annoying!
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}

d['k1'][2]['k2'][1]['tough'][2][0]


# Can you sort a dictionary? Why or why not?<br><br>
# no because normal dictionaries are mappings not sequence

# ## Tuples

# What is the major difference between tuples and lists?<br><br>
# TUPLES ARE IMMUTABLE AND LISTS ARE NOT

# How do you create a tuple?<br><br>
# OPEN PARENTHESIS

# ## Sets 

# What is unique about a set?<br><br>
# IT ONLY COUNTS UNIQUE INPUTS

# Use a set to find the unique values of the list below:

# In[82]:


list5 = (1,2,2,33,4,4,11,22,3,3,2)
set(list5)




# ## Booleans

# For the following quiz questions, we will get a preview of comparison operators. In the table below, a=3 and b=4.
# 
# <table class="table table-bordered">
# <tr>
# <th style="width:10%">Operator</th><th style="width:45%">Description</th><th>Example</th>
# </tr>
# <tr>
# <td>==</td>
# <td>If the values of two operands are equal, then the condition becomes true.</td>
# <td> (a == b) is not true.</td>
# </tr>
# <tr>
# <td>!=</td>
# <td>If values of two operands are not equal, then condition becomes true.</td>
# <td> (a != b) is true.</td>
# </tr>
# <tr>
# <td>&gt;</td>
# <td>If the value of left operand is greater than the value of right operand, then condition becomes true.</td>
# <td> (a &gt; b) is not true.</td>
# </tr>
# <tr>
# <td>&lt;</td>
# <td>If the value of left operand is less than the value of right operand, then condition becomes true.</td>
# <td> (a &lt; b) is true.</td>
# </tr>
# <tr>
# <td>&gt;=</td>
# <td>If the value of left operand is greater than or equal to the value of right operand, then condition becomes true.</td>
# <td> (a &gt;= b) is not true. </td>
# </tr>
# <tr>
# <td>&lt;=</td>
# <td>If the value of left operand is less than or equal to the value of right operand, then condition becomes true.</td>
# <td> (a &lt;= b) is true. </td>
# </tr>
# </table>

# What will be the resulting Boolean of the following pieces of code (answer fist then check by typing it in!)

# In[83]:


# Answer before running cell
2 > 3
#False


# In[84]:


# Answer before running cell
3 <= 2
#False


# In[85]:


# Answer before running cell
3 == 2.0
#False


# In[86]:


# Answer before running cell
3.0 == 3
#True


# In[87]:


# Answer before running cell
4**0.5 != 2
#False


# Final Question: What is the boolean output of the cell block below?

# In[89]:


# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

# True or False?
l_one[2][0] >= l_two[2]['k1']
#False


# ## Great Job on your first assessment! 
