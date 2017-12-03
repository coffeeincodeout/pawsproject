#([\d]+)\s(years)
#([\d]+)\s(pounds)

import requests
import lxml.html
import re
from scraper.db import Database
from lxml.cssselect import CSSSelector

def animals(url):
    base_url = 'petharbor.com/'
    load_url = requests.get(url)
    page_html = lxml.html.fromstring(load_url.text)


    for num in range(2, 12):
        a = str(num)
        name = page_html.xpath('//*[@id="frmResults"]/table[3]/tr[' + a + ']/td[2]/text()[1]')
        des = page_html.xpath('//*[@id="frmResults"]/table[3]/tr[' + a + ']/td[3]/text()')
        des2 = page_html.xpath('//*[@id="frmResults"]/table[3]/tr[' + a + ']/td[3]/text()[2]')
        image = page_html.xpath('//*[@id="frmResults"]/table[3]/tr[' + a + ']/td[1]/a/img/@src')

        for n1, d1, d2, i1 in zip(name, des, des2, image):
            years = re.search('([\d]+)\s(years)', d2)
            pounds = re.search('([\d]+)\s(pounds)', d2)

            if (years):
                y1 = years.group()
            else:
                y1 = ""
            if (pounds):
                p1 = pounds.group()
            else:
                p1 = ""
                
            db.insert(n1, d1, y1, p1, base_url + i1)
            db.commit()

            
            
            #print("name:", n1)
            #print("des:", d1)
            #if (years):
            #    print("years:", years.group())
            #if (pounds):
            #    print("pounds:", pounds.group())
            #print("image:", base_url + i1)




url = 'http://petharbor.com/results.asp?searchtype=ADOPT&start=3&friends=0&samaritans=0&nosuccess=0&rows=10&imght=' \
      '120&imgres=thumb&tWidth=200&view=sysadm.v_miad&text=000000&fontface=arial&fontsize=10&col_bg=99b5c9&col_bg2=' \
      'e7eec4&SBG=026BA9&zip=33183&miles=10&shelterlist=%27MIAD%27&atype=&where=type_DOG&PAGE='

user_login = "dbname='pawsproject' user='root' host='localhost' password='motifes6'"
db = Database()
db.connection(user_login)
db.cursor()

for n in range(1, 38):
    new_url = url + str(n)
    animals(new_url )

db.close()