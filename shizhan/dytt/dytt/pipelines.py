# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import dytt.settings as settings


class TestPipeline(object):
    def __init__(self):
        print(">>>>>>>>>>>>>>>> 这个是用来测试的Pipeline <<<<<<<<<<<<<<<<<")

    def process_item(self, item, spider):
        return item


# 将爬取数据存入MYSQL
class SaveMainUrlToMySQLPipeline(object):
    # config = {
    #     'host': 'localhost',
    #     'port': 3306,
    #     'user': 'root',
    #     'password': 'a8616645',
    #     'db': 'test',
    #     'charset': 'utf8mb4'
    # }
    config = []

    def __init__(self):
        self.config = settings.MYSQL_CONFIG
        print(">>>>>>>>>>>>>>>> 准备写入MySQL数据库 <<<<<<<<<<<<<<<<<")

    def process_item(self, item, spider):
        # 创建连接
        connection = pymysql.connect(**self.config)
        print(">>>>>>>>>>>>>>>> 创建连接 <<<<<<<<<<<<<<<<<")
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM dytt_domain WHERE 1 = 1 AND title = '{0}' AND full_url = '{1}'".format(
                    item['title'], item['full_url'])
                # print('------>>>>>>>>>>执行查询SQL为：')
                # print(sql)
                rr = cursor.execute(sql)
                row = cursor.fetchall()
                if (len(row) > 0):
                    print("已经存在【{0}】【{1}】！".format(item['title'], item['full_url']))
                    return

                sql = "INSERT INTO dytt_domain(id,title,full_url,url,checked)" \
                      "VALUES (nextval('dytt_domain'),'{0}','{1}','{2}','0')".format(
                    item['title'], item['full_url'], item['url'])
                # print('------>>>>>>>>>>执行写入SQL为：')
                # print(sql)
                cursor.execute(sql)
                connection.commit()
                # print('------>>>>>>>>>>执行写入SQL成功！！')
        finally:
            connection.close()

    def spider_closed(self, spider):
        print(">>>>>>>>>>>>>>>> 写入MySQL数据库完成 <<<<<<<<<<<<<<<<<")
