#Author:xue yi yang
import requests
from bs4 import BeautifulSoup
import bs4


def getHTMLText(url):
    try:
        r = requests.get(url, timeoout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string])


def printUnivList(ulist, num):
    tplt = "{0:^10}\t{1:{3}^10}"
    print(tplt.format("企业名称", "统一社会信用代码", chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], chr(12288)))


def main():
    uinfo = []
    for num in range(1, 700):  # 循环record=1-700的所有url
        url = "http://www.credithebei.gov.cn:8082/was5/web/detail?record={}&channelid=220802".format(num)
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo)


main()