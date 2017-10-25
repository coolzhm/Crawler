# -*- coding: utf-8 -*-
import urllib.request

for i in range(1, 100):
    try:
        file = urllib.request.urlopen("http://yum.iqianyue.com", timeout=0.1)
        data = file.read()
        print(len(data))
    except Exception as e:
        print("异常：-->" + str(e))
