#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
import re
from time import sleep


# In[2]:


names = []
roles = []
locations = []
nos = []
emails = []


# In[11]:


from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')


# In[12]:


u = UserAgent()
header = {'user-agent':u.chrome}
driver = webdriver.Chrome('/home/sush/Downloads/Compressed/chromedriver_linux64/chromedriver', chrome_options=options)


# In[13]:


alphabet = ['A']
# for i in list(range(65, 91)):
#     alphabet.append(str(chr(i)))


# In[14]:


alphabet


# In[15]:


for i in alphabet:
    driver.get('https://www.lw.com/attorneyBioSearch.aspx?searchIndex={}&peopleViewMode=ListView'.format(i))
    sleep(5)
    try:
        driver.find_element_by_xpath('//div[@id="TopPagerAttorney"]/span/a[3]').click()
    except:
        pass
    sleep(5)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    tempname = soup.find('table', {'id':'PeopleList'}).find_all('a', href=re.compile('/people/'))
    for i in tempname:
        name = i.text.strip()
        role = i.findNext('td').text.strip()
        email = i.findNext('td').findNext('td').text.strip()
        try:
            location = i.findNext('td').findNext('td').findNext('td').find('td', style=re.compile('width')).text.strip()
        except:
            location = 'None'
        try:
            no = i.findNext('td').findNext('td').findNext('td').find('td', text= lambda x: x and x.startswith('+')).text.strip()
        except:
            no = 'None'
        names.append(name)
        roles.append(role)
        emails.append(email)
        locations.append(location)
        nos.append(no)


# In[16]:


df = pd.DataFrame([names, roles,locations, nos, emails]).T
df.columns = ['name', 'Role','location', 'number', 'email']


# In[10]:


df.to_csv('lwnew.csv', index=False)


# In[17]:


df


# In[ ]:




