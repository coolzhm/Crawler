# -*- coding: utf-8 -*-

import urllib.request

#代理地址可从此网站拷贝 http://www.xicidaili.com/nn/
def use_proxy(proxy_addr, url):
    proxy = urllib.request.ProxyHandler({'http': proxy_addr})
    opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(url).read().decode('utf-8')
    return data


proxy_addr = "118.114.77.47:8080"
data = use_proxy(proxy_addr, "http://www.baidu.com")
print(len(data))
