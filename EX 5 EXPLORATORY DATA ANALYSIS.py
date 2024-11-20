#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#EX 5 EXPLORATORY DATA ANALYSIS
#REG NO: 230701262
#STUDENT NAME: RAMAYA SREEEVARSHINI
#DATE:03/09/2024

import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline #especially for jupiter notebook')


# In[5]:


tips=sns.load_dataset('tips')


# In[6]:


tips.head


# In[7]:


tips.head()


# In[8]:


sns.displot(tips.total_bill,kde=True)


# In[9]:


sns.displot(tips.total_bill,kde=False)


# In[10]:


sns.displot(tips.total_bill) #default kde=False ,where kde stands for "Kernal Density Estimation"


# The total_bill is left skewed

# In[11]:


sns.displot(tips.tip,kde=True)


# In[12]:


sns.displot(tips.sex,kde=True)


# In[13]:


sns.displot(tips.smoker,kde=True)


# In[14]:


sns.displot(tips.day,kde=True)


# In[15]:


sns.displot(tips.time,kde=True)


# In[17]:


sns.displot(tips['size'],kde=True)


# In[21]:


sns.jointplot(x=tips.tip,y=tips.total_bill) #does not have kde argument


# In[24]:


sns.jointplot(x=tips.tip,y=tips.total_bill,kind='reg')   # here "reg" refers to "regression line"


# This jointplot shows the distribution

# In[22]:


sns.jointplot(x=tips.tip,y=tips.sex)


# In[ ]:





# In[26]:


sns.jointplot(x=tips.tip,y=tips['size'],kind='reg') 


# In[27]:


sns.jointplot(x=tips.tip,y=tips.total_bill,kind='hex')


# In[28]:


sns.pairplot(tips) #does not give plot for categorical data of type string


# In[29]:


tips.time.value_counts()


# In[30]:


tips.sex.value_counts()


# In[31]:


tips.total_bill.value_counts()


# In[32]:


tips.tip.value_counts()


# In[33]:


sns.pairplot(tips,hue='time') # This is good for ploting all numerical data with comparision to categorical data


# In[34]:


sns.pairplot(tips,hue='total_bill')


# In[35]:


sns.pairplot(tips,hue='tip')


# In[36]:


sns.pairplot(tips,hue='size')


# In[37]:


sns.pairplot(tips,hue='day')


# In[38]:


sns.heatmap(tips.corr(numeric_only=True),annot=True)


# In[39]:


sns.heatmap(tips.corr(numeric_only=True),annot=False)

