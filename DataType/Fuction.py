#!/user/bin/python3
#coding=utf-8

#Python 函数相关学习笔记  （函数：function）

#概念   
'''
    1、函数是组织好的，可以重复使用，用来实现单一或关联成功的代码段
    2、函数可提高应用的模块性，和代码的重复利用率。比如：python中有很多内建函数，比如print()
        用户可以自己创建函数，所以因此被称为自定义函数
'''

#关于函数的定义,有如下几个规则：
'''
    1、函数代码块以def关键字开头，后接函数标识符名称和圆括号()
    2、任何传入参数和自变量必须放在括号中间，圆括号之间可以用于定义参数
    3、函数的第一行语句可以选择性的使用文档字符串，用于存放函数说明
    4、函数内容以冒号起始，并且缩进。
    5、return[表达式expression]结束函数，选择性的返回一个值给调用方，不带表达式的return相当于返回None。

'''

#关于函数的语法
'''
def 函数名(参数名):
    函数体
'''    

#关于函数的实例1：  使用函数输出hello，world
'''
def hello( a ):
    print(a)
    return
print("hello,world")
'''
#关于函数的实例2：函数中带上参数变量,计算面积
'''
def area(width, height):        
    return width * height       

def print_welcome(name):        
    print("welcome", name)      
print_welcome("jing")

w = 10
h = 20
print("宽为：",w,  "高为：",h,  "面积等于：",area(w,h) )
'''

#函数调用：定义一个函数：给函数一个名称，指定函数里包含的参数和代码块结构
    #函数基本结构完成后，可通过另一个函数调用执行，也可以直接从python命令提示符执行
'''
#实例1：调用printme()函数

def printme( str ):     #定义函数printme
    print(str)      #打印任何传入的字符串
    return          #调用函数
printme("我要调用用户自定义的函数")
printme("我要再一次调用这个函数")
'''

#参数传递：
#1、在python中，类型属于对象，变量是没有类型的。
'''
#举例：
a = [1, 2, 3]   #[1,2,3]在这里属于list类型
a = "xxx"       #"xxx"属于string类型
#但以上的两个变量a是没有类型的，它仅仅是对象的引用，类似于指针。可以指向list类型对象也可以指向string类型对象
'''
#2、可更改对象：mutable； 不可更改对象immutable
'''
#在python中，strings, tuples和numbers是不可更改的对象，而list和dict等则是可修改的对象

#不可变类型：
a=5     #先赋值5
a=10    #再赋值10
print(a)  #实际输出会新生成一个int值对象10，再让a指向它。而5丢弃，这里不是改变a的值，而是相当于新生了a

#可变类型：
la = [1, 2, 3, 4]   #先赋值la=1,2,3,4
la[2]=5             #再赋值la[2]=5
print(la) #实际再赋值时将la的第三个值3更改成了5，本身la没有动，只是其中的一部分值被修改了

#python的参数传递：
#不可变类型：如 ——> fun(a)内部修改a的值，只是修改另一个赋值的对象，不会影响到a本身

def changeInt(a):
    a = 10
b = 2   
changeInt(b)    
print (b)   #结果为2

#可变类型：所有参数再python里都是按引用传递。如果在函数里修改了参数，那么在调用这个函数里，原始参数会发生改变

def changeme( mylist):
    mylist.append([1,2,3,4])
    print("函数内取值为：", mylist)
    return

#调用changeme函数
mylist = [10,20,30]
changeme(mylist)
print("函数外取值为：", mylist)
'''
#参数：以下是调用函数时可以使用的正式参数类型

# ——> 1、必须参数：需要以正确的顺序传入参数。调用时的数量必须和声明时的一样
'''
def printme(str):
    "打印任何传入的字符串"
    print (str)
    return
#printme()   调用printme函数，不加参数会报错哦
printme("调用printme函数，不加参数会报错哦")
'''
# ——> 2、关键字参数:函数调用可以使用关键字参数来确定传入的参数值；另顺序与声明不一致时，可自动用参数名匹配到参数值
'''
def printme(str):
    "打印任何传入的字符串"
    print (str)
    return
printme(str= "关键字参数")   

def printinfo(name, age):
   "打印任何传入的字符串"
   print("名字：", name)
   print("年龄:", age)
   return
#调用printinfo函数
printinfo( age=20,  name="jing")    
'''
# ——> 3、默认参数：如果没有传递蚕食，则会使用默认参数
'''
def printinfo(name, age=20):
   "打印任何传入的字符串"
   print("名字：", name)
   print("年龄:", age)
   return
#调用printinfo函数
printinfo( age=50,  name="jing")   
print("--------------------")
printinfo(name="xixi")
'''
# ——> 4、不定长参数:当需要一个函数能处理比当初声明时更多的参数，这些参数叫不定长参数
#语法1：参数带一个星号
'''
def functionName([formal_args,] *var_args_tuple):   #加了星号*的参数会以元组的形式导入，存放所有未命名的变量参数
    "函数文档字符串"
    function_suite
    return[expression]
#加了星号*的参数会以元组的形式导入，存放所有未命名的变量参数。实例：
def printinfo(arg1,*var_tuple):
    print("输出")
    print(arg1)
    print(var_tuple)
printinfo(70,60,50)

#如果在函数调用时没有指定参数，它就是一个空元组。我们也可以不向函数传递未命名的变量。如下实例：
def printinfo(arg1,*var_tuple):
    print("输出")
    print(arg1)
    for var in var_tuple:
        print(var)
    return
printinfo(10)
printinfo(70,60,50)
'''
#语法2：参数带两个星号
'''
def functionName([formal_args,] **var_args_tuple):   #加了两个星号**的参数会以字典的形式导入
    "函数文档字符串"
    function_suite
    return[expression]

def printinfo(arg1, **var_dict):
    print("输出")
    print(arg1)
    print(var_dict)
printinfo(1,a=2,b=3)
'''
#语法3：参数中星号单独出现
'''
def f(a,b,*,c):
    print(a+b+c)
    return
#f(1,2,3)   #报错，如果单独出现带星号，*后的参数必须用关键字传入。
f(1,2,c=3)  #正确，输出结果为6
'''
#匿名函数：python使用lambda来创建匿名函数。所谓匿名，就是不再使用def语句这样的标准的形式来定义一个函数
#概念：
'''
    1、lambda只是一个表达式，函数体要比def简单
    2、lambda的主体时一个表达式，而不是代码块。仅仅能在lambda表达式中封装有限的逻辑进去
    3、lambda函数拥有自己的命名空间，且不能访问自己参数列表之外或全局空间里的参数
    4、虽然lambda函数看起来只能写一行，却不等同c或c++内联函数后者的目的是调用小函数时不占用栈内存从而增加运行效率。
'''
#语法：lambda函数的语法只包含一个语句 ——> lambda [arg1[,arg2,...argn]]:expression
#实例
sum = lambda arg1, arg2: arg1 + arg2

print("相加后的值为 ：", sum(10,20))
print("相加后的值为 ：", sum(20,20))