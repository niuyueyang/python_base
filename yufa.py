# python基础语法


# 第一个注释
print ("Hello, Python!") # 第二个注释

# 第一个注释
# 第二个注释

'''
第三注释
第四注释
'''

"""
第五注释
第六注释
"""

print ("Hello, Python!")

# python最具特色的就是使用缩进来表示代码块，不需要使用大括号 {} 。
# 缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数。实例如下：
if True:
    print ("True")
else:
    print ("False")


# Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠(\)来实现多行语句，例如：
total = 'item_one' + \
        'item_two' + \
        'item_three'

# python基本类型
# 数字(Number)类型
'''
python中数字有四种类型：整数、布尔型、浮点数和复数。
int (整数), 如 1, 只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
bool (布尔), 如 True。
float (浮点数), 如 1.23、3E-2
complex (复数), 如 1 + 2j、 1.1 + 2.2j
'''
# 字符串(String)
# python中单引号和双引号使用完全相同。
# 使用三引号(''',""")可以指定一个多行字符串。
# 转义符 '\'
# 反斜杠可以用来转义，使用r可以让反斜杠不发生转义。。 如 r"this is a line with \n" 则\n会显示，并不是换行。
# 按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string。
# 字符串可以用 + 运算符连接在一起，用 * 运算符重复。
# Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
# Python中的字符串不能改变。
# Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。
# 字符串的截取的语法格式如下：变量[头下标:尾下标:步长]
word = '字符串'
sentence = "这是一个句子。"
paragraph = """这是一个段落，
可以由多行组成"""
print(paragraph)

str = 'Runoob'

print(str)  # 输出字符串 Runoob
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符 Runoo
print(str[0])  # 输出字符串第一个字符 R
print(str[2:5])  # 输出从第三个开始到第五个的字符 noo
print(str[2:])  # 输出从第三个开始后的所有字符 noob
print(str[1:5:2])  # 输出从第二个开始到第五个且每隔两个的字符 uo
print(str * 2)  # 输出字符串两次 RunoobRunoob
print(str + '你好')  # 连接字符串 Runoob你好

print('------------------------------')

print('hello\nrunoob')  # 使用反斜杠(\)+n转义特殊字符
'''
hello
runoob
'''
print(r'hello\nrunoob')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义 hello\nrunoob

input("\n\n按下 enter 键后退出。")

import sys;
x = 'runoob';
sys.stdout.write(x + '\n')

x = "a"
y = "b"
# 换行输出
print(x)
print(y)
'''
a
b
'''

print('---------')
# 不换行输出
print(x, end = " ")
print(y, end = " ")
'''
a b 
'''

#导入
'''
在 python 用 import 或者 from...import 来导入相应的模块。
将整个模块(somemodule)导入，格式为： import somemodule
从某个模块中导入某个函数,格式为： from somemodule import somefunction
从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
将某个模块中的全部函数导入，格式为： from somemodule import *
'''

