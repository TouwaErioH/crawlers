import requests     #  s


#选中ctrl +/ 注释

def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30) #reponse   参数 timeout
        r.raise_for_status()  # 如果状态不是200，引发error异常
        # print("%d\n %s" % (r.status_code, r.text))
        print("%s %s" % (r.encoding, r.apparent_encoding))
        r.encoding=r.apparent_encoding
        print("%s %s" % (r.encoding, r.apparent_encoding))
        #html = r.content  # bytes 类型
        #html_doc = str(html, 'utf-8')  # html_doc=html.decode("utf-8","ignore")
        #print(html_doc)
        print(r.text)
        return r.text
    except:
        return "产生异常"

def head(url):
    r=requests.head(url)
    print(r.headers)    # 注意head headers
    print(r.text)   #空

def post(url): #追加
    r=requests.get("http://httpbin.org/post")
    print(r.text)
    payload = {'name': '刘强', 'ID': '2017301510029'}
    r = requests.post("http://httpbin.org/post", data=payload)   #参数 data
    print(r.text)

def put(url):   #覆盖
    r = requests.get("http://httpbin.org/put")
    print(r.text)
    payload = {'name': 'your_name', 'ID': '123456'}
    r = requests.put("http://httpbin.org/put", data=payload)
    print(r.text)

if __name__ == '__main__':
    #url = "https://www.baidu.com"
    url="http://whu.edu.cn"
    #url="www.baidu.com"
    #url="http://httpbin.org/put"
    #url="http://httpbin.org/post"
    #getHTMLText(url)
    #head(url)
    post(url)
    put(url)


