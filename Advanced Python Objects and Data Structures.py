#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Advanced Numbers


# In[2]:


hex(12)


# In[3]:


hex(512)


# In[4]:


bin(1234)


# In[5]:


bin(128)


# In[6]:


bin(512)


# In[7]:


pow(2,4)


# In[8]:


pow(2,4,3)


# In[9]:


abs(-2354)


# In[10]:


round(3.1)


# In[11]:


round(3.9)


# In[12]:


round(3.141592,2)


# In[13]:





# In[14]:


#Advanced strings


# In[15]:


s = 'Hello World'


# In[16]:


s.upper()


# In[17]:


s.capitalize()


# In[18]:


s.lower()


# In[19]:


s.count('o')


# In[20]:


s.find('o')


# In[21]:


s


# In[22]:


s.center(20,'z')


# In[23]:


print('hello\thi')


# In[24]:


s = 'hello'


# In[25]:


s.isalnum()


# In[26]:


s.isalpha()


# In[27]:


s.islower()


# In[28]:


s


# In[29]:


s.isspace()


# In[30]:


s.isupper


# In[31]:


s.isupper()


# In[32]:


s.isspace()


# In[33]:


s.endswith('o')


# In[34]:


'HELLO'.isupper()


# In[35]:


s.split('e')


# In[36]:


s = 'hiiihihihhiihhi'


# In[37]:


s.split('i')


# In[38]:


s.partition('i')


# In[ ]:





# In[39]:


#Advanced Sets


# In[40]:


s = set()


# In[41]:


s.add(1)


# In[42]:


s.add(2)


# In[43]:


s


# In[44]:


s.add(2)


# In[45]:


s


# In[46]:


s.clear()


# In[47]:


s


# In[48]:


s = {1,2,3}


# In[49]:


sc = s.copy()


# In[50]:


sc


# In[51]:


s.add(4)


# In[52]:


s


# In[53]:


sc


# In[54]:


s.difference(sc)


# In[55]:


a1 = {1,2,3}
a2 = {1,4,5}


# In[56]:


a1.difference_update(a2)


# In[57]:


a1


# In[58]:


a2


# In[59]:


s.discard(2)


# In[60]:


s


# In[66]:


s1 = {1,2,3}
s2 = {1,2,4}


# In[67]:


s1.intersection(s2)


# In[68]:


s1


# In[69]:


s1.intersection_update(s2)


# In[70]:


s1


# In[71]:


s1 = {1,2}
s2 = {1,2,4}
s3 = {5}


# In[73]:


s1.isdisjoint(s2)


# In[74]:


s1.isdisjoint(s3)


# In[75]:


s1


# In[76]:


s2


# In[77]:


s1.issubset(s2)


# In[78]:


s2.issuperset(s1)


# In[79]:


s1.symmetric_difference(s2)


# In[80]:


s1.symmetric_difference_update(s2)


# In[81]:


s1


# In[82]:


s1.union(s2)


# In[83]:


s1.update(s2)


# In[84]:


s1


# In[ ]:





# In[85]:


#Advanced dictionaries


# In[86]:


d = {'k1':1, 'k2':2}


# In[87]:


{x:x**2 for x in range(10)}


# In[89]:


{k:v**2 for k,v in zip(['a','b'],range(2))}


# In[90]:


for k in d.items():
    print(k)


# In[94]:


for k in d.values():
    print(k)


# In[95]:


for k in d.keys():
    print(k)


# In[ ]:





# In[97]:


#Advanced lists


# In[98]:


l = [1,2,3]


# In[99]:


l.append(4)


# In[100]:


l


# In[101]:


l.count(10)


# In[102]:


l.count(1)


# In[104]:


x = [1,2,3]
x.append([4,5])
print(x)


# In[105]:


x = [1,2,3]
x.extend([4,5])
print(x)


# In[106]:


l


# In[107]:


l.index(3)


# In[108]:


l.index(7)


# In[109]:


l.insert(2,'INSERTED')


# In[110]:


l


# In[111]:


ele = l.pop()


# In[112]:


l


# In[113]:


ele


# In[114]:


l.pop(0)


# In[115]:


l


# In[116]:


l.remove('INSERTED')


# In[118]:


l


# In[119]:


l = [1,2,3,4,3]


# In[120]:


l.remove(3)


# In[121]:


l


# In[122]:


l.reverse()


# In[123]:


l


# In[124]:


l.sort()


# In[125]:


l


# In[ ]:




