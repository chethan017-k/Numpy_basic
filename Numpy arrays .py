#!/usr/bin/env python
# coding: utf-8

# ## Numpy arrays 

# In[1]:


my_list = [1,2,3,4,5,6,7,8,9]


# In[2]:


import numpy as np


# In[3]:


myarr = np.array(my_list)


# In[4]:


myarr


# In[5]:


my_matrix = ([1,2,3],[4,5,6],[7,8,9])


# In[6]:


my_arrymat= np.array(my_matrix)


# In[7]:


my_arrymat


# In[8]:


np.arange(0,101,5)


# In[12]:


np.zeros((5,2))


# In[13]:


np.zeros (5)


# In[14]:


np.linspace(0,10,3)


# In[16]:


np.eye(4)


# ## random distribution of data

# In[17]:


np.random.rand(1)


# In[18]:


np.random.rand(10,5)


# In[19]:


np.random.randn(2,5)


# In[20]:


np.random.randint(0,101,10)


# In[23]:


np.random.seed(42)
np.random.rand(5)


# In[29]:


a=np.random.rand(1,20)


# In[32]:


a.reshape(5,4)


# In[33]:


a.max()


# In[35]:


a.min()


# In[36]:


a.argmax()


# In[37]:


a.argmin()


# In[38]:


a.dtype


# In[ ]:




