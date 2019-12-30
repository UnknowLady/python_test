#!/user/bin/python3
#coding=utf-8

#这个案例为python成员运算符的操作

#基本概念
'''
python也支持成员运算符，在下面的实例中包含了一系列的成员，包括字符串、列表、元组等
# 运算符 in：——> 如果在指定序列中找到值返回True，否则返回False。
# 运算符 not in：——> 如果在指定序列中没有找到值返回True，否则返回False。
'''

#实例

a = 10
b = 20
list = [1,2,3,4,5]

if( a in list ):
    print("1、变量 a 在给定的列表 list 中")
else:
    print("1、变量 a 不在给定的列表 list 中")

if ( b not in list ):
    print("2、变量 b 不在给定的列表 list 中")
else:
    print("2、变量 b 在给定的列表 list 中")

#修改变量a的值
a = 2

if (a in list):
    print("3、变量 a 在给定的列表 list 中")
else:
    print("3、变量 a 不在给定的列表 list 中")
    