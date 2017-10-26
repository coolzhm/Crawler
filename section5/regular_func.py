# -*- coding: utf-8 -*-
print(
    '''
    *********** 正则表达式的常见函数 *************
    '''
)

print('''------------------------------- 1.re.match()函数 -------------------------------''')
print(
    '''
    如果想从源字符串的起始位置匹配到一个模式，我们可以使用re.match()函数
    '''
)
import re

string = "apythonhellomypythonhispythonourpythonend"
pattern = ".python."
result = re.match(pattern, string)
result2 = re.match(pattern, string).span()
print(result)
print(result2)

print('''------------------------------- 2.re.search()函数 -------------------------------''')
print(
    '''
    re.search()与re.match()函数最大的不同是，re.match()函数从源字符串的开头进行匹配，
    而re.search()函数会在全文中进行检索并匹配，如下例子
    '''
)
import re

string = "hellomypythonhispythonourpythonend"
pattern = ".python."
result = re.match(pattern, string)
result2 = re.search(pattern, string)
print(result)
print(result2)

print('''------------------------------- 3.全局匹配re.compile()函数 -------------------------------''')
print(
    '''
    思路如下：
    1）使用re.compile()对正则表达式进行预编译
    2）变异后，使用findall（）根据正则表达式从源字符串中将匹配的结果全部找出
    '''
)
string = "hellomypythonhispythonourpythonend"
pattern = re.compile(".python.")  # 预编译
result = pattern.findall(string)  # 找出符合模式的所有结果
print(result)

print('''------------------------------- 4.re.sub()函数 -------------------------------''')
print(
    '''
    re.sub(pattern,rep,string,max)
    使用re.sub()这个函数，会根据正则表达式pattern，从源字符串string查找复合模式的结果，
    并替换为字符串rep，最多可替换max次
    '''
)
string = "hellomypythonhispythonourpythonend"
pattern = "python."
result = re.sub(pattern, "php", string)  # 全部替换
result2 = re.sub(pattern, "php", string, 2)  # 最多替换2次
print(result)
print(result2)
