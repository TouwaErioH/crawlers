import requests
import os

def amazon():
    #url="https://www.amazon.cn"
    # r=requests.get(url)
    # print(r.status_code)
    #url="https://www.amazon.com"
    #理论上python直接爬，可以看到requests请求很诚实的告诉了网站访问使用Python发起的，
    # 该网站通过头信息判断该访问是爬虫发起的而不是由浏览器发起的。amazon会503，使用useragent模拟浏览器后没问题
    #问题是直接10060.
    #url = "https://www.amazon.co.jp"
    # try:
    #      r=requests.get(url)
    #      #r = requests.get(url,timeout=5)
    #       print(r.request.headers)  #头信息
    #      #print(r.request.url)
    #      #r.raise_for_status()
    #      print(r.status_code)
    # except:
    #      print("except %s"% r.status_code)
    # print(r.request.headers)  #   注意是request 网站通过头信息判断是python发起，爬虫，拒绝
    #hd = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}
    #r = requests.request('post', url=url, headers=hd)
    #r = requests.get(url, headers=hd)

    #上面是网络问题导致的amazon访问不了，我还以为是代码问题改了很久...
    url = "https://www.amazon.com"
    r=requests.get(url)
    print("%s %s"%(r.status_code,r.request.headers))  #注意是request.headers不是requests
    #503 {'User-Agent': 'python-requests/2.21.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
    hd = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}
    #r = requests.request('post', url=url, headers=hd) #请求方式是post，返回状态码405，后台不允许post
    r = requests.get(url, headers=hd)
    print("%s %s" % (r.status_code, r.request.headers))  #200

def searchengine():
    keyword = "知乎"
    try:
        kv = {'wd': keyword}
        r = requests.get("http://www.baidu.com/s", params=kv)
        print(r.request.url)
        r.raise_for_status()
        print(r.text[1:1000])
    # 结果太长，打印前1000个字符
    except:
        print("爬取失败")
    # 百度直接搜索 武汉大学，华科
    # https: // www.baidu.com / s?wd = 武汉大学 & rsv_spt = 1……
    # https: // www.baidu.com / s?wd = 华中科技大学 & rsv_spt = 1……
    # 所以只需要替换wd即可搜索
    #

def images():
    #可以通过循环语句，批量爬取大量图片  正则式也可
    url = "https://meowdancing.com/images/timg.jpg"
    root = "F://Pictures//"
    path = root + url.split('/')[-1]  #split 通过 / 分片，取最后一片也就是timg.jpg
    try:
        if not os.path.exists(root):
            os.mkdir(root)  # 用于以数字权限模式创建目录
        if not os.path.exists(path):
            r = requests.get(url)
            with open(path, 'wb')as f:
                f.write(r.content)
                f.close()
                print("文件保存成功")
        else:  # 写代码时注意缩进
            print("文件已存在")
    except:
        print("爬取失败")

def ipaddress():
    url = "http://www.ip138.com/ips138.asp?ip="
    ip="101.24.190.228"
    url=url+ip
    #   +"&action=2" 不加也可以
    hd = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}
    print(url)
    try:
        r = requests.get(url,headers=hd)   #不加hd好像不行
        print(r.status_code)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.text[-2000:])  # 输出最后2000个字符
    except:
        print("爬取失败")

    # 打开
    # http: // www.ip138.com / 可以通过输入IP地址查询地理位置，输入IP地址后，查看浏览器链接
    # http: // www.ip138.com / ips138.asp?ip = 202.114
    # .66
    # .96 & action = 2
    # 可以看出，查询链接为
    # http: // www.ip138.com / ips138.asp?ip =“你的IP地址”
    #
    # 通过这个例子我们可以看出，很多人机交互的操作，实际上是通过提交的HTTP链接来完成的，
    # 因此当我门通过简单的分析，得知HTTP链接与交互信息的对应关系后，就可以通过Python，爬取我们所需的资源


if __name__ == "__main__":
    amazon()
    #searchengine()
    #images()
    #ipaddress()
