#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Python debugger


# In[2]:


import pdb


# In[3]:


x = [1,3,4]
y = 2
z = 3

result = y + z
print(result)
result2 = y + x
print(result2)


# In[4]:


x = [1,3,4]
y = 2
z = 3

result = y + z
print(result)

pdb.set_trace()

result2 = y + x
print(result2)


# In[ ]:





# In[ ]:





# In[5]:


#Timing your code


# In[6]:


import timeit


# In[7]:


'0-1-2-3-....-99'


# In[8]:


"-".join(str(n) for n in range(100))


# In[12]:


timeit.timeit("'-'.join(str(n) for n in range(100))", number =10000)


# In[13]:


"-".join([str(n) for n in range(100)])


# In[14]:


timeit.timeit("'-'.join([str(n) for n in range(100)])", number=10000)


# In[16]:


timeit.timeit("'-'.join(map(str,range(100)))", number=10000)


# In[17]:


get_ipython().run_line_magic('timeit', "'-'.join(map(str,range(100)))")


# In[18]:


get_ipython().run_line_magic('timeit', "'-'.join(str(n) for n in range(100))")


# In[19]:


get_ipython().run_line_magic('timeit', "'-'.join([str(n) for n in range(100)])")


# In[ ]:




