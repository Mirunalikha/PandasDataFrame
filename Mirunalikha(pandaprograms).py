#!/usr/bin/env python
# coding: utf-8

# In[1]:


#pandas
import pandas as pd
df=pd.DataFrame()
print(df)


# In[4]:


import pandas as pd
emp=pd.Series(['Miru','Yasir','Niha','captainAmerica'])
id=pd.Series([10,20,30,40])
frame={'Emp':emp,'ID':id}
result=pd.DataFrame(frame)
print("\nSeries to DataFrame\n")
print(result)


# In[5]:


#excration
print("\n Extracting the second row \n")
print(result['Emp'])


# In[6]:


#adding a new colomn
result['Age']=pd.Series([20,18,30,50])
print(result)


# In[7]:


#delete exist colomn
del result['Age']
print(result)


# In[8]:


#slicing
print("Slice Row\n",result[1:3])


# In[9]:


print("\nExtracting the Second Row\n")
print(result.loc[1])


# In[ ]:




