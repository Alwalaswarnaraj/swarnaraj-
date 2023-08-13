#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


da=pd.read_csv("D:/python/IRIS.csv")


# In[3]:


da.head()


# In[4]:


col_drop=['0.222222222','0.625','0.06779661','0.041666667']
da.drop(col_drop,axis=1,inplace=True)


# In[5]:


da.head()


# In[6]:


headerlist=['Sepal Length','Sepal Width','Petal Length','Peatal Width','Species']

da.to_csv("IRIS2.csv", header=headerlist, index=False)


# In[7]:


da.head()


# In[8]:


da=pd.read_csv("IRIS2.csv")


# In[9]:


da.head()


# In[10]:


da.shape


# In[11]:


da["Species"].value_counts()


# In[12]:


da.plot(kind='scatter',x='Sepal Length',y='Sepal Width');

plt.show()


# In[13]:


import warnings
from warnings import filterwarnings
filterwarnings('ignore')


# In[14]:


sns.set_style('whitegrid')
sns.FacetGrid(da, hue='Species', size=4)     .map(plt.scatter, 'Petal Length','Peatal Width')    .add_legend()
plt.show()


# In[15]:


sns.set_style('whitegrid')
sns.FacetGrid(da, hue='Species',size=4)    .map(plt.scatter, 'Sepal Length', 'Sepal Width')    .add_legend()
#plt.show


# In[16]:


#da.plot(kind='scatter',x='Sepal Length',y='Sepal Width')
#x=da.Species['setosa']
#fig=plt.plot(x,da,lw=4,color='orange')


# In[17]:


#x=da.iloc[:,[1]].values
#x


# In[18]:


#y=da.iloc[:,2].values
#y


# In[19]:


plt.scatter(x,y)


# In[ ]:


#fig=plt.plot(x,da,lw=4,c='orange')


# In[ ]:


plt.close()
sns.set_style('whitegrid')
sns.pairplot(da,hue='Species', size=3)
plt.show()


# In[ ]:


sns.pairplot(da,hue='Species',size=4)


# In[ ]:


sns.set_style('whitegrid')
sns.FacetGrid(da, hue='Species',size=4)     .map(plt.scatter, 'Peatal Width','Petal Length')    .add_legend()
#plt.show


# In[ ]:


#plt.scatter(da,hue='Species',size=3)


# In[20]:


headerlist=['Sepal Length','Sepal Width','Petal Length','Peatal Width','Species']

da.to_csv("IRIS2.csv", header=headerlist, index=False)


# In[21]:





# In[22]:





# In[ ]:





# In[ ]:





# In[24]:





# In[26]:


#x


# In[27]:





# In[29]:


#y


# In[30]:





# In[ ]:




