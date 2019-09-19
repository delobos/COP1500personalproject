#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Map function


# In[2]:


def sqre(num):
    return num**2


# In[3]:


mynums= [1,2,3,4,5]


# In[5]:


for  item in map(sqre,mynums):
    print(item)


# In[6]:


list(map(sqre,mynums))


# In[17]:


def splicer(mystring):
    if len(mystring)%2 == 0:
        return "even"
    else:
        return mystring.upper()[0]


# In[18]:


names = ['andy', 'eve', 'sally']


# In[19]:


list(map(splicer,names))


# In[20]:


#Filter function


# In[21]:


def check_even(num):
    return num%2 == 0


# In[22]:


mynums = [1,2,3,4,5,6]


# In[23]:


list(filter(check_even,mynums))


# In[24]:


for n in filter(check_even, mynums):
    print(n)


# In[25]:


#Lambda Expressions


# In[26]:


def sqre(num):
    result = num ** 2
    return result


# In[28]:


sqre(3)


# In[29]:


#simplify function


# In[30]:


def sqre(num): return num ** 2


# In[31]:


#Now lambda Expression style


# In[34]:


list(map(lambda num:num ** 2, mynums))


# In[35]:


list(filter(lambda num:num%2 == 0,mynums))


# In[36]:


names


# In[37]:


list(map(lambda name:name[0], names))


# In[38]:


list(map(lambda name:name[::-1], names))


# In[39]:


#Scope


# In[40]:


x = 25

def printer():
    x = 50
    return x


# In[41]:


print(x)


# In[42]:


print(printer())


# In[43]:


##LEGB rule (Local, Enclosing function local, Global, Built-in)##


# In[48]:


#LOCAL
lambda num:num**2

#GLOBAL
name = 'THIS IS A GLOBAL STRING'


def greet():
    #ENCLOSING FUNCTION LOCA
    name = 'SAMMY'
    
    def hello():
        #LOCAL
        name = "I AM A LOCAL"
        print('Hello '+ name)
    hello()
    
greet()


# In[52]:


x = 50

def func(x):
    print(f'X is {x}')
    
    


# In[53]:


func(x)


# In[54]:


x = 50

def func(x):
    print(f'X is {x}')
    
    #LOCAL REASSIGNMENT
    x = 200
    print(f'I JUST LOCALLY CHANGED X to {x}')


# In[55]:


func(x)


# In[56]:


print(x)


# In[59]:


x = 50

def func():
    global x
    print(f'X is {x}')
    
        #LOCAL REASSIGNMENT ON A GLOBAL VARIABLE!
    x = 'NEW VALUE'
    print(f'I JUST LOCALLY CHANGED GLOBAL X to {x}')


# In[60]:


print(x)


# In[62]:


func()


# In[63]:


print(x)


# In[ ]:





# In[ ]:




