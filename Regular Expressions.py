#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re


# In[2]:


patterns = ['term1', 'term2']


# In[6]:


text = 'this is a string with term1, but not the other term'


# In[7]:


re.search('hello','hello world')


# In[ ]:





# In[8]:


for pattern in patterns:
    print("Searching for '%s' in: \n'%s'" % (pattern,text))
    
    #check for match
    if re.search(pattern, text):
        print('\n')
        print("match was found. \n")
    else:
        print('\n')
        print("No match was found. \n")


# In[9]:


print(re.search('h', 'w'))


# In[10]:


match = re.search(patterns[0], text)


# In[11]:


type(match)


# In[12]:


match.start()


# In[13]:


match.end()


# In[14]:


split_term = '@'

phrase = "What is your email? is it hello@gmail.com?"


# In[15]:


re.split(split_term, phrase)


# In[16]:


re.findall('match', 'here is one match, here is another match')


# In[ ]:





# In[22]:


def multi_re_find(patterns, phrase):
    
    '''
    takes in a list of regex patterns
    prints a list of all matcher
    '''
    for pattern in patterns:
        print("Searching the phrase using the re check: %r" %pattern)
        print(re.findall(pattern,phrase))
        print('\n')


# In[23]:


test_phrase ='sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'

test_patterns =[ 'sd*', 'sd+', 'sd?', 'sd{3}', 'sd{2,3}']

multi_re_find(test_patterns, test_phrase)


# In[24]:


test_phrase ='sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'

test_patterns =[ '[sd]', 's[sd]+']

multi_re_find(test_patterns, test_phrase)


# In[ ]:





# In[25]:


test_phrase = 'This is a string! But it has punctuation. How can we remove it?'


# In[28]:


re.findall('[^!.? ]+', test_phrase)


# In[ ]:





# In[31]:


test_phrase = 'This is an example sentence. Lets see if we can find some letters.'

test_patterns = [ "[a-z]+", "[A-Z]+", "[a-zA-Z]+", "[A-Z][a-z]+"]

multi_re_find(test_patterns, test_phrase)


# In[ ]:





# In[33]:


test_phrase = "This is a string with some numbers 1233 and a symbol #hashtag"

test_patterns = [r'\d+', r'\D+', r'\s+', r'\S+', r'\w+', r'\W+']

multi_re_find(test_patterns, test_phrase)


# In[ ]:




