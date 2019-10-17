#!/usr/bin/env python
# coding: utf-8

# In[1]:


def  add(n1,n2):
    print(n1+n2)


# In[2]:


add(10,20)


# In[3]:


number1 = 10

number2 = input('please provide a number: ')


# In[6]:


add(number1, number2)
print('something happened')


# In[15]:


try:
    # want to attempt this code
    # may have an error
    result = 10 + 10
except:
    print("Hey it looks like you arent adding correctly")


# In[12]:


result


# In[14]:


try:
    # want to attempt this code
    # may have an error
    result = 10 + '10'
except:
    print("Hey it looks like you arent adding correctly")


# In[17]:


try:
    # want to attempt this code
    # may have an error
    result = 10 + 10
except:
    print("Hey it looks like you arent adding correctly")
else:
    print("add went well!")
    print(result)


# In[ ]:





# In[18]:


try:
    f = open('testfile', 'w')
    f.write('Write a test line')
except TypeError:
    print("there was a type error")
except OSError:
    print("hey you have an OS error")
finally:
    print("I always run")


# In[20]:


try:
    f = open('testfile', 'r')
    f.write('Write a test line')
except TypeError:
    print("there was a type error")
except OSError:
    print("hey you have an OS error")
finally:
    print("I always run")


# In[22]:


try:
    f = open('testfile', 'r')
    f.write('Write a test line')
except TypeError:
    print("there was a type error")
except:
    print("All other exceptions")
finally:
    print("I always run")


# In[23]:


def ask_for_int():
    try:
        result = int(input('please provide number: '))
    except:
        print('That is not a number')
    finally:
        print('end of try/except/finally')


# In[24]:


ask_for_int()


# In[26]:


ask_for_int()


# In[1]:


def ask_for_int():
    while True:
        
        try:
            result = int(input('please provide number: '))
        except:
            print('That is not a number')
            continue
        else:
            print('yes thank you')
            break
        finally:
            print('end of try/except/finally')
            print('i will always run at the end')


# In[2]:


ask_for_int()


# In[3]:


ask_for_int()


# In[ ]:




