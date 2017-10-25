# -*- coding: utf-8 -*-

import urllib.request

# GET请求实例
keywd = "hello"
url = "http://www.baidu.com/s?wd=" + keywd
req = urllib.request.Request(url)
data = urllib.request.urlopen(req).read()
fhandl = open("H:\Python\Project\PythonSpiderLearning\Crawler\lesson2\\4.html", "wb")
fhandl.write(data)
fhandl.close()

url = "http://www.baidu.com/s?wd="
key = u"你好啊"
# 通过urllib.request.quote对关键字编码
key_code = urllib.request.quote(key)
url_all = url + key_code
req = urllib.request.Request(url_all)
data = urllib.request.urlopen(req).read()
fhandl = open("H:\Python\Project\PythonSpiderLearning\Crawler\lesson2\\5.html", "wb")
fhandl.write(data)
fhandl.close()

# POST请求实例
import urllib.parse

url = "http://www.iqianyue.com/mypost/"
postdata = urllib.parse.urlencode({
    "name": "ceo@iqianyue.com",
    "pass": "aA123456"
}).encode('utf-8') #讲数据使用urlencode编码处理后，使用encode（）设置为utf-8编码
req=urllib.request.Request(url,postdata)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36')
data=urllib.request.urlopen(req).read()
fhandl = open("H:\Python\Project\PythonSpiderLearning\Crawler\lesson2\\6.html", "wb")
fhandl.write(data)
fhandl.close()
