#!/user/bin/python3
#coding=utf-8

#循环相关学习笔记

#概念：
    #1、python循环语句有for 和 while
    #2、使用缩进划分语句块，相同缩进数的语句在一起组成一个语句块
    #3、在python中没有do..while语句

# while循环实例：计算1-100之间的总和

n = 100         #设置n为100

sum = 0         #初始化sum
counter = 1     #默认数字为1
while counter <= n:         
    sum = sum + counter     
    counter += 1            
print("sum of 1 until %d: %d" %(n, sum) )
