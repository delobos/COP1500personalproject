#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Collections module#


# In[3]:


#counter
from collections import Counter


# In[4]:


l = [1,1,1,1,112,2,2,2,2,2,3,3,3,4,4,4,5,5,5]

Counter(l)


# In[5]:


s = 'assssvavavasvabsbsbba'

Counter(s)


# In[6]:


s = 'How many times does each word show up in this sentence word word show up up shoe'


# In[7]:


words = s.split()

Counter(words)


# In[8]:


c = Counter(words)


# In[9]:


c.most_common(2)


# In[10]:


sum(c.values())


# In[ ]:





# In[11]:


#Defaultdict#


# In[12]:


from collections import defaultdict


# In[14]:


d = {'k1':1}


# In[15]:


d['k2']


# In[16]:


d['k1']


# In[17]:


d = defaultdict(object)


# In[18]:


d['one']


# In[19]:


for item in d:
    print(item)


# In[20]:


d = defaultdict(lambda : 0)


# In[21]:


d['one']


# In[24]:


d['two'] = 2


# In[25]:


d


# In[ ]:





# In[26]:


#Ordereddict#


# In[28]:


d = {}

d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5


# In[29]:


d


# In[31]:


for k,v in d.items():
    print(k,v)


# In[32]:


from collections import OrderedDict


# In[33]:


d = OrderedDict()


# In[34]:


d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5


# In[35]:


for k,v in d.items():
    print(k,v)


# In[36]:


d1 = {}

d1['a']= 1
d1['b']= 2

d2 = {}

d2['b']= 2
d2['a']= 1


# In[37]:


d1 == d2


# In[38]:


d1 = OrderedDict()

d1['a']= 1
d1['b']= 2

d2 = OrderedDict()

d2['b']= 2
d2['a']= 1


# In[39]:


d1 == d2


# In[ ]:





# In[40]:


#namedtuple#


# In[41]:


t = (1,2,3)


# In[42]:


t[0]


# In[43]:


from collections import namedtuple


# In[44]:


Dog = namedtuple('Dog',"age breed name")


# In[45]:


sam = Dog(age = 2, breed = 'lab', name = 'Sam')


# In[46]:


sam


# In[47]:


sam.age


# In[48]:


sam[0]


# In[ ]:





# In[49]:


Cat = namedtuple("Cat", "fur claws name")


# In[50]:


c = Cat(fur ='fuzzy', claws=False, name= 'kitty')


# In[51]:


c


# In[52]:


c.name


# In[53]:


c.claws


# In[ ]:




