# -*- coding: utf-8 -*-
print(
    '''
    *********** 正则表达式的基础知识 *************
    '''
)

print('''------------------------------- 1.原子 -------------------------------''')
# (1)、普通字符作为原子
print('(1)、普通字符作为原子')
import re

pattern = "yue"  # 普通字符作为原子
string = "http://yum.iqianyue.com"
result1 = re.search(pattern, string)
print(result1)

# (2)、非打印字符作为原子
print('(2)、非打印字符作为原子')
import re

pattern = "\n"  # 普通字符作为原子
string = '''http://yum.iqianyue.com
http://baidu.com'''
result1 = re.search(pattern, string)
print(result1)

# (3)、通用字符作为原子
print('(3)、通用字符作为原子')
print(
    '''
    \w 匹配任意一个字母、数字或下划线
    \W 匹配任意一个除字母、数字或下划线以外任意一个其他字符
    \d 匹配任意一个十进制数
    \D 匹配除十进制数以外任意一个其他字符
    \s 匹配任意一个空白字符
    \S 匹配除空白字符以外任意一个其他字符
    ''')
import re

pattern = "\w\dpython\w"  # 普通字符作为原子
string = "abcdfphp345pythony_py"
result1 = re.search(pattern, string)
print(result1)

# (4)、原子表
print('(4)、原子表')
import re

pattern1 = "\w\dpython[xyz]\w"
pattern2 = "\w\dpython[^xyz]\w"
pattern3 = "\w\dpython[xyz]\W"
string = "abcdfphp345pythony_py"
result1 = re.search(pattern1, string)
result2 = re.search(pattern2, string)
result3 = re.search(pattern3, string)
print(result1)
print(result2)
print(result3)

print('''------------------------------- 2.元字符 -------------------------------''')
print(
    '''
    .   匹配除换行符以外的任意字符
    ^   匹配字符串的开始位置
    $   匹配字符串的结束位置
    *   匹配0次、1次或多次前面的原子
    ?   匹配0此或1次前面的原子
    +   匹配1次或多次前面的原子
    {n} 前面的原子恰好出现n次
    {n,}    前面的原子至少出现n次
    {n,m}   前面的原子至少出现n次，至多出现m次
    |   模式选择符
    ()  模式单元符
    ''')
# （1）、任意匹配元字符
print('（1）、任意匹配元字符')
import re

pattern = ".python..."
string = "abcdfphp345pythony_py"
result = re.search(pattern, string)
print(result)

# (2)、边界限制元字符
print('(2)、边界限制元字符')
import re

pattern1 = "^abd"
pattern2 = "^abc"
pattern3 = "py$"
pattern4 = "ay$"
string = "abcdfphp345pythony_py"
result1 = re.search(pattern1, string)
result2 = re.search(pattern2, string)
result3 = re.search(pattern3, string)
result4 = re.search(pattern4, string)
print(result1)
print(result2)
print(result3)
print(result4)

# (3)、限定符
print('(3)、限定符')
import re

pattern1 = "py.*n"
pattern2 = "cd{2}"
pattern3 = "cd{3}"
pattern4 = "cd{2,}"
string = "abcdddfphp345pythony_py"
result1 = re.search(pattern1, string)
result2 = re.search(pattern2, string)
result3 = re.search(pattern3, string)
result4 = re.search(pattern4, string)
print(result1)
print(result2)
print(result3)
print(result4)

# (4)、模式选择符
print('(4)、模式选择符')
import re

pattern = "python|php"
string = "abcdfphp345pythony_py"
result1 = re.search(pattern, string)
print(result1)

# (5)、模式单元符
print('(5)、模式单元符')
import re

pattern1 = "(cd){1,}"
pattern2 = "cd{1,}"
string = "abcdcdcdcdcdfphp345pythony_py"
result1 = re.search(pattern1, string)
result2 = re.search(pattern2, string)
print(result1)
print(result2)

print('''------------------------------- 3.模式修正 -------------------------------''')
print(
    '''
    I   匹配时忽略大小写
    M   多行匹配
    L   做本地化识别匹配
    U   根据Unicode字符及解析字符
    S   让.匹配包括换行符，即用了该模式修正后，“.”匹配就可以匹配任意的字符了
    '''
)
import re

pattern1 = "python"
pattern2 = "python"
string = "abcdfphp345Pythony_py"
result1 = re.search(pattern1, string)
result2 = re.search(pattern2, string, re.I)
print(result1)
print(result2)

print('''------------------------------- 4.贪婪模式与懒惰模式 -------------------------------''')
print(
    '''
    贪婪模式的核心点就是尽可能多匹配
    懒惰模式的核心点就是尽可能少匹配
    通常情况下，如果我们想在某些字符间匹配任意字符，想“p.*y”这样写没有任何的语法错误，
    这个时候默认是使用贪婪模式的，要转化为懒惰模式，需在对应的“.*”后面加上“?”，方可转化为懒惰模式
    '''
)
import re

pattern1 = "p.*y"  # 贪婪模式
pattern2 = "p.*?y"  # 懒惰模式
string = "abcdfphp345pythony_py"
result1 = re.search(pattern1, string)
result2 = re.search(pattern2, string)
print(result1)
print(result2)
