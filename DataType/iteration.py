#!/user/bin/python3
#coding=utf-8

#迭代器与生成器相关学习笔记  

#迭代器——概念   迭代（iteration）
    #迭代是python最强大的功能之一，是访问集合元素的一种方式
    #迭代器是一个可以记住遍历位置的对象
    #迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完为止。迭代器只往前不往后
    #迭代器有两个方法，分别是iter()和next()
    #字符串，列表或元组对象都可以用于创建迭代器

#例子:创建迭代器
'''
    >>> list = [1,2,3,4]
    >>> it = iter(list)         #创建迭代器的对象
    >>> print (next(it))        #输出迭代器的下一个元素
    1
    >>> print(next(it))
    2
    >>>
'''
#例子：迭代器对象可以用for语句进行遍历
'''
list = [1, 2, 3, 4]
it = iter(list)
for x in it:
    print(x, end="")    # end=""  意思是取消换行
'''
#例子：迭代器对象可以用next()函数来进行遍历
'''
import sys      #引入sys模块

list = [1, 2, 3, 4]
it =iter(list)      #创建迭代器对象

while True:         #无线循环
    try:
        print(next(it))     #依次输出迭代期的下一个元素
    except StopIteration:   #迭代器没有更多的值时
        sys.exit()          #解释器请求退出
'''

#生成器——概念   生成器（generator）

    #在python中，使用了yield的函数被称为生成器
    #跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作
    #在调用生成器的运行过程中，每次遇到yield时函数就会暂停并保存当前所有的运行信息，返回yield的值，并在下一次执行next()方法时从当前位置继续运行
    #调用一个生成器函数，返回的是一个迭代器对象

#实例：用yield实现斐波那契数列

import sys

def fibonacci(n):   #生成器函数——斐波那契
    a, b, couter = 0, 1, 0
    while True:
        if (couter > n):
            return
        yield a
        a, b = b, a+b
        couter += 1
f = fibonacci(10)   #f是一个迭代器，由生成器返回生成
while True:
    try:
        print(next(f), end=" ")    
    except StopIteration:
        sys.exit()