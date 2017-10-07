# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 09:10:43 2017

@author: Utkarsh_Utsava
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

base_url= "http://www.imdb.com/movies-in-theaters/?ref_=cs_inth"

page= urlopen(base_url)
soup= BeautifulSoup(page, 'html.parser')

title= []
duration= []
director= []




# Find all movies in the list
for name in soup.find_all('h4',attrs={'itemprop': 'name'}):
    title.append(name.text.strip())


# Find duration of extracted movies 
for time in soup.find_all('time',attrs={'itemprop': 'duration'}):
    duration.append(time.text.strip())
    


title= pd.DataFrame(title, columns=['Title'])
duration= pd.DataFrame(duration, columns= ['Duration'])


data= pd.concat([title, duration], axis=1)

Movies= data.to_excel('Movies.xlsx', sheet_name='This Week Movie')



    

    
    
    
    
    
