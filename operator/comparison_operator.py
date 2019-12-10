#!/user/bin/python3
#coding=utf-8

#这个案例为python比较运算符的操作
a = 21
b = 10
c = 0

if( a == b):  #等于 - 比较对象是否相等#
    print("1、a 等于 b")
else:
    print("1、a 不等于 b")

if( a != b):    #不等于 - 比较两个对象是否不相等
    print("2、a 不等于 b")
else:
    print("2、a 等于 b")

if( a < b):  #小于 - 返回x是否小于y。所有比较运算符返回1表示真，返回0表示假。
    print("3、a 小于 b")
else:
    print("3、a 大于等于 b")

if( a > b):  #大于 - 返回x是否大于y
    print("4、a 大于 b")
else:
    print("4、a 小于等于 b")


#修改变量a、b的值
a = 2
b = 3
if( a <= b):  #小于 - 返回x是否小于等于y
    print("5、a 小于等于 b")
else:
    print("5、a 大于 b")

if( a >= b):  #大于等于 - 返回x是否大于等于y
    print("6、a 大于等于 b")
else:
    print("6、a 小于 b")