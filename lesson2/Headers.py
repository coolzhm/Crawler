# -*- coding: utf-8 -*-
import urllib.request

url = "http://blog.csdn.net/weiwei_pig/article/details/51178226"
file = urllib.request.urlopen(url)
print(file)
print(file.getcode())

# 使用build_opener()修改报头
url = "http://blog.csdn.net/weiwei_pig/article/details/51178226"
headers = ("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
data = opener.open(url).read()
print(data)
fhandle = open(u"H:\Python\Project\PythonSpiderLearning\Crawler\lesson2\\2.html","wb")
fhandle.write(data)
fhandle.close()

#使用add_header()添加报头
url = "http://blog.csdn.net/weiwei_pig/article/details/51178226"
req=urllib.request.Request(url)
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0')
data = urllib.request.urlopen(req).read()
print(data)