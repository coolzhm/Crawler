# -*- coding: utf-8 -*-
import scrapy
import urllib.request
from scrapy.http import Request, FormRequest
from bs4 import BeautifulSoup
import re
import stock.settings  as settings

'''
Sina股票数据接口
以大秦铁路（股票代码：601006）为例，如果要获取它的最新行情，只需访问新浪的股票数据接口：
http://hq.sinajs.cn/list=sh601006
这个url会返回一串文本，例如：
var hq_str_sh601006="大秦铁路, 27.55, 27.25, 26.91, 27.55, 26.20, 26.91, 26.92, 
22114263, 589824680, 4695, 26.91, 57590, 26.90, 14700, 26.89, 14300,
26.88, 15100, 26.87, 3100, 26.92, 8900, 26.93, 14230, 26.94, 25150, 26.95, 15220, 26.96, 2008-01-11, 15:05:32";
这个字符串由许多数据拼接在一起，不同含义的数据用逗号隔开了，按照程序员的思路，顺序号从0开始。
0：”大秦铁路”，股票名字；
1：”27.55″，今日开盘价；
2：”27.25″，昨日收盘价；
3：”26.91″，当前价格；
4：”27.55″，今日最高价；
5：”26.20″，今日最低价；
6：”26.91″，竞买价，即“买一”报价；
7：”26.92″，竞卖价，即“卖一”报价；
8：”22114263″，成交的股票数，由于股票交易以一百股为基本单位，所以在使用时，通常把该值除以一百；
9：”589824680″，成交金额，单位为“元”，为了一目了然，通常以“万元”为成交金额的单位，所以通常把该值除以一万；
10：”4695″，“买一”申请4695股，即47手；
11：”26.91″，“买一”报价；
12：”57590″，“买二”
13：”26.90″，“买二”
14：”14700″，“买三”
15：”26.89″，“买三”
16：”14300″，“买四”
17：”26.88″，“买四”
18：”15100″，“买五”
19：”26.87″，“买五”
20：”3100″，“卖一”申报3100股，即31手；
21：”26.92″，“卖一”报价
(22, 23), (24, 25), (26,27), (28, 29)分别为“卖二”至“卖四的情况”
30：”2008-01-11″，日期；
31：”15:05:32″，时间；


                    ------From: <http://blog.csdn.net/juncailiao/article/details/52159514>
'''


class stocksSpider(scrapy.Spider):
    name = "stock"
    list = []
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"}

    def start_requests(self):
        # print("准备爬取...")

        return [
            Request("http://hq.sinajs.cn/list=sz000016", headers=self.header, meta={'cookiejar': 1},
                    callback=self.parse)]

    def parse(self, response):
        url = "http://hq.sinajs.cn/list="
        try:
            self.list = settings.LIST
        except:
            self.list = ['sz000016']

        url = url + ','.join(self.list)
        # print(url)
        # print("进入爬取")
        soup = BeautifulSoup(response.body, 'lxml')
        # print(soup)
        for a in soup.find_all('p'):
            # print(a.string)
            for b in a.string.split(';'):
                for c in re.findall(r'".*"', b):
                    # print(c.encode("utf-8"))
                    if c != "":
                        c = c.encode("utf-8").decode("GBK")

                        # print(c)
                        self.domain(c)
        # print(response.url)

        return [
            Request(url, dont_filter=True, headers=self.header, meta={'cookiejar': 1},
                    callback=self.parse)]

    def domain(self, value):
        # value = str(value)
        values = value.split(",")
        ratio = round(round((float(values[3]) - float(values[2])) / float(values[2]), 4) * 100, 2)
        # str = "[{7} {8}]【{0}】 【{1}|[{2} {9}]】 买【{3}|[{4}]】 卖【{5}|[{6}]】".format(
        #     values[0], values[2], values[3], values[11], int(values[10]) / 100, values[21], int(values[20]) / 100,
        #     values[30], values[31], "{0}%".format(ratio))
        str = "[{3} {4}]【{0}】 【{1}|[{2} {5}]】".format(
            values[0], values[2], values[3], values[30], values[31], "{0}%".format(ratio))
        str2 = "买【{0} [{1}]】【{2} [{3}]】【{4} [{5}]】【{6} [{7}]】【{8} [{9}]】".format(
            values[11], int(values[10]) / 100, values[13], int(values[12]) / 100, values[15], int(values[14]) / 100,
            values[17], int(values[16]) / 100, values[19],
                        int(values[18]) / 100
        )
        str3 = "卖【{0} [{1}]】【{2} [{3}]】【{4} [{5}]】【{6} [{7}]】【{8} [{9}]】".format(
            values[21], int(values[20]) / 100, values[23], int(values[22]) / 100, values[25], int(values[24]) / 100,
            values[27], int(values[26]) / 100, values[29],
                        int(values[28]) / 100
        )
        print(str)
        print(str2)
        print(str3)
