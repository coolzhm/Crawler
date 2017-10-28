# -*- coding: utf-8 -*-

'''
    第一个简单爬虫，爬取百度图片
'''

import re
import urllib.request, urllib.error


def craw(url, page):
    html1 = urllib.request.urlopen(url).read()
    html1 = str(html1)
    pat1 = '(http://.+?.jpg)'
    imagelist = re.compile(pat1).findall(html1)
    x = 1
    for imgeurl in imagelist:
        print(imgeurl)
        imagename = "H:/Python/Project/PythonSpiderLearning/Crawler/section6/img1/" + str(page) + "-" + str(
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


url = "http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E5%9B%BE%E7%89%87"
craw(url, 1)
