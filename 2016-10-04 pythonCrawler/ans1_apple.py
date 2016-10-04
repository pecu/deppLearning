# -*- coding: utf-8 -*-
from lxml import etree
import requests
import pandas as pd

###  蘋果日報基金會 :
targeturl = "http://search.appledaily.com.tw/charity/projlist/"

res = requests.get(targeturl)
res.encoding = 'utf8'
root = etree.fromstring(res.content, etree.HTMLParser())
 
### 編號 :
#------------------------------------------------
#//*[@id="inquiry3"]/table/tbody/tr[3]/td[1]
#//*[@id="inquiry3"]/table/tbody/tr[4]/td[1]
#...
#//*[@id="inquiry3"]/table/tbody/tr[22]/td[1]
#------------------------------------------------
### 報導標題 :
#------------------------------------------------
#//*[@id="inquiry3"]/table/tbody/tr[3]/td[2]/a
#//*[@id="inquiry3"]/table/tbody/tr[4]/td[2]/a
#...
#//*[@id="inquiry3"]/table/tbody/tr[22]/td[2]/a
#------------------------------------------------

idlist = [] ; titlelist = []
for num in range(3,23):
    xpath = '//*[@id="inquiry3"]/table/tr['+str(num)+']/td[1]/text()'
    tmp = root.xpath(xpath)
    idlist.append(tmp)
    xpath = '//*[@id="inquiry3"]/table/tr['+str(num)+']/td[2]/a/text()'
    tmp = root.xpath(xpath)
    titlelist.append(tmp)

### 刊登日期 :
#------------------------------------------------
#/html/body[@id='home']/div[@class='wrapper']/div[@class='sqrezeer']/div[@class='soil']/article[@id='maincontent']/div[@class='abdominis']/div[@id='charity']/div[@id='charitysidebox3']/div[@id='inquiry3']/table/tbody/tr[@class='odd'][2]/td[@id='wordcenter'][1]
#...
#/html/body[@id='home']/div[@class='wrapper']/div[@class='sqrezeer']/div[@class='soil']/article[@id='maincontent']/div[@class='abdominis']/div[@id='charity']/div[@id='charitysidebox3']/div[@id='inquiry3']/table/tbody/tr[@class='odd'][21]/td[@id='wordcenter'][1]
#------------------------------------------------

datelist = []
for num in range(2,22):
    xpath = "/html/body[@id='home']/div[@class='wrapper']/div[@class='sqrezeer']/div[@class='soil']/article[@id='maincontent']/div[@class='abdominis']/div[@id='charity']/div[@id='charitysidebox3']/div[@id='inquiry3']/table/tr[@class='odd']["+ str(num) + "]/td[@id='wordcenter'][1]/text()"
    tmp = root.xpath(xpath)
    datelist.append(tmp)

### 狀態 :
#------------------------------------------------
#/html/body[@id='home']/div[@class='wrapper']/div[@class='sqrezeer']/div[@class='soil']/article[@id='maincontent']/div[@class='abdominis']/div[@id='charity']/div[@id='charitysidebox3']/div[@id='inquiry3']/table/tbody/tr[@class='odd'][3]/td[@id='wordcenter'][2]/font
#...
#/html/body[@id='home']/div[@class='wrapper']/div[@class='sqrezeer']/div[@class='soil']/article[@id='maincontent']/div[@class='abdominis']/div[@id='charity']/div[@id='charitysidebox3']/div[@id='inquiry3']/table/tbody/tr[@class='odd'][21]/td[@id='wordcenter'][2]/font
#------------------------------------------------

statelist = [] ; money = []
for num in range(2,22):
    xpath = "/html/body[@id='home']/div[@class='wrapper']/div[@class='sqrezeer']/div[@class='soil']/article[@id='maincontent']/div[@class='abdominis']/div[@id='charity']/div[@id='charitysidebox3']/div[@id='inquiry3']/table/tbody/tr[@class='odd']["+str(num)+"]/td[@id='wordcenter'][2]/font/text()"
    xpath = xpath.replace("/tbody","")
    tmp = root.xpath(xpath)
    statelist.append(tmp)

### 累計(元) :
#------------------------------------------------
#/html/body[@id='home']/div[@class='wrapper']/div[@class='sqrezeer']/div[@class='soil']/article[@id='maincontent']/div[@class='abdominis']/div[@id='charity']/div[@id='charitysidebox3']/div[@id='inquiry3']/table/tbody/tr[@class='odd'][2]/td[@id='wordcenter'][3]
#...
#/html/body[@id='home']/div[@class='wrapper']/div[@class='sqrezeer']/div[@class='soil']/article[@id='maincontent']/div[@class='abdominis']/div[@id='charity']/div[@id='charitysidebox3']/div[@id='inquiry3']/table/tbody/tr[@class='odd'][21]/td[@id='wordcenter'][3]
#------------------------------------------------
    
    xpath = "/html/body[@id='home']/div[@class='wrapper']/div[@class='sqrezeer']/div[@class='soil']/article[@id='maincontent']/div[@class='abdominis']/div[@id='charity']/div[@id='charitysidebox3']/div[@id='inquiry3']/table/tbody/tr[@class='odd']["+str(num)+"]/td[@id='wordcenter'][3]/text()"
    xpath = xpath.replace("/tbody","")
    tmp = root.xpath(xpath)
    money.append(tmp)

df1 = pd.DataFrame({"idlist":idlist,
                    "titlelist":titlelist,
                    "datelist":datelist,
                    "statelist":statelist,
                    "money":money})
print df1