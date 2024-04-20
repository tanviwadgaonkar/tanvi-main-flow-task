#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
df=pd.read_csv(r'C:\Users\Tanvi\Downloads\01.Data Cleaning and Preprocessing.csv')


# In[4]:


df


# In[14]:


data=df.drop('ChipRate',axis=1)
data


# In[15]:


da=df.dropna()
da


# In[18]:


df.isna().sum()


# In[20]:


df.fillna(value='xyz')


# In[21]:


df.head()


# In[22]:


df.tail()


# In[24]:


df.fillna(df.mean())


# In[26]:


df.shape


# In[32]:


import matplotlib.pyplot as plt
import pandas as pd
x=df['Observation']
y=df['Y-Kappa']
plt.plot(x,y)
plt.title('Data Analysis')
plt.xlabel('x axis')
plt.ylabel('y Axis')
plt.show()


# In[35]:





# In[ ]:




