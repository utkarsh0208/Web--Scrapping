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
SNo= []
SNo.extend(range(1,len(latest_news)+1))
SNo= pd.DataFrame(SNo, columns=['SNo.'])
news= pd.concat([latest_news, top_news, SNo], axis=1)
news= news[news['Top News'] != 'NaN']
news= news[news['Latest News']!='NaN']

News=news.to_excel('News.xlsx', sheet_name='News of the Hour')

"""

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import smtplib
s = smtplib.SMTP(host='smtp.gmail.com', port=25)
s.starttls()
s.login('utkarsh0208@gmail.com', 'utkarsh!0208')

msg = MIMEMultipart()
msg['From']="utkarsh0208@gmail.com"
msg['To']="utkarsh0208@gmail.com"
msg['Subject']="This is hourly news update !!!"
msg.attach(MIMEText("News.xlxs").read())


s.send_message(msg)
s.quit()

"""