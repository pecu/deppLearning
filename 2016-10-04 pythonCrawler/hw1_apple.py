# -*- coding: utf-8 -*-
from lxml import etree
import requests
import pandas as pd

###  蘋果日報基金會 :
targeturl = "http://search.appledaily.com.tw/charity/projlist/"

res = requests.get(targeturl)
res.encoding = 'utf8'
root = etree.fromstring(res.content, etree.HTMLParser()) 

#===============================================#
### Hint                                        #
#===============================================#
# list [] 可以使用 .append() 方法               #
#                                               #
# ex. list1=[] ; x=10 ; list1.append(x)         #
#===============================================#
# str "" 可以使用拼貼  "+"   方法               #
#                                               #
# ex. str1="xx" ; str2="YY" ; str3=str1+str2    #
#     print str3                                #
#     >>> "xxYY"                                #
#===============================================#
# range(1,10)                                   #
# >>> [1, 2, 3, 4, 5, 6, 7, 8, 9]               # 
#===============================================#

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
for 


### 刊登日期 :
#------------------------------------------------
#/html/body[@id='home']/div[@class='wrapper']/div[@class='sqrezeer']/div[@class='soil']/article[@id='maincontent']/div[@class='abdominis']/div[@id='charity']/div[@id='charitysidebox3']/div[@id='inquiry3']/table/tbody/tr[@class='odd'][2]/td[@id='wordcenter'][1]
#...
#/html/body[@id='home']/div[@class='wrapper']/div[@class='sqrezeer']/div[@class='soil']/article[@id='maincontent']/div[@class='abdominis']/div[@id='charity']/div[@id='charitysidebox3']/div[@id='inquiry3']/table/tbody/tr[@class='odd'][21]/td[@id='wordcenter'][1]
#------------------------------------------------

datelist = []
for 


### 狀態 :
#------------------------------------------------
#/html/body[@id='home']/div[@class='wrapper']/div[@class='sqrezeer']/div[@class='soil']/article[@id='maincontent']/div[@class='abdominis']/div[@id='charity']/div[@id='charitysidebox3']/div[@id='inquiry3']/table/tbody/tr[@class='odd'][3]/td[@id='wordcenter'][2]/font
#...
#/html/body[@id='home']/div[@class='wrapper']/div[@class='sqrezeer']/div[@class='soil']/article[@id='maincontent']/div[@class='abdominis']/div[@id='charity']/div[@id='charitysidebox3']/div[@id='inquiry3']/table/tbody/tr[@class='odd'][21]/td[@id='wordcenter'][2]/font
#------------------------------------------------
### 累計(元) :
#------------------------------------------------
#/html/body[@id='home']/div[@class='wrapper']/div[@class='sqrezeer']/div[@class='soil']/article[@id='maincontent']/div[@class='abdominis']/div[@id='charity']/div[@id='charitysidebox3']/div[@id='inquiry3']/table/tbody/tr[@class='odd'][2]/td[@id='wordcenter'][3]
#...
#/html/body[@id='home']/div[@class='wrapper']/div[@class='sqrezeer']/div[@class='soil']/article[@id='maincontent']/div[@class='abdominis']/div[@id='charity']/div[@id='charitysidebox3']/div[@id='inquiry3']/table/tbody/tr[@class='odd'][21]/td[@id='wordcenter'][3]
#------------------------------------------------

statelist = [] ; money = []
for 





df1 = pd.DataFrame({"idlist":idlist,
                    "titlelist":titlelist,
                    "datelist":datelist,
                    "statelist":statelist,
                    "money":money})
print df1