import urllib.request
import urllib.parse

'''
    Cookiejar实战精析
'''

'''
    无cookie处理的登陆
'''

url = "http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=LpJt3"
postdata = urllib.parse.urlencode({
    "username": "zhmmerry",
    "password": "a8616645"
}).encode('utf-8')  # 使用urlencode编码处理后，再设置为utf-8编码
req = urllib.request.Request(url, postdata)  # 构建Request对象
req.add_header('User-Agent',
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36')
data = urllib.request.urlopen(req).read()  # 登陆并爬取对应网页
fhandle = open("H:\Python\Project\PythonSpiderLearning\Crawler\section5\\1.html", "wb")
fhandle.write(data)  # 将内容写入对应文件
fhandle.close()

url2 = "http://bbs.chinaunix.net/"  # 设置要爬取该网站下其他网页地址
req2 = urllib.request.Request(url, postdata)
req2.add_header('User-Agent',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36')
data2 = urllib.request.urlopen(req).read()  # 登陆并爬取对应网页
fhandle = open("H:\Python\Project\PythonSpiderLearning\Crawler\section5\\2.html", "wb")
fhandle.write(data2)  # 将内容写入对应文件
fhandle.close()

'''
    Cookie处理登陆
'''
import http.cookiejar

url = "http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=LpJt3"
postdata = urllib.parse.urlencode({
    "username": "zhmmerry",
    "password": "a8616645"
}).encode('utf-8')  # 使用urlencode编码处理后，再设置为utf-8编码
req = urllib.request.Request(url, postdata)  # 构建Request对象
req.add_header('User-Agent',
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36')
# 使用http.cookiejar.CookieJar()创建CookieJar对象
cjar = http.cookiejar.CookieJar()
# 就是用HTTPCookieProcessor创建cookie处理器，并以其为参数构建opener对象
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
# 将opener安装为全局
urllib.request.install_opener(opener)
file = opener.open(req)
data = file.read()

file = open("H:\Python\Project\PythonSpiderLearning\Crawler\section5\\3.html", "wb")
file.write(data)  # 将内容写入对应文件
file.close()

url2 = "http://bbs.chinaunix.net/"  # 设置要爬取该网站下其他网页地址
data2 = urllib.request.urlopen(url2).read()  # 登陆并爬取对应网页
fhandle = open("H:\Python\Project\PythonSpiderLearning\Crawler\section5\\4.html", "wb")
fhandle.write(data2)  # 将内容写入对应文件
fhandle.close()
