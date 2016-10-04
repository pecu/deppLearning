from lxml import etree
import requests
import pandas as pd
from multiprocessing import Pool
from datetime import datetime

res = requests.get("https://www.buy123.com.tw/")
res.encoding = 'utf8'
root = etree.fromstring(res.content, etree.HTMLParser()) 

urllist = []
for each in root.xpath('//*[@id="container"]/div[4]/section[2]//a/@href'):
    urllist.append("https://www.buy123.com.tw/" + each)

def get_data(urllist):
    total_item = {}
    res = requests.get(urllist)
    res.encoding = 'utf8'
    root = etree.fromstring(res.content, etree.HTMLParser())
    try:
        tmp_item = root.xpath('//*[@id="deal_detail_info"]/div[1]/div/h1/text()')[0]
        tmp_price = root.xpath('//*[@id="price"]/text()')[1]
        tmp_sold = root.xpath('//*[@id="deal_price_detail"]/div[7]/text()')[0]
    except:
        tmp_item = 'na'
        tmp_price = 'na'
        tmp_sold = 'na'
    total_item[tmp_item] = [tmp_price,tmp_sold]
    return total_item

if __name__ == '__main__':
    scraped_data = []
    
    starttime = datetime.now()    
    
    p = Pool(7)
    scraped_data.append(p.map(get_data,urllist))
    df1 = pd.DataFrame(scraped_data)

    endtime = datetime.now()
    runtime = endtime - starttime
    print "Total run time : "+runtime
    # len(scraped_data[0]) = 3387










