#!/user/bin/python3
#coding=utf-8

#这个案例为python逻辑运算符的操作

'''
概念：python语言支持逻辑运算符
#运算符and ——> 布尔“与”：如果x为False，x and y 返回False，否则它返回y的计算值
#运算符or  ——> 布尔“或”：如果x是True，它返回x的值，否则它返回y的计算值
#运算符not ——> 布尔“非”：如果x为True，返回False。如果x为False，它返回True。
'''

a = 10
b = 20
#逻辑表达式 (a and b)
if ( a and b ):      
    print("1、变量 a 和 b 都为True")
else:
    print("1、变量 a 和 b 有一个不为True")

#逻辑表达式 (a or b)
if ( a or b ):
    print("2、变量 a 和 b 都为True，或其中一个变量为 True")
else:
    print("2、变量 a 和 b 有一个不为True")

#修改变量a的值
a = 0
if ( a and b ):      
    print("3、变量 a 和 b 都为True")
else:
    print("3、变量 a 和 b 有一个不为True")

if ( a or b ):
    print("4、变量 a 和 b 都为True，或其中一个变量为 True")
else:
    print("4、变量 a 和 b 有一个不为True")

#逻辑表达式 not(a and b)
if not( a and b ):
    print("5、变量 a 和 b 都为False，或其中一个变量为 False")
else:
    print("5、变量 a 和 b 都为True")