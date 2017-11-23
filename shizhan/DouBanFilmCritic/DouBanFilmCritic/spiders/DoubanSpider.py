# -*- coding: utf-8 -*-
import scrapy
import urllib.request
from scrapy.http import Request, FormRequest
from DouBanFilmCritic.items import DouBanItem
from bs4 import BeautifulSoup
import re
from urllib import parse
import DouBanFilmCritic.settings as settings

'''
爬取豆瓣网站上[雷神3：诸神黄昏]电影的短评，爬取的内容包括，评论人、评论内容、评论星星数、以及
评论人是否看过电影、评论时间、以及评论是否有用信息，并将爬取内容存储到mysql数据库。可用于后续
对评论内容进行分析！
用到的技术包括：
1、正则
2、bs4
3、xpath
4、随机User-Agent防禁止

遇到的问题点：
1、Scrapy "Filtered duplicate request" 结束运行
此问题可参考 http://www.jianshu.com/p/d9d2e082af3a
在Request中加入dont_filter=True，例如
yield scrapy.Request(
    info_url,
    cookies=self.cookie,
    callback=self.parse_info,
    dont_filter=True,
    meta={
        'item': item,
        'date': meta_data['date'],
        'weibo_id': meta_data['weibo_id']
    }
)

'''


class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["douban.com", "accounts.douban.com", "movie.douban.com"]

    # 复写设置，用于指定pipelines执行
    custom_settings = {
        'ITEM_PIPELINES': {'DouBanFilmCritic.pipelines.SaveMainMySQLPipeline': 1},
    }

    # 设置头信息变量，供下面代码中模拟成浏览器爬取
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/59.0.3071.115 Safari/537.36"}
    num = 5

    # 编写start_requests(self)方法，第一次会默认调取该方法中的请求
    def start_requests(self):
        # 是否模拟登陆标识，0不登录 1登陆
        login = settings.LOGIN
        if login == 1:
            print("此时需要模拟登陆...")
            return [Request("https://accounts.douban.com/login", meta={'cookiejar': 1}, callback=self.parse)]
        else:
            print("此时不需要模拟登陆...")
            return [Request(
                "https://movie.douban.com/subject/25821634/comments?start=0&limit=20&sort=new_score&status=P&percent_type=",
                callback=self.next)]

    def parse(self, response):
        print("进入模拟登陆方法..")
        # 获取验证码图片所在地址，获取后赋给captcha变量，此时captcha为一个列表
        captcha = response.xpath('//img[@id="captcha_image"]/@src').extract()
        # 因为登陆时有时网页有验证码，有时没有验证码
        # 所以需要判定此时是否需要输入验证码，若captcha列表中有元素，说明有验证码信息
        if len(captcha) > 0:
            print("此时有验证码")
            # 设置将验证码图片存储到本地的本地地址中
            localpath = "H:/Python/Project/PythonSpiderLearning/Crawler/shizhan/DouBanFilmCritic/DouBanFilmCritic/spiders/captcha.png"
            # 将服务器中的验证码图片存储到本地，供我们在本地直接进行查看
            urllib.request.urlretrieve(captcha[0], filename=localpath)
            print("请查看本地图片captcha.png并输入对应验证码：")
            # 通过input（）等待我们输入对应的验证码并赋给captcha_value变量
            captcha_value = input()

            # 设置要传递的post信息
            data = {
                # 设置登陆账号，格式为账号字段名：具体账号
                "form_email": "357270546@qq.com",
                # 设置登陆密码，格式为密码字段名：具体密码
                "form_password": "Aa8616645",
                # 设置验证码，格式为验证码字段名：具体验证码
                "captcha-solution": captcha_value,
                # 设置需要转向的网址
                "redir": "https://movie.douban.com/subject/25821634/comments?start=0&limit=20&sort=new_score&status=P&percent_type="
            }
        else:
            print("此时没有验证码")
            # 设置需要传递的post信息，此时没有验证码字段
            data = {
                # 设置登陆账号，格式为账号字段名：具体账号
                "form_email": "357270546@qq.com",
                # 设置登陆密码，格式为密码字段名：具体密码
                "form_password": "Aa8616645",
                # 设置需要转向的网址
                "redir": "https://movie.douban.com/subject/25821634/comments?start=0&limit=20&sort=new_score&status=P&percent_type="
            }
        print("登陆中...")
        # 通过FormRequest.form_response()进行登录
        return [FormRequest.from_response(response,
                                          # 设置cookie信息
                                          meta={"cookiejar": response.meta["cookiejar"]},
                                          # 设置headers信息模拟成浏览器
                                          headers=self.header,
                                          # 设置post表单中的数据
                                          formdata=data,
                                          # 设置毁掉函数，此时毁掉函数为next（）
                                          callback=self.next,
                                          )]

    def next(self, response):
        soup = BeautifulSoup(response.body, 'lxml')
        # print("进入雷神3：诸神黄昏 短评网页：【{0}】".format(response.url))
        print("当前URL：【{0}】".format(response.url))
        # 匹配内容的正则
        # content_re = re.compile(r'<p class="">.*</p>')
        i = 1
        for one in soup.find_all("div", class_="comment-item"):
            model = DouBanItem()

            for a in one.find_all("p", class_=""):
                model["content"] = a.string

            for b in one.find_all("span", attrs={"class": re.compile(r'^allstar')}):
                model["star"] = b["class"][0][7:]
                # print(b["class"][0][7:])

            for c in one.find_all("span", class_="votes"):
                model["result"] = c.string
                # print(c.string)

                # for d in one.find_all("span", class_="comment-info"):
                #     for da in d.find_all('a'):
                #         print(da.get('href'))
            model['watch'] = response.xpath(
                '//*[@id="comments"]/div[{0}]/div[2]/h3/span[2]/span[1]/text()'.format(i)).extract_first()
            # print(model['watch'])

            for e in one.find_all("span", attrs={"class": re.compile(r'comment-time')}):
                model["date"] = e.get('title')
                # print(e.get('title'))

            # for f in one.find_all("div", class_="avatar"):
            #     for fa in f.find_all("a"):
            #         model["username"] = fa.get('title')
            #         print(fa.string)
            model["username"] = response.xpath('//*[@id="comments"]/div[{0}]/div[1]/a/@title'.format(i)).extract_first()
            # print(model["username"])
            i = i + 1
            yield model
            # print(model)

        url = ""
        for url_ in soup.find_all('a', class_="next"):
            urls = 'https://movie.douban.com/subject/25821634/comments'
            url = urls + url_.get('href')
            # print(url_.get('href'))
        print("下个URL：【{0}】".format(url))
        # 是否模拟登陆标识，0不登录 1登陆
        login = settings.LOGIN
        if login == 1:
            yield Request(url=parse.urljoin(response.url, url), meta={'cookiejar': response.meta["cookiejar"]},
                          callback=self.next, dont_filter=True)
        else:
            yield Request(
                url, callback=self.next, dont_filter=True)
