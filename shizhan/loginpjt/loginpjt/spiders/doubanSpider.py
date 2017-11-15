# -*- coding: utf-8 -*-
import scrapy, urllib, re
from scrapy.http import Request, FormRequest


class DoubanSpider(scrapy.Spider):
    name = "DouBan"
    allowed_domains = ["douban.com"]
    # start_urls = ['http://douban.com/']
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"}  # 供登录模拟使用

    def start_requests(self):
        url = 'https://www.douban.com/accounts/login'
        print('准备')
        return [Request(url=url, meta={"cookiejar": 1},
                        callback=self.parse)]  # 可以传递一个标示符来使用多个。如meta={'cookiejar': 1}这句，后面那个1就是标示符

    def parse(self, response):
        print('进入')
        captcha = response.xpath('//*[@id="captcha_image"]/@src').extract()  # 获取验证码图片的链接
        print(captcha)
        if len(captcha) > 0:
            '''此时有验证码'''
            print('此时有验证码')
        else:
            '''此时没有验证码'''
            print('无验证码')
            data = {
                "form_email": "weisuen007@163.com",
                "form_password": "weijc7789",
                # "redir": "https://www.douban.com/people/151968962/",
            }
        print('正在登陆中......')
        ####FormRequest.from_response()进行登陆
        return [
            FormRequest.from_response(
                response,
                meta={"cookiejar": response.meta["cookiejar"]},
                headers=self.header,
                formdata=data,
                callback=self.get_content,
            )
        ]

    def get_content(self, response):
        title = response.xpath('//title/text()').extract()[0]
        if u'登录豆瓣' in title:
            print('登录失败，请重试！')
        else:
            print('登录成功')
            '''
            可以继续后续的爬取工作
            '''
