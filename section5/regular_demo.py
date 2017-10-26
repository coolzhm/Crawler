# -*- coding: utf-8 -*-
print(
    '''
    *********** 正则表达式常见实例解析 *************
    '''
)

print('''------------------------------- 1.匹配.com或.cn后缀的URL网站 -------------------------------''')
import re

pattern = "[a-zA-Z]+://[^\s]*[.com|.cn]"
string = "<a href='http://www.baidu.com'>百度首页</a>"
result = re.search(pattern, string)
print(result)

print('''------------------------------- 2.匹配电话号码 -------------------------------''')
pattern = "\d{4}-\d{7}|\d{3}-\d{8}"  # 匹配电话号码的正则表达式
string = "021-6728263653682382265236"
result = re.search(pattern, string)
print(result)


print('''------------------------------- 3.匹配电子邮箱地址 -------------------------------''')
pattern = "\w+([.+-]\w+)*@\w+([.-]\w+)*\.\w+([.-]\w+)*"  # 匹配电子邮箱的正则表达式
string = "<a href='http://www.baidu.com'>百度首页</a><br>" \
         "<a href='mailto:c-e+o@iqi-anyue.com.cn'>电子邮箱地址</a>"
result = re.search(pattern, string)
print(result)


