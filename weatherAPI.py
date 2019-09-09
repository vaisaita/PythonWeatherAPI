#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import requests


# In[11]:


response=requests.get("http://api.open-notify.org/iss-now.json")


# In[12]:


response.status_code


# In[13]:


parameters = {"lat": 40.71, "lon": -74}


# In[14]:


response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)


# In[15]:


print(response.content)


# In[16]:


response1=requests.get("https://samples.openweathermap.org/data/2.5/weather?zip=94040,us&appid=b6907d289e10d714a6e88b30761fae22")


# In[17]:


print(response1.content)


# In[18]:


arr= response1.content


# In[19]:


arr


# In[20]:


arr.keys


# In[21]:


arr[arr="rain"]


# In[22]:


import json


# In[23]:


arr2=json.loads(arr)


# In[24]:


arr2


# In[26]:


data=arr2['weather']
print(data)


# In[27]:


import csv


# In[31]:


weather_data = open('weatherTest2.csv', 'w')


# In[32]:


csvwriter = csv.writer(weather_data)

count = 0

for id in data:

      if count == 0:

             header = id.keys()

             csvwriter.writerow(header)

             count += 1

      csvwriter.writerow(id.values())

weather_data.close()


# In[ ]:




