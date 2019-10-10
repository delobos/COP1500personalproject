#!/usr/bin/env python
# coding: utf-8

# In[1]:


mylist =[1,2,3]


# In[2]:


myset = set()


# In[3]:


type(myset)


# In[4]:


type(mylist)


# In[5]:


class Sample():
    pass


# In[6]:


my_sample = Sample()


# In[7]:


type(my_sample)


# In[8]:


class Dog():
        def __init__(self, breed):
            self.breed = breed


# In[9]:


my_dog = Dog()


# In[10]:


my_dog = Dog(breed= 'Lab')


# In[11]:


type(my_dog)


# In[12]:


my_dog.breed


# In[13]:


class Dog():
        def __init__(self, breed):
            
            #Attributes
            #We take in the argument
            #Assignit usinf self.attribute_name
            self.breed = breed


# In[14]:


my_dog = Dog(breed = 'Huskie')


# In[15]:


my_dog.breed


# In[16]:


class Dog():
        def __init__(self, breed, name, spots):
            
            #Attributes
            #We take in the argument
            #Assignit usinf self.attribute_name
            self.breed = breed
            self.name = name
            #Expect Boolean
            self.spots = spots


# In[17]:


my_dog = Dog(breed = 'Lab', name = 'Sammy', spots = False)


# In[20]:


my_dog.breed


# In[21]:


my_dog.name


# In[23]:


my_dog.spots


# In[ ]:





# In[30]:


#Class object Attributes and Methods


# In[32]:


class Dog():
        #Class object attribute
        #Same for any instance of a class
        species = 'Mammal'
        
        def __init__(self, breed, name, spots):
            
            #Attributes
            #We take in the argument
            #Assignit usinf self.attribute_name
            self.breed = breed
            self.name = name
            
            #Expect Boolean
            self.spots = spots


# In[33]:


my_dog = Dog(breed = 'Lab', name = 'Sam', spots = False)


# In[34]:


my_dog.species


# In[35]:


class Dog():
        #Class object attribute
        #Same for any instance of a class
        species = 'Mammal'
        
        def __init__(self, breed, name):
            
            #Attributes
            #We take in the argument
            #Assignit usinf self.attribute_name
            self.breed = breed
            self.name = name
        
        #Operations/Actions ---> Methods
        def bark(self):
            print('Woof!')


# In[36]:


my_dog = Dog('Lab', 'Sam')


# In[39]:


#methods need to be executed so they need()
my_dog.bark


# In[40]:


my_dog.bark()


# In[51]:


#Typically methods will use information from the object themselves


class Dog():
        #Class object attribute
        #Same for any instance of a class
        species = 'Mammal'
        
        def __init__(self, breed, name):
            
            #Attributes
            #We take in the argument
            #Assignit usinf self.attribute_name
            self.breed = breed
            self.name = name
        
        #Operations/Actions ---> Methods
        def bark(self,number):
            print('Woof! My name is {} and the number is {}!'.format(self.name,number))


# In[52]:


my_dog = Dog('Lab','Frankie')


# In[53]:


my_dog.bark()


# In[54]:


my_dog.bark(23)


# In[ ]:





# In[ ]:





# In[61]:


class Circle():
    
    #Class object Attribute
    pi = 3.14
    
    def __init__(self,radius=1):
        
        self.radius = radius
        self.area = radius * radius * self.pi
        
    #method
    def get_circumference(self):
        return self.radius * self.pi * 2


# In[68]:


#You can also override the assigned arguement, in this case radius = 1
#by putting an arguement in Circle()
my_circle= Circle(12)


# In[69]:


my_circle.pi


# In[70]:


my_circle.radius


# In[71]:


my_circle.get_circumference()


# In[72]:


my_circle.area


# In[ ]:




