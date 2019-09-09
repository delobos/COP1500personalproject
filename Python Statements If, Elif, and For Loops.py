#!/usr/bin/env python
# coding: utf-8

# In[2]:


#if some_condition:
    #execute some code
#elif some_other_condition:
    #do something different
#else:
    #do something else


# In[3]:


if True:
    print('ITS TRUE!')


# In[4]:


if 3 > 2:
    print('ITS TRUE!')


# In[5]:


hungry = True

if hungry:
    print('feed me')


# In[6]:


hungry = False

if hungry:
    print('Feed me!')


# In[7]:


hungry = False

if hungry:
    print('Feed me!')
else:
    print('Im not hungry')


# In[8]:


hungry = True

if hungry:
    print('Feed me!')
else:
    print('Im not hungry')


# In[10]:


loc = "Bank"

if loc == 'Auto Shop':
    print('Cars are Cool!')
else:
    print('I do not know much.')


# In[13]:


loc = "Bank"

if loc == 'Auto Shop':
    print('Cars are Cool!')
elif loc == 'Bank':
    print("Money is Cool")
else:
    print('I do not know much.')


# In[14]:


loc = "Game"

if loc == 'Auto Shop':
    print('Cars are Cool!')
elif loc == 'Bank':
    print('Money is cool')
elif loc == 'Store':
    ('Welcome to the Store!')
else:
    print('I do not know much.')


# In[16]:


loc = "Store"

if loc == 'Auto Shop':
    print('Cars are Cool!')
elif loc == 'Bank':
    print('Money is cool')
elif loc == 'Store':
    print('Welcome to the Store!')
else:
    print('I do not know much.')


# In[17]:


name = "Sammy"

if name == "Frankie":
    print('Hello Frankie!')
elif name == "Sammy":
    print('Hello Sammy!')
else:
    print("What is your name?")


# In[18]:


name = "Frankie"

if name == "Frankie":
    print('Hello Frankie!')
elif name == "Sammy":
    print('Hello Sammy!')
else:
    print("What is your name?")


# In[19]:


name = "Jose"

if name == "Frankie":
    print('Hello Frankie!')
elif name == "Sammy":
    print('Hello Sammy!')
else:
    print("What is your name?")


# In[1]:


#For Loops


# In[2]:


my_iterable = [1,2,3]
for item_name in my_iterable:
    print(item_name)


# In[3]:


mylist = [1,2,3,4,5,6,7,8,9,10]


# In[9]:


for testname in mylist:
    print(testname)


# In[10]:


for num in mylist:
    print('hello')


# In[12]:


for num in mylist:
    #check for even
    if num % 2 == 0:
        print(num)


# In[14]:


for num in mylist:
    #check for even
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd number:{num}')


# In[16]:


list_sum = 0

for num in mylist:
    list_sum = list_sum + num

print(list_sum)


# In[18]:


list_sum = 0

for num in mylist:
    list_sum = list_sum + num

    print(list_sum)
#why indentation is important


# In[19]:


mystring = "Hello World"
for letter in mystring:
    print(letter)


# In[20]:



for letter in "Hello World":
    print(letter)


# In[21]:


tup = (1,2,3)

for item in tup:
    print(item)


# In[22]:


mylist = [(1,2),(3,4),(5,6),(7,8)]


# In[23]:


len(mylist)


# In[24]:


for item in mylist:
    print(item)


# In[26]:


#tuple unpacking
for a,b in mylist:
    print(a)
    print(b)


# In[27]:


mylist = [(1,2,3),(5,6,7),(8,9,10)]


# In[28]:


for item in mylist:
    print(item)


# In[31]:


for a,b,c in mylist:
    print(b)
    


# In[32]:


#iterate through a dictionary


# In[34]:


d = {'k1': 1, 'k2': 2, 'k3': 3}

for item in d:
    print(item)


# In[35]:


d = {'k1': 1, 'k2': 2, 'k3': 3}

for item in d.items():
    print(item)


# In[36]:


d = {'k1': 1, 'k2': 2, 'k3': 3}

for key,value in d:
    print(value)


# In[38]:


d = {'k1': 1, 'k2': 2, 'k3': 3}

for value in d.values():
    print(value)


# In[ ]:




