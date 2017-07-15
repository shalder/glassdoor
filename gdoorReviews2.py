#!/usr/bin/env python

#!/usr/bin/env python

import requests
from bs4 import  BeautifulSoup
import pandas as pd
from urllib.request import urlopen
from userAgents import user_agents, randomUserAgents
import time

start = time.time()
url = 'https://www.glassdoor.com/Reviews/Snap-Reviews-E671946.htm'
head = randomUserAgents()


def soup(url,headers):
    ''' url = full glassdoor.com/reviews url'''
    session = requests.Session()
    req = session.get(url, headers=headers)
    bs = BeautifulSoup(req.text, 'html.parser')
    return bs


pages = set()
def getPages(url, head):
    ''' Gets a set of ALL "Next Page" hrefs '''
    global pages
    bs = soup(url, head)
    nextPage = bs.find('div',{'class',"flex-grid tbl margTop"})
    for link in nextPage.findAll('a'):
        if 'href' in link.attrs:
            url = 'https://glassdoor.com{}'.format(link.attrs['href'])
            if url not in pages:
            #new page
                pages.add(url)
    #get last page
    for lastPage in nextPage.findAll('li',{'class':'page last'}):
        lastPage = 'https://glassdoor.com{}'.format(lastPage.a['href'])
        getPages(lastPage, head)
    return pages


print(getPages(url, head))
print(start - time.time())
#-11.2422
