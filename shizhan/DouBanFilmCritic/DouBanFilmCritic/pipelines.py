# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import DouBanFilmCritic.settings as settings

class DoubanfilmcriticPipeline(object):
    def process_item(self, item, spider):
        return item


class SaveMainMySQLPipeline(object):
    config = []

    def __init__(self):
        self.config = settings.MYSQL_CONFIG
        print(">>>>>>>>>>>>>>>> 准备写入MySQL数据库 <<<<<<<<<<<<<<<<<")

    def process_item(self, item, spider):
        # 创建连接
        connection = pymysql.connect(**self.config)
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO douban(id,username,content,star,dates,result,watch)" \
                      "VALUES (nextval('douban'),'{0}','{1}','{2}','{3}','{4}','{5}')".format(
                    item['username'], item['content'], item['star'],item['date'],item['result'],item['watch'])
                cursor.execute(sql)
                connection.commit()
        finally:
            connection.close()

    def spider_closed(self, spider):
        print(">>>>>>>>>>>>>>>> 写入MySQL数据库完成 <<<<<<<<<<<<<<<<<")

