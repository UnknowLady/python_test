#!/user/bin/python3
#coding=utf-8
#元组运算的相关笔记
# Python与列表List类似，元组创建很简单，只需要在括号中添加元素，并用逗号隔开即可。
'''
    #  Python与List的区别
    1、元组的元素不能修改；列表的元素可以修改
    2、元组使用小括号；列表使用方括号
'''
# 1、Tuple创建
'''
    tup0 =()    #创建空元组
    tup01 = (51,)   #元组只包含一个元素时，需要在元素后面增加逗号

    print("tup0:", tup0)
    print("tup01:", tup01[0])

#-----------------------------分割线---------------------------

    tup1 = ('baidu','google','1990','2020')
    tup2 = (1, 2, 3, 4)
    tup3 = "a", "b", "c","d"

    print("tup1:", tup1[0])
    print("tup2:", tup2[1:4])
    print("tup3:", tup3[:])
'''
# 2、Tuple修改  
    #·Tup元组中的元素值不允许修改，但可以对元组进行连接组合，如下实例
'''

    tup1 = (11, 22, 33)
    tup2 = ('abc', 'def')

        #tup1[0] = 111  非法操作，元组的元素不允许修改   

    tup3 = tup1 + tup2  #创建一个新元组，对 tup1 和 tup2 进行拼接

    print(tup3)
'''
    
# 3、Tuple删除
    #·Tup元组中的元素值不允许删除，但可以使用del语句删除整个元组。如下实例：
'''
    tup = ("IE","Chrome","Firefox",111)
    print (tup)
    del tup         #删除tup元组
    print("删除后的元组 tup ：")
    print(tup)      #成功删除后，输出变量会有未定义的异常信息
'''
# 4、Tuple运算符
    # ·和运算符一样，元组之间可以使用+（拼接组合）和*（复制）进行运算。运算后会生成新的元组。

    #(1)、计算元组个数
"""
        tup = (1,2,3)
        print(len(tup))
"""
    #(2)、元组连接
'''
        tup = (1, 2, 3,)
        tup1 = ('a', 'b', 'c')
        tup2 = tup + tup1
        print(tup2)
'''
    #(3)、元组复制
'''
        tup = ('hello!')
        tup1 = tup * 4
        print(tup1)
'''
    #(4)、检查元素是否在元组中
'''
    tup = ('baidu','google',1111,2222)
    tup1 =('baidu')

    if (tup1 in tup):
        print("tup1在元组tup中")
    else:
        print("tup1不在元组tup中")
'''
    #(5)、for迭代(遍历tup的元组成员，依次访问元组中的元素，最后打印出来)
'''
    tup = ('baidu','google',1111,2222)
    for x in tup:
        print (x)
'''
# 5、Tuple元组索引、截取
  #· 因为元组也是一个序列，所以可以访问元组中指定位置的元素，也可截取索引中的一段元素
'''
    >>> tup = ('baidu','google', 1111, 2222)    #第一步：创建元组tup
    >>> tup[0]          #第二步：访问序列0，也就是左边第一位元素
    'baidu'
    >>> tup[-1]         #第三步：访问序列最后一位，也就是倒数第一位（右边数起第一位）
    2222
    >>> tup[1:]         #最后：截取序列1之后一段元组，注意这里包含序列1哦
    ('google', 1111, 2222)
    >>>
''' 
# 5、Tuple元组内置函数
    #·元组包含了内置函数，以下分别为len(tuple)、max(tuple)、min(tuple)、tuple(seq)的说明及实例

    #(1)、计算元组个数  len(tuple)
'''
    >>> tup = ('baidu','google', 1111, 2222)    #创建元组
    >>> len(tup)    #计算个数
    4               #运行结果
'''    
    #(2)、返回元组中的最大值  max(tuple)
'''
    >>> tup =(1, 2, 3, 4, 111)  #创建元组
    >>> max(tup)    #返回最大值
    111             #运行结果
'''
    #(3)、返回元组中的最小值  min(tuple)
'''
    >>> tup =(1, 2, 3, 4, 111) #创建元组
    >>> min(tup)    #返回最小值
    1               #运行结果
'''
    #(4)、将列表换为元组  tuple(seq)
'''
    >>> list1 = ['baidu', 'google',360]     #创建列表list1
    >>> tup = tuple(list1)  #将列表list1转换为元组tup
    >>> tup                 #返回元组tup
    ('baidu', 'google', 360)    #tup结果
'''