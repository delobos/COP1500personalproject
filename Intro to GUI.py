#!/usr/bin/env python
# coding: utf-8

# In[2]:


from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets


# In[7]:


def func(x):
    return x


# In[9]:


interact(func, x=10)


# In[10]:


def func(x):
    return x


# In[12]:


interact(func, x=True)

def func(x):
    return x
# In[13]:


interact(func, x= 'Hello')


# In[15]:


@interact(x=True, y=1.0)
def g(x,y):
    return (x,y)


# In[16]:


@interact(x=True, y=fixed(1.0))
def g(x,y):
    return (x,y)


# In[17]:


interact(func, x=widgets.IntSlider(min=-100, max=100, step=1, value=0))


# In[18]:


interact(func, x=(-100,100,1))


# In[19]:


interact(func, x=(-100.0,100.0,.1))


# In[20]:


@interact(x=(0.0, 20.0, .05))
def h(x=5):
    return x


# In[21]:


interact(func, x= ['Hello', 'option 2', 'option 3'])


# In[23]:


interact(func, x= {'one':10, 'two': 20})


# In[24]:


from IPython.display import display

def f(a,b):
    display(a+b)
    return a+b


# In[26]:


w = interactive(f,a=10,b=20)


# In[27]:


type(w)


# In[28]:


w.children


# In[29]:


display(w)


# In[ ]:





# In[31]:


#GUI widget basics#


# In[32]:


import ipywidgets as widgets


# In[34]:


w = widgets.IntSlider()


# In[35]:


from IPython.display import display


# In[36]:


display(w)


# In[37]:


display(w)


# In[38]:


w.close()


# In[39]:


w = widgets.IntSlider()
display(w)


# In[41]:


w.value


# In[42]:


w.value =50


# In[43]:


w.keys


# In[44]:


w.max = 2000


# In[45]:


display(w)


# In[49]:


a = widgets.FloatText()
b = widgets.FloatSlider()

display(a,b)

mylink = widgets.jslink((a,'value'),(b,'value'))


# In[50]:


a = widgets.FloatText()
b = widgets.FloatSlider()

display(a,b)

mylink = widgets.jslink((a,'value'),(b,'max'))


# In[51]:


mylink.unlink()


# In[ ]:





# In[58]:


#widget styling and layout


# In[59]:


import ipywidgets as widgets
from IPython.display import display


# In[61]:


w = widgets.IntSlider()
display(w)


# In[62]:


w.layout.margin = 'auto'
w.layout.height = '75px'


# In[65]:


x = widgets.IntSlider(value = 15, description = "New slider")
display(x)


# In[66]:


x.layout = w.layout


# In[70]:


widgets.Button(description = 'Ordinary Button', button_style = "info")


# In[ ]:





# In[ ]:





# In[ ]:





# In[72]:


b1 = widgets.Button(description = 'Custom Color')
b1.style.button_color = 'lightgreen'
b1


# In[75]:


b2 = widgets.Button(description = 'NEW')
b2.style = b1.style


# In[76]:


b2


# In[80]:


s1 = widgets.IntSlider(description = 'My Handle')
s1.style.handle_color = 'purple'


# In[81]:


s1


# In[79]:


s1.style.keys


# In[ ]:




