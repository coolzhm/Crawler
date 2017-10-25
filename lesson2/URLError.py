# -*- coding: utf-8 -*-
# 异常处理器
'''
常见状态码以及对应含义
200 OK
    一切正常
301 Moved Permanently
    重定向到新URL，永久性
302 Found
    重定向到临时的URL，非永久性
304 NotModified
    请求的资源未更新
400 Bad Request
    非法请求
401 Unauthorized
    请求未经授权
403 Forbidden
    禁止访问
404 Not Found
    没有找到对应页面
500 Internal Server Error
    服务器内部出现错误
501 Not Implemented
    服务器不支持实现请求所需要的功能
'''
# 实例1
import urllib.request
import urllib.error

try:
    urllib.request.urlopen("http://blog.csdn.net")
except urllib.error.URLError as e:
    print(e.code)
    print(e.reason)

'''
实际异常中不知道HTTPError能否处理，所以要在后面加个URLError，此时若发生连接不上服务器、
远程URL不存在、无网络等异常时也能够处理

'''
try:
    urllib.request.urlopen("http://blog.baidusss.net")
except urllib.error.HTTPError as e:
    print(e.reason)
except urllib.error.URLError as e:
    print(e.reason)

'''
实际中可以用URLError代替HTTPError直接运行，但是前者不存在e.code，所以需要优化
'''
try:
    urllib.request.urlopen("http://blog.csdn.net")
except urllib.error.URLError as e:
    if hasattr(e, 'code'):
        print(e.code)
    if hasattr(e, 'reason'):
        print(e.reason)
