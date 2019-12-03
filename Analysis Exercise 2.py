#!/usr/bin/env python
# coding: utf-8

# In[118]:


import pandas as pd

Location = "datasets/axisdata.csv"
df = pd.read_csv(Location)
df.head()


# In[86]:


df['Cars Sold'].mean()


# In[51]:


df['Cars Sold'].max()


# In[4]:


df['Cars Sold'].min()


# In[5]:


pd.pivot_table(df, values=['Cars Sold'], index=['Gender'])


# In[6]:


df[df['Cars Sold']>3]['Hours Worked'].mean()


# In[7]:


df['Years Experience'].mean()


# In[8]:


df[df['Cars Sold']>3]['Years Experience'].mean()


# In[9]:


pd.pivot_table(df, values=['Cars Sold'], index=['SalesTraining'])


# In[93]:


df.boxplot (by='SalesTraining', column='Cars Sold')


# In[119]:


plt.scatter(df['Hours Worked'], df['Cars Sold'])

