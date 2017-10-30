# -*- coding: utf-8 -*-

'''
    第一个简单爬虫，爬取百度图片
'''

import re
import urllib.request, urllib.error

'''
从百度网页下载图片
'''


def crawfrombaidu(url, page):
    html1 = urllib.request.urlopen(url).read()
    html1 = str(html1)
    pat1 = '(http://.+?.jpg)'
    imagelist = re.compile(pat1).findall(html1)
    x = 1
    for imgeurl in imagelist:
        print(imgeurl)
        imagename = "C:/MyWorkSpace/GitHubProject/Crawler/section6/img1/baidu/" + str(page) + "-" + str(
            x) + ".jpg";
        try:
            urllib.request.urlretrieve(imgeurl, filename=imagename)
        except urllib.error.URLError as e:
            if hasattr(e, "code"):
                print(e.code)
                x += 1
            if hasattr(e, "reason"):
                print(e.reason)
                x += 1


'''
从京东下载商品图片
'''


def crawfromjingdong(url, page):
    html1 = urllib.request.urlopen(url).read()
    html1 = str(html1)
    pat1 = '<img width="220" height="220" data-img="1" src="//(.+?\.jpg)"'
    imagelist = re.compile(pat1).findall(html1)
    print(len(imagelist))
    x = 1
    for imgeurl in imagelist:
        print("http://" + imgeurl)
        imagename = "C:/MyWorkSpace/GitHubProject/Crawler/section6/img1/jingdong/" + str(page) + "-" + str(
            x) + ".jpg";
        try:
            urllib.request.urlretrieve("http://" + imgeurl, filename=imagename)
        except urllib.error.URLError as e:
            if hasattr(e, "code"):
                print(e.code)
                x += 1
            if hasattr(e, "reason"):
                print(e.reason)
                x += 1


print("------ Ready Dowmload pic from BD.. -----")
url = "http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E5%9B%BE%E7%89%87"
crawfrombaidu(url, 1)
print("------ Ready Dowmload pic from JD.. -----")
for i in range(1, 79):
    url = "http://list.jd.com/list.html?cat=9987,653,655&page=" + str(i)
    crawfromjingdong(url, i)
