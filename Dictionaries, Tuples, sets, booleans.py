#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dictionaries


# In[2]:


my_dict = {'key1': 'value1', 'key2':'value2'}


# In[3]:


my_dict


# In[5]:


my_dict['key1']


# In[6]:


prices_lookup = {'apple' : 2.99, 'oranges': 1.99, 'milk': 5.80}


# In[7]:


prices_lookup['apple']


# In[8]:


d = {'k1':123, 'k2':[0,1,2], 'k3': {'insidekey':100}}


# In[9]:


d['k2']


# In[10]:


d['k3']


# In[11]:


d['k3']['insidekey']


# In[12]:


d['k2']


# In[13]:


d['k2'][2]


# In[14]:


d = {'key1': ['a','b','c']}


# In[15]:


d


# In[16]:


mylist = d["key1"]


# In[17]:


mylist


# In[19]:


letter = mylist[2]


# In[20]:


letter


# In[22]:


letter.upper()


# In[25]:


d['key1'][2].upper()


# In[26]:


d = {'k1':100, "k2":200}


# In[27]:


d


# In[28]:


d['k3'] = 300


# In[29]:


d


# In[30]:


d['k1'] = 'NEW VALUE'


# In[31]:


d


# In[32]:


d = {'k1': 100, 'k2': 200, 'k3': 300}


# In[33]:


d.keys()


# In[34]:


d.values()


# In[35]:


d.items()


# In[ ]:





# In[1]:


# Tuples


# In[2]:


t = (1,2,3)


# In[3]:


mylist = [1,2,3]


# In[4]:


type(t)


# In[5]:


type(mylist)


# In[6]:


len(t)


# In[7]:


t = ('one', 2)


# In[8]:


t[0]


# In[9]:


t[-1]


# In[10]:


t = ('a','a','b')


# In[12]:


t.count('a')


# In[13]:


t.index('a')


# In[15]:


t.index('b')


# In[16]:


t


# In[17]:


mylist


# In[18]:


mylist[0] = "NEW"


# In[19]:


mylist


# In[20]:


t[0] = 'NEW'


# In[21]:


#immutable#


# In[ ]:





# In[22]:


#sets


# In[23]:


myset = set()


# In[24]:


myset


# In[25]:


myset.add(1)


# In[26]:


myset


# In[27]:


myset.add(2)


# In[28]:


myset


# In[29]:


myset.add(2)


# In[30]:


myset


# In[33]:


mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]


# In[34]:


set(mylist)


# In[ ]:





# In[35]:


#Booleans


# In[36]:


True


# In[37]:


true


# In[38]:


False


# In[39]:


false


# In[41]:


type(False)


# In[42]:


1 > 2


# In[43]:


1 == 1


# In[44]:


b = None


# In[ ]:




