#!/usr/bin/env python
# coding: utf-8

# In[1]:


def func():
    return 1


# In[2]:


func()


# In[3]:


def hello():
    return 'Hello!'


# In[4]:


hello


# In[5]:


hello()


# In[6]:


greet = hello


# In[7]:


greet()


# In[8]:


hello()


# In[9]:


del hello


# In[10]:


hello()


# In[11]:


greet()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[1]:


def hello(name="Jose"):
    print("Hello function has been executed")


# In[2]:


hello()


# In[3]:


def hello(name="Jose"):
    print("Hello function has been executed")
    
    def greet():
        return '\t This is the greet function inside hello'


# In[4]:


hello()


# In[5]:


def hello(name="Jose"):
    print("Hello function has been executed")
    
    def greet():
        return '\t This is the greet function inside hello'
    
    print(greet())


# In[6]:


hello()


# In[7]:


def hello(name="Jose"):
    print("Hello function has been executed")
    
    def greet():
        return '\t This is the greet function inside hello'
    
    def welcome():
        return "\t This is welcome() inside hello"
    
    print(greet())
    print(welcome())


# In[8]:


hello()


# In[9]:


greet()


# In[10]:


def hello(name="Jose"):
    print("Hello function has been executed")
    
    def greet():
        return '\t This is the greet function inside hello'
    
    def welcome():
        return "\t This is welcome() inside hello"
    
    print("I am going to return a function!")
    
    if name == "Jose":
        return greet
    else:
        return welcome


# In[11]:


my_new_func = hello("Jose")


# In[12]:


my_new_func


# In[13]:


my_new_func()


# In[14]:


print(my_new_func())


# In[15]:


def cool():
    
    def super_cool():
        return "I am very cool"
    
    return super_cool


# In[16]:


some_func = cool()


# In[17]:


some_func


# In[18]:


some_func()


# In[ ]:





# In[ ]:





# In[ ]:





# In[1]:


def hello():
    return "hi Jose!"


# In[2]:


def other(some_def_func):
    print('Other code runs here!')
    print(some_def_func())


# In[3]:


other(hello)


# In[ ]:





# In[ ]:





# In[ ]:





# In[4]:


def new_decorator(original_func):
    
    def wrap_func():
        
        print("Some extra code before original function")
    
        original_func()
        
        print("some extra code, after the original function!")
    
    return wrap_func


# In[5]:


def func_needs_decorator():
    print("I want to be decorated!!")


# In[6]:


func_needs_decorator()


# In[7]:


decorated_func = new_decorator(func_needs_decorator)


# In[8]:


decorated_func()


# In[10]:


@new_decorator
def func_needs_decorator():
    print("I want to be decorated!!") 


# In[11]:


func_needs_decorator()


# In[12]:


#@new_decorator
def func_needs_decorator():
    print("I want to be decorated!!") 


# In[13]:


func_needs_decorator()


# In[ ]:




