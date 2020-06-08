import requests
from bs4 import BeautifulSoup


def analyse(str):
    str1 = str.split('>', 1)
    str2 = str1[1].split('<', 1)
    return str2[0]

def spe1_analyse(str):
    str1 = str.split('>', 1)
    str2 = str1[1].split('㎡', 1)
    return str2[0]

def spe2_analyse(str):
    str1 = str.split('>', 1)
    str2 = str1[1].split('/', 1)
    return str2[0]

def spe3_analyse(str):
    str1 = str.split('>', 3)
    str2 = str1[3].split('<', 1)
    return str2[0]


# r = requests.get("https://gy.58.com/ershoufang/")
# html_doc = r.text
# print(r.text)
with open('test.html', "r", encoding="utf-8") as f:
    file = f.read()
soup = BeautifulSoup(file,"lxml")
#因变量：单位价格
#自变量：总面积、楼层、房间数、交通、区

for i in range(1000):


    #总价
    sum = soup.select('body > div.main-wrap > div.content-wrap > div.content-side-left > ul > li:nth-child({id}) > div.price > p.unit'.format(id = str(i)))
    if sum !=[]:
        sum = spe2_analyse(str(sum))
    else:
        sum = 0


    #户型
    type1 = soup.select('body > div.main-wrap > div.content-wrap > div.content-side-left > ul > li:nth-child({id}) > div.list-info > p:nth-child(2) > span:nth-child(1)'.format(id = str(i)))
    if type1 !=[]:
        type1 = analyse(str(type1))
    else:
        type1 = 0


    #面积
    area = soup.select('body > div.main-wrap > div.content-wrap > div.content-side-left > ul > li:nth-child({id}) > div.list-info > p:nth-child(2) > span:nth-child(2)'.format(id = str(i)))
    if area !=[]:
        area = spe1_analyse(str(area))
    else:
        area = 0


    #楼层
    floor = soup.select('body > div.main-wrap > div.content-wrap > div.content-side-left > ul > li:nth-child({id}) > div.list-info > p:nth-child(2) > span:nth-child(4)'.format(id = str(i)))
    if floor !=[]:
        floor = analyse(str(floor))
    else:
        floor = 0


    #地区
    region = soup.select('body > div.main-wrap > div.content-wrap > div.content-side-left > ul > li:nth-child({id}) > div.list-info > p:nth-child(3) > span > a:nth-child(2)'.format(id = str(i)))
    if region !=[]:
        region = analyse(str(region))
    else:
        region = 0


    #交通
    traffic = soup.select('body > div.main-wrap > div.content-wrap > div.content-side-left > ul > li:nth-child({id}) > div.list-info > p:nth-child(3) > span:nth-child(2)'.format(id = str(i)))
    if traffic !=[]:
        traffic = spe3_analyse(str(traffic))
    else:
        traffic = 0
    print(sum)
    print(type1)
    print(area)
    print(floor)
    print(region)
    print(traffic)
