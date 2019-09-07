#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().run_cell_magic('writefile', 'myfile.txt', 'Hello this is a text file\nThis is the second line\nThis is the third line')


# In[3]:


myfile = open("myfile.txt")


# In[4]:


myfile = open('whoops_wrong.txt')


# In[5]:


pwd


# In[6]:


myfile = open('myfile.txt')


# In[8]:


myfile.read()


# In[9]:


myfile.read()


# In[10]:


myfile.seek(0)


# In[11]:


myfile.read()


# In[12]:


myfile.seek(0)


# In[13]:


contents = myfile.read()


# In[14]:


contents


# In[15]:


contents


# In[16]:


myfile.seek(0)


# In[17]:


myfile.readlines()


# In[18]:


pwd


# In[22]:


myfile.close()


# In[26]:


with open('myfile.txt') as my_new_file:
    contents = my_new_file.read()


# In[27]:


contents


# In[28]:


with open('myfile.txt',mode = 'r') as myfile:
    contents = myfile.read()


# In[29]:


contents


# In[30]:


with open('myfile.txt',mode = 'w') as myfile:
    contents = myfile.read()


# In[ ]:





# In[32]:


get_ipython().run_cell_magic('writefile', 'my_new_file.txt', 'ONE ON FIRST\nTWO ON SECOND\nTHREE ON THIRD')


# In[33]:


with open("my_new_file.txt", mode = "r") as f:
    print(f.read())


# In[34]:


with open('my_new_file.txt', mode = 'a') as f:
    f.write('FOUR ON FOURTH')


# In[35]:


with open("my_new_file.txt", mode = "r") as f:
    print(f.read())


# In[36]:


with open('dfsdggsd.txt', mode = 'w') as f:
    f.write('I created this file!')


# In[37]:


with open('dfsdggsd.txt', mode = "r") as f:
    print(f.read())


# In[ ]:





# In[ ]:




