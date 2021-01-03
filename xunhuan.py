# 循环

# while
'''
flag = 1

while (flag): print ('欢迎访问教程!')

print ("Good bye!")
'''

# for循环
'''
sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")
'''

# range函数
'''
>>>for i in range(5,9) :
    print(i)
 
    
5
6
7
8
>>>
'''

'''
>>>for i in range(0, 10, 3) :
    print(i)
 
    
0
3
6
9
>>>
'''

'''
>>>a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
>>> for i in range(len(a)):
...     print(i, a[i])
... 
0 Google
1 Baidu
2 Runoob
3 Taobao
4 QQ
>>>
'''

'''
for letter in 'Runoob': 
   if letter == 'o':
      pass
      print ('执行 pass 块')
   print ('当前字母 :', letter)
'''
'''
当前字母 : R
当前字母 : u
当前字母 : n
执行 pass 块
当前字母 : o
执行 pass 块
当前字母 : o
当前字母 : b
Good bye!
'''