# -*- coding: utf-8 -*-

# Scrapy settings for dytt project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'dytt'
SPIDER_MODULES = ['dytt.spiders']
NEWSPIDER_MODULE = 'dytt.spiders'

MYSQL_CONFIG = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'a8616645',
    'db': 'test',
    'charset': 'utf8mb4'
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'dytt (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'

USER_AGENTS = [
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5"]

PROXIES = [
{'ip_port':'223.112.84.30:3128', 'user_passwd': ''},
{'ip_port':'114.115.140.25:3128', 'user_passwd': ''},
{'ip_port':'118.178.228.175:3128', 'user_passwd': ''},
{'ip_port':'112.17.65.50:3128', 'user_passwd': ''},
{'ip_port':'140.143.90.197:1080', 'user_passwd': ''},
{'ip_port':'103.244.252.242:3128', 'user_passwd': ''},
{'ip_port':'114.115.148.181:3128', 'user_passwd': ''},
{'ip_port':'139.196.17.203:8080', 'user_passwd': ''},
{'ip_port':'123.206.58.129:1080', 'user_passwd': ''},
{'ip_port':'123.206.70.19:1080', 'user_passwd': ''},
{'ip_port':'114.115.217.39:3128', 'user_passwd': ''},
{'ip_port':'123.207.218.139:8080', 'user_passwd': ''},
{'ip_port':'123.207.55.239:1080', 'user_passwd': ''},
{'ip_port':'123.207.58.85:1080', 'user_passwd': ''},
{'ip_port':'103.12.69.55:1080', 'user_passwd': ''},
{'ip_port':'139.198.6.166:3128', 'user_passwd': ''},
{'ip_port':'123.207.154.239:1080', 'user_passwd': ''},
{'ip_port':'139.199.172.100:3128', 'user_passwd': ''},
{'ip_port':'139.199.199.222:8080', 'user_passwd': ''},
{'ip_port':'117.48.199.20:3128', 'user_passwd': ''},
{'ip_port':'139.224.118.55:3128', 'user_passwd': ''},
{'ip_port':'139.224.130.225:3128', 'user_passwd': ''},
{'ip_port':'139.224.131.100:1080', 'user_passwd': ''},
{'ip_port':'139.199.201.27:808:', 'user_passwd': ''},
{'ip_port':'120.52.73.173:8080', 'user_passwd': ''},
{'ip_port':'139.196.243.30:8080', 'user_passwd': ''},
{'ip_port':'112.17.14.27:8080', 'user_passwd': ''},
{'ip_port':'139.196.140.130:3128', 'user_passwd': ''},
{'ip_port':'123.206.93.108:8081', 'user_passwd': ''},
{'ip_port':'123.207.149.64:8080', 'user_passwd': ''},
{'ip_port':'112.16.154.190:808:', 'user_passwd': ''},
{'ip_port':'203.19.33.100:808:', 'user_passwd': ''},
{'ip_port':'123.207.10.11:1080', 'user_passwd': ''},
{'ip_port':'112.17.14.39:8080', 'user_passwd': ''},
{'ip_port':'123.206.75.11:3128', 'user_passwd': ''},
{'ip_port':'159.226.101.55:8080', 'user_passwd': ''},
{'ip_port':'123.207.226.100:808:', 'user_passwd': ''},
{'ip_port':'139.196.154.31:808:', 'user_passwd': ''},
{'ip_port':'118.193.23.162:3128', 'user_passwd': ''},
{'ip_port':'112.8.71.142:9999', 'user_passwd': ''},
{'ip_port':'123.207.174.204:808:', 'user_passwd': ''},
{'ip_port':'120.219.110.82:9999', 'user_passwd': ''},
{'ip_port':'112.8.62.76:9999', 'user_passwd': ''},
{'ip_port':'112.8.235.53:9999', 'user_passwd': ''},
{'ip_port':'112.16.110.169:9999', 'user_passwd': ''},
{'ip_port':'123.206.184.191:8080', 'user_passwd': ''},
{'ip_port':'139.196.210.55:1080', 'user_passwd': ''},
{'ip_port':'139.196.254.126:1080', 'user_passwd': ''}
]
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'dytt.middlewares.DyttSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    # 'dytt.middlewares.MyCustomDownloaderMiddleware': 543,
    'dytt.middlewares.RandomUserAgent': 1,
    # 'dytt.middlewares.RandomProxy': 100,
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'dytt.pipelines.DyttPipeline': 300,
#     'dytt.pipelines.TestPipeline': 100,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
