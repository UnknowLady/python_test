#!/user/bin/python3
#coding=utf-8

#这个案例为python身份运算符的操作

#基本概念
'''
身份运算符一般用于比较两个对象的存储单元

# 运算符 is：——>is 是判断两个标识符是否引用自一个对象
# 运算符 is not：——>is not是判断两个标识符是否引用自不同对象

'''

#实例
a = 20
b = 20

if( a is b):
    print("1、a 和 b 有相同的标识")
else:
    print("1、a 和 b 没有相同的标识")

if( id(a) == id(b)):
    print("2、a 和 b 有相同的标识")
else:
    print("2、a 和 b 没有相同的标识")

#修改变量b的值
b = 10

if( a is b):
    print("3、a 和 b 有相同的标识")
else:
    print("3、a 和 b 没有相同的标识")

if( a is not b):
    print("4、a 和 b 没有相同的标识")
else:
    print("4、a 和 b 有相同的标识")
