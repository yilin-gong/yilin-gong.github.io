#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
data = pd.read_csv('denver-1.nov.csv')


# In[2]:


data.head()


# In[120]:


data['days'] = pd.to_datetime(data['date']).map(lambda x: x.weekday())


# In[121]:


list1 = []
for n,i in enumerate(data['arrest_made']):
    if i==True:
        
        list1.append(data.loc[n,'days'])



# In[122]:



for i in range(7):

    print(i, list1.count(i))


# In[127]:


import altair as alt
alt.data_transformers.disable_max_rows()
alt.Chart(data).mark_bar().encode(alt.X('days:N'),y='count()',color='arrest_made',tooltip=['count()','arrest_made'])


# In[ ]:




