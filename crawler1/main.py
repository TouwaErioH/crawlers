# 这个爬取的是动态页面
# 爬取动态页面，今日头条
# 源文件里是没有内容的只有js
import requests
from bs4 import BeautifulSoup as bs
import json
def gethtml(url):
    try:
        #通过F12检查出来自下面这个链接
        # url="https://www.toutiao.com/api/pc/feed/?category=news_hot&utm_source=toutiao&widen=1&max_behot_time=0&max_behot_time_tmp=0&tadrequire=true&as=A1D5FDAAB5194AE&cp=5DA599948ACE7E1&_signature=TBeQ-wAAEbOkzbKGAd3hQUwXkO"
        head={'User-Agent':'Mozilla/5.0 '}
        r=requests.get(url,headers=head)
        return r.text #返回json文件
    except:
        print("oneerror")
def getulist(html,list):
    try:
        soup=json.loads(html)
        soupdata=soup['data']
        for one in soupdata:
            a='https://www.toutiao.com/a'+one['group_id']
            list.append([one['title'],one['abstract'],a])
    except:
        print("twoerror")
def printulist(list):
    for i in list:
        print("title:\n{}".format(i[0]))
        print("简介：\n{}".format(i[1]))
        print("链接:{:^30}".format(i[2]))
if __name__=="__main__":
    url = "https://www.toutiao.com/api/pc/feed/?category=news_hot&utm_source=toutiao&widen=1&max_behot_time=0&max_behot_time_tmp=0&tadrequire=true&as=A1D5FDAAB5194AE&cp=5DA599948ACE7E1&_signature=TBeQ-wAAEbOkzbKGAd3hQUwXkO"
    html=gethtml(url)
    relist=[]
    getulist(html,relist)
    printulist(relist)