from bs4 import BeautifulSoup
import bs4
import requests
import re
def html():
    # 得到未解析的HTML网页内容
    r = requests.get("https://whu.edu.cn/coremail/common/index_cm40.jsp")
    print(r.text)
    # 得到解析的HTML网页内容
    demo = r.text
    soup = BeautifulSoup(demo, 'html.parser')
    #print(soup.prettify())
    print(soup.title)
    print(soup.a)
    # 查看标签a的属性
    tag = soup.a
    print(tag.attrs)
    # 查看标签a的属性中class的值
    tag.attrs['class']
    # 查看标签a的属性 的类型
    print(type(tag.attrs))
    # 查看标签a的非属性字符串
    print(tag.string)
    # 查看标签a的非属性字符串属性 的类型
    print(type(tag.string))
    # 返回值为bs4.element.NavigableString  (可以遍历的字符串）

def htmlergodic():
    # 得到未解析的HTML网页内容
    r = requests.get("https://whu.edu.cn/coremail/common/index_cm40.jsp")
    #print(r.text)
    # 得到解析的HTML网页内容
    demo = r.text
    soup = BeautifulSoup(demo, 'html.parser')
    # 子节点的列表，将<tag>所有儿子节点存入列表
    #print(soup.body.contents)
    # 获得孩子节点的个数
    print(len(soup.body.contents))
    # 分别输出各个子节点
    print(soup.body.contents[0])
    print(soup.body.contents[2])
    # 标号 由0开始

    for child in soup.body.children:
        print(child)
    for child in soup.body.descendants:
        print(child)

    print(soup.a.parent.name)
    for parent in soup.a.parents:  #注意s
        print(parent.name)

    for sibling in soup.a.next_siblings:
        print(sibling)

    print(soup.body.prettify())

def jiansuo():
    r = requests.get("http://www.baidu.com/")
    r.encoding = r.apparent_encoding
    demo = r.text
    soup = BeautifulSoup(demo, 'html.parser')
    print(soup.find_all('a'))

def sakura():
    r = requests.get("http://www.whu.edu.cn/")
    r.encoding = r.apparent_encoding
    demo = r.text
    soup = BeautifulSoup(demo,'html.parser')
    for tag in soup.find_all('a', string=re.compile('樱')):
        print(tag.string)
def fyrw():
    r=requests.get("http://top.baidu.com/buzz?b=257&fr=topboards")
    r.encoding=r.apparent_encoding
    demo=r.text
    soup=BeautifulSoup(demo, 'html.parser')
    ulist = []
    for tag in soup.find_all('a', 'list-title' ):
        ulist.append(tag.string)
        print(ulist.index(tag.string)+1,ulist[ulist.index(tag.string)])


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children: #提取tbody的每个tr标签
        if isinstance(tr,bs4.element.Tag): #判断tr是否是tag类型
            tds = tr('td')                 #tds[0] <td>1</td>.简写，等价于下一行代码
            #tds = tr.find_all('td')
            # ,然后用.string取string
            #ulist.append([tds[0].contents[0].string, tds[1].string, tds[3].string])
            #ulist.append([tds[0].string, tds[1].string, tds[3].string])

            tmp=tds[1].find('a')
            #print(tds[0].string, tmp.string, tds[3].string)
            ulist.append([tds[0].string, tmp.string, tds[3].string])
def printUnivListbeta(ulist, num):
    print("{:^10}\t{:^6}\t{:^10}".format("排名", "学校名称", "总分"))
    for i in range(num):
        u = ulist[i]
        print("{:^10}\t{:^6}\t{:^10}".format(u[0], u[1], u[2]))


'''
# :是引导符号
#  : <填充><对齐><宽度>,<精度><类型>  这里的 ','是千位分隔符
# 拿上面的代码举例
#tply：0,1,2对应输出的第0，1，2个数据。^表示居中，然后第0个数据宽4.中间{3}表示填充用format第3个变量也就是chr(12288)
'''
def printUnivList(ulist, num):
    tplt = "{0:^4}\t{1:{3}^12}\t{2:^10}"
    print(tplt.format("排名", "学校名称", "总分", chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], chr(12288)))


def main():
    uinfo = []
    #url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2017.html'
    #url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    url='http://www.zuihaodaxue.cn/ARWU2016.html'
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20)  # 20 univs

if __name__=="__main__":
    main()
    #html()
    #htmlergodic()
    #jiansuo()
    #sakura()
    #fyrw()
