# -*- coding: utf-8 -*-
'''
1、分析各页面的网址规律，构造网址变量，并可以通过for循环实现多页内容的爬取
2、构建一个自定义函数，专门用来实现爬取某个网页上的段子。包括两部分内容，一部分是对应
用户，一部分是用户发表的段子内容。该函数功能实现的过程为：首先，模拟成浏览器访问，
观察对应网页源代码中的内容，将用户信息部分与段子内容部分的格式写成正则表达式。随后，
根据正则表达式分别赋给对应的变量，这里变量名是有规律的，格式为“content+顺序号”，
接下来再通过for循环遍历对应用户，并输出该用户对应的内容。
3、通过for循环分别获取多页的各页URL链接，每页分别调用一次getcontent(url,
page)函数。
'''

import urllib.request
import re


def getcontent(url, page):
    # 模拟成浏览器
    headers = ("User-Agent",
               "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3192.0 Safari/537.36")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    # 将opener安装为全局
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(url).read()
    data = data.decode('utf-8')
    # 构建对应用户提取的正则表达式
    userpat = 'target="_black" title="(.*?)*>'
    # 构建段子内容提取的正则表达式
    contentpat = '<div class="content">(.*?)</div>'
    # 寻找出所有的用户
    userlist = re.compile(userpat, re.S).findall(data)
    # 寻找出所有的内容
    contentlist = re.compile(contentpat, re.S).findall(data)
    x = 1
    # 通过for循环遍历段子内容并将内容分别赋值给对应的变量
    for content in contentlist:
        content = content.replace("\n", "")
        # 用字符串作为变量名，先将对应字符串赋值给一个变量
        name = "content" + str(x)
        # 通过exec（）函数实现用字符串作为变量名并赋值
        exec(name + '=content')
        x += 1
    y = 1
    # 通过for循环遍历用户，并输出该用户对应的内容
    for user in userlist:
        name = "content" + str(y)
        print("用户" + str(page) + str(y) + "是:" + user)
        print("内容是：")
        exec("print(" + name + ")")
        print("\n")
        y += 1


# 分别获取各页的段子，通过for循环可以获取多页
for i in range(1, 30):
    url = "http://www.qiushibaike.com/8hr/page/"+str(i)
    getcontent(url, i)
