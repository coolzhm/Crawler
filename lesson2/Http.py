# -*- coding: utf-8 -*-

import urllib.request

keywd = "hello"
url = "http://www.baidu.com/s?wd=" + keywd
req = urllib.request.Request(url)
data = urllib.request.urlopen(req).read()
fhandl = open("H:\Python\Project\PythonSpiderLearning\Crawler\lesson2\\4.html", "wb")
fhandl.write(data)
fhandl.close()

url = "http://www.baidu.com/s?wd="
key = u"你好啊"
#通过urllib.request.quote对关键字编码
key_code = urllib.request.quote(key)
url_all = url + key_code
req = urllib.request.Request(url_all)
data = urllib.request.urlopen(req).read()
fhandl = open("H:\Python\Project\PythonSpiderLearning\Crawler\lesson2\\5.html", "wb")
fhandl.write(data)
fhandl.close()
