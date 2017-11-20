# -*- coding: utf-8 -*-
import scrapy
import urllib.request
from scrapy.http import Request, FormRequest
from bs4 import BeautifulSoup
import random
from dytt.items import DyttMainItem
import io
import sys

'''
爬取电影天堂所有的电影信息
'''


# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8') #改变标准输出的默认编码

class DyttSpider(scrapy.Spider):
    name = "dytt"
    allowed_domains = ["www.ygdy8.net", "www.dytt8.net"]

    # 复写设置，用于指定pipelines执行
    custom_settings = {
        'ITEM_PIPELINES': {'dytt.pipelines.SaveMainUrlToMySQLPipeline': 300},
    }

    # 设置头信息变量，供下面代码中模拟成浏览器爬取
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/59.0.3071.115 Safari/537.36"}
    list = [2, 3, 4]

    # 编写start_requests(self)方法，第一次会默认调取该方法中的请求
    def start_requests(self):
        print("准备爬取...")
        print(self.settings["MYSQL_CONFIG"])
        return [Request("http://www.dytt8.net/html/gndy/china/index.html", headers=self.header, callback=self.parse)]

    def parse(self, response):
        print("进入爬取方法..")
        soup = BeautifulSoup(response.body, "lxml")
        for li in soup.find_all('div', id='menu'):
            for a in li.find_all('a'):
                item = DyttMainItem()
                item['url'] = a.get('href')
                # print(item['url'])
                item['title'] = a.get_text()
                if "http" in a.get('href'):
                    item['full_url'] = a.get('href')
                else:
                    item['full_url'] = "http://www.dytt8.net" + a.get('href')
                # print(item['full_url'])
                if item['full_url'].count("/") > 5:
                    if "/index" in item['full_url']:
                        yield item

        if (len(self.list) > 0):
            # 获取最后一个元素
            value = self.list.pop()
            print(value)
            print(self.list)
            url = "http://www.dytt8.net/html/gndy/rihan/list_6_" + str(value) + ".html"
            print("准备爬取---------->>>>>>>>>>>")
            print(url)
            return [Request(url, headers=self.header, callback=self.parse)]
