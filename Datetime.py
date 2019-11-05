#!/usr/bin/env python
# coding: utf-8

# In[1]:


import datetime


# In[4]:


t = datetime.time(5,25,1)


# In[5]:


print(t)


# In[7]:


t.hour


# In[8]:


t.minute


# In[9]:


t.second


# In[10]:


datetime.time.min


# In[11]:


print(datetime.time.min)


# In[13]:


print(datetime.time.max)


# In[14]:


print(datetime.time.resolution)


# In[15]:


today = datetime.date.today()


# In[16]:


print(today)


# In[18]:


today.timetuple()


# In[19]:


today.year


# In[20]:


today.month


# In[22]:


print(datetime.date.min)


# In[23]:


print(datetime.date.max)


# In[24]:


print(datetime.date.resolution)


# In[25]:


d1 = datetime.date(2019,11,4)
print(d1)


# In[26]:


d2 = d1.replace(year= 2000)


# In[27]:


d2


# In[28]:


d1


# In[29]:


d2


# In[30]:


d1-d2


# In[ ]:




