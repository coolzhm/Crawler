# -*- coding: utf-8 -*-
'''
多线程爬虫
'''
import threading
from time import sleep

class A(threading.Thread):
    def __init__(self):
        # 初始化该线程
        threading.Thread.__init__(self)

    def run(self):
        # 该线程要执行的程序内容
        for i in range(10):
            print("我是线程A--【{0}】-->>>>>>>>".format(i))
            sleep(1)


class B(threading.Thread):
    def __init__(self):
        # 初始化该线程
        threading.Thread.__init__(self)

    def run(self):
        # 该线程要执行的程序内容
        for i in range(10):
            print("我是线程B--【{0}】-->>>>>>>>".format(i))
            sleep(1)

#实例化线程A为t1
t1=A()
#启动线程t1
t1.start()

#实例化线程B为t2
t2=B()
#启动线程t2
t2.start()