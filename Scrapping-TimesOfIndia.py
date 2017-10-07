# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 11:10:18 2017

@author: Utkarsh_Utsava
"""

# Import Basic packages
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

# Initialize url for Times of India

base_url= "https://timesofindia.indiatimes.com"

page= urlopen(base_url)
soup= BeautifulSoup(page, 'html.parser')

top_news_extract= soup.find('ul', attrs={'class': 'list8'})
top_news= top_news_extract.text.strip().split('\n')

latest_news_extract=soup.find('ul',attrs={'class':'list9'})
latest_news= latest_news_extract.text.strip().split('\n')

print('The top news are listed below : \n', top_news)
print('The Latest news are listed below : \n', latest_news)



top_news= pd.DataFrame(top_news, columns= ['Top News'])
latest_news= pd.DataFrame(latest_news, columns= ['Latest News'])
news= pd.concat([latest_news, top_news], axis=1)
news= news[news['Top News'] != '']
news= news[news['Latest News']!='']
news= news.reset_index(drop=True)
News=news.to_excel('News.xlsx', sheet_name='News of the Hour')
