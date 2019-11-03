#!/usr/bin/env python
# coding: utf-8

# In[1]:


def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x**3)
    return result


# In[2]:


create_cubes(10)


# In[3]:


for x in create_cubes(10):
    print(x)


# In[4]:


def create_cubes(n):
    
    for x in range(n):
        yield x**3


# In[7]:


for x in create_cubes(10):
    print(x)


# In[8]:


create_cubes(10)


# In[9]:


list(create_cubes(10))


# In[10]:


def gen_fibon(n):
    
    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b, a+b


# In[11]:


for number in gen_fibon(10):
    print(number)


# In[12]:


def gen_fibon(n):
    
    a = 1
    b = 1
    output = []
    
    for i in range(n):
        yield a
        a,b = b, a+b
    return  output


# In[13]:


for number in gen_fibon(10):
    print(number)


# In[ ]:





# In[ ]:





# In[ ]:





# In[14]:


def simple_gen():
    for x in range(3):
        yield x


# In[15]:


for number in simple_gen():
    print(number)


# In[16]:


g = simple_gen()


# In[17]:


g


# In[18]:


print(next(g))


# In[19]:


print(next(g))


# In[20]:


print(next(g))


# In[21]:


print(next(g))


# In[22]:


s = "hello"


# In[23]:


for letter in s:
    print(letter)


# In[24]:


next(s)


# In[25]:


s_iter = iter(s)


# In[26]:


next(s_iter)


# In[27]:


next(s_iter)


# In[28]:


next(s_iter)


# In[29]:


next(s_iter)


# In[30]:


next(s_iter)


# In[ ]:




