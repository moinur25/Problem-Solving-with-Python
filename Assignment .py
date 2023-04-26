#!/usr/bin/env python
# coding: utf-8

# # ease use the three data sets about US states and their populations: (1) state-areas.csv, (2) state-abbrevs.csv, and (3) state-population.csv during the lecture.Find out the density of the under-18 population densityfrom 1990 to 2013 for every states.

# In[17]:


import pandas as pd

# read the three datasets
state_areas = pd.read_csv('state-areas.csv')
state_abbrevs = pd.read_csv('state-abbrevs.csv')
state_populations = pd.read_csv('state-population.csv')


# In[18]:


state_areas.head()


# In[19]:


state_abbrevs.head()


# In[20]:


state_populations.head()


# In[112]:


merged = pd.merge(state_areas, state_abbrevs, how='outer', on='state')


# In[113]:


merged.head()


# In[115]:


merged = pd.merge(merged, state_populations, how='outer', left_on='abbreviation', right_on='state/region')


# In[122]:


merged.head()


# In[117]:


merged = merged.dropna()


# In[118]:


merged.count()


# In[127]:


merged = merged[(merged['year'] >= 1990) & (merged['year'] <= 2013)]


# In[132]:


merged.head(100)


# In[133]:


merged = merged[merged['ages'] == 'under18']


# In[135]:


merged.head()


# In[138]:


merged['density'] = merged['population'] / merged['area (sq. mi)']


# In[152]:


merged.head(100)


# In[151]:


print(merged['density'])


# In[142]:


print(merged[['state', 'year', 'density']])

