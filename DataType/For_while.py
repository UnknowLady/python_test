#!/user/bin/python3
#coding=utf-8

#循环相关学习笔记

#概念：
    #1、python循环语句有for 和 while
    #2、使用缩进划分语句块，相同缩进数的语句在一起组成一个语句块
    #3、在python中没有do..while语句

# while循环实例：计算1-100之间的总和
'''
n = 100         #设置n为100

sum = 0         #初始化sum
counter = 1     #默认数字为1
while counter <= n:         
    sum = sum + counter     
    counter += 1            
print("sum of 1 until %d: %d" %(n, sum) )
'''
# for语句，用以遍历任意序列的项目，如一个列表或者一个字符串
'''
languages = ["C","c++","c#","java"]
for x in languages:
    print(x)
'''
# for语句，下例使用了break语句，break语句用于跳出当前循环体
'''
languages = ["C","c++","c#","ipad","java"]
for x in languages:
    if x =="ipad":              #执行脚本后，在循环到ipad时会跳出循环体
        print("iphone不属于编程语言，跳出循环体")
        break
    print("编程语言有"+ x)
else:
    print("这里边都是编程语言")

print("最后，完成")
'''

# range()函数：如果需要遍历数字序列就可以用到该range()内置函数，它会生成数列。如下：
'''
for i in range(4):
    print(i)        #输出0，1，2，3     规则为包前不包后

for i in range(5,9):    #指定区间的值
    print(i)        #输出5，6，7，8     规则为包前不包后

for i in  range(0,10,3):     #依次输出0到10之间，每次增量为3的数字
    print(i)    #输出0，3，6，9

for i in  range(-10,-100,-30):     #依次输出-10到-100之间，每次增量为-30的数字
    print(i)    #输出-10，-40，-70
'''

#range()函数，结合range()和len()函数遍历一个序列的索引，如下：
'''
language = ["C","C++","C#","java"]
for i in range(len(language)):
    print(i, language[i])
'''
#使用range()函数来创建列表
'''
>>> list(range(5))
[0, 1, 2, 3, 4]
'''

#break 和 continue语句以及循环中的else子句
'''
    注：break可以跳出for和while的循环体，如果从for和while循环中中止，则else将不会被执行
    注：continue被用来告诉python跳过当前循环块中的剩余语句，然后继续执行下一轮循环
    注：循环中的else子句，在无穷尽列表（以for循环）或条件为假（以while循环）终止时被执行
        但循环被break终止时则不执行。
'''
#举例：在指定范围内2-10之间寻找质数（质数是指大于1的自然数中，除了1和它本身以外不再被其他数整除）
'''
for a in range(2,10):        #迭代2-10之间的数字，为2，3，4，5，6，7，8，9
    for x in range(2,a):     #根据因子迭代
        if a % x == 0:      #确定因子
            # print(a,'非质数，因为等于',x,'*',a//x)     
            break       #跳出当前循环
    else:       #循环的else部分
        print(a,'是质数')    
'''

#pass语句：pass语句是空语句，时为了保持程序结构的完整性
#Pass不做任何事情，一般用作占位语句
#pass实例:输出puthon的每个字母
for i in 'python':
    if i == 'h':
        pass
        print('这是pass块')
    print('当前字母：', i)
print("bye!")




