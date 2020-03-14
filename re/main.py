import re
def refunc():
    search = re.search(r'[1-9]\d{5}', 'WuHan 430073')
    match1 = re.match(r'[1-9]\d{5}', 'WuHan 430073')
    match2 = re.match(r'[1-9]\d{5}', '430073 WuHan')
    print("search结果")
    if search:
        print(search.group(0))
    print("\nmatch1结果")
    if match1:
        print(match1.group(0))
    else:
        print("未匹配到结果")
    print("\nmatch2结果")
    if match2:
        print(match2.group(0))

    findall = re.findall(r'[1-9]\d{5}', 'WuHan 430073  Beijing 100010')
    print("findall匹配结果")
    if findall:
        print(findall)
    print("finditer匹配结果")
    for m in re.finditer(r'[1-9]\d{5}', 'WuHan 430073  Beijing 100010'):
        if m:
            print(m.group(0))

    split1 = re.split(r'[1-9]\d{5}', 'WuHan 430073  Beijing 100010')
    split2 = re.split(r'[1-9]\d{5}', 'WuHan 430073  Beijing 100010', maxsplit=1)
    print("split1分割结果")
    print(split1)
    print("split2分割结果")
    print(split2)

    sub = re.sub(r'[1-9]\d{5}', '123456', 'WuHan 430073  Beijing 100010')
    print("替换结果")
    print(sub)

    pat = re.compile(r'[1-9]\d{5}')
    a = pat.search('wuhan430073')
    print("搜索结果")
    print(a)
    b = pat.sub('...','bj100010 wh430073')
    print("替换结果")
    print(b)

def rematch():
    m=re.search(r'[1-9]\d{5}','wuhan123456 thu456789')
    print(m.string)
    print(m.re)
    print(m.pos)
    print(m.endpos)
    print(m.start())
    print(m.end())
    print(m.span())
    print(m.group(0))

    for m in re.finditer(r'[1-9]\d{5}', 'WuHan 430073  Beijing 100010'):
        if m:
            print(m.group(0))
            print(m.pos)
            print(m.endpos)
            print(m.start())
            print(m.end())
            print(m.span())
def greedy():
    match = re.search(r'PY.*N', ' PYANBNCNDN')
    print(match.group(0))

    match = re.search(r'PY.*?N', ' PYANBNCNDN')
    print(match.group(0))


if __name__=='__main__':
    #refunc()
    #rematch()
    greedy()