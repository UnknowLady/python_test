'''
#python 3中有六个标准的数据类型
number（数字）
string（字符串）
list（列表）
tuple（元组）
sets（集合）
dictionaries(字典)
'''
#python3支持int（整数） float（浮点数） bool（布尔） complex(复数)
'''
a, b, c, d = 20, 5.5, True, 4+3J
print(type(a), type(b), type(c), type(d))
'''

#列表List
#python中列表是可变的，这是他区别于字符串和元组的重要特点。
#列表可以修改，而字符串和元组则不能
'''
概念类：

'''
#方法：list.append(x)
#描述：把一个元素添加到列表的结尾，相当于 a[len(a):]=[x]
#实例：
'''
a = [111,]
a.append(2)
print(a)

#结果：a为[111,2]
'''

#方法：list.extend(L)
#描述：通过添加指定列表中的所有元素赖扩充列表，相当于a[len(a):]=L

#方法：list.insert(i,x)
#描述：在指定位置插入一个元素，第一个参数是准备插入其前面的那个元素的索引。例如：a.insert(0,x)会插入到整个列表之前，而a.insert(len(a),x)相当于a.append(x).
#实例：
'''
a = [111,2]
a.insert(1,-1)
print(a)

#结果：a为[111, -1, 2]
'''
#方法：list.remove(X)
#描述:删除列表中值为x的第一个元素，如果没有这样的元素，就会返回一个错误
#实例：
'''
a = [111,2]
a.remove(111)
print(a)
#结果：a为[2]
'''
#方法：list.pop([li])
#描述：从列表的指定位置删除元素，并将其返回。如果没有指定索引，a.pop()返回最后一个元素，元素随即从列表中被删除
        #（方法中i两边的方括号表示这个参数是可选的，而不是要求你输入一对方括号）

#方法：list.clear()
#描述：移除列表中的所有相，等于 del a[:]
#实例：
'''
a = [111,-5]
a.clear()
print(a)
#结果：a为[]
'''
#方法：list.index(x)
#描述：返回列表中第一个值为x的元素的索引，如果没有匹配的元素就会返回一个错误
'''
a = [66.25, 333, -1, 333, 1, 1234.5, 333]
a.index(66.25)
'''
#方法：list.count(x)
#描述：返回x在列表中出现的次数
#实例：
'''
a = [66.25, 333, 333, 1, 1234.5]
print(a.count(333),a.count(1),a.count('x'))

#结果：2 1 0
'''

#方法：list.sort()
#描述：对列表中的元素进行排序
#实例
'''
a = [66.25, 333, 333, 1, 1234.5]
a.sort()
print(a)

#结果：[1, 66.25, 333, 333, 1234.5]
'''
#方法：list.reverse()
#描述：倒排列表中的元素

#方法：list.copy()
#描述：返回列表的浅复制，等于a[:]


#将列表当作堆栈使用
'''
列表方法使得列表可以很方便的作为一个堆栈使用，最先进入的元素最后一个被释放。（后进先出）
用append()方法可以把一个元素添加到堆栈顶。
用不指定索引的pop()方法可以把一个元素从堆栈顶释放出来
'''

#实例
'''
stack = [1,2,3]         #定义一个列表，元素为1，2，3
stack.append(4)         #把元素4添加到列表的结尾
stack.append(5)         #把元素5添加到列表的结尾
print(stack)            #输出现在的列表为[1,2,3,4,5]
print(stack.pop())      #释放最后进入列表的元素，也就是5
print(stack)            #现在的列表为[1,2,3,4]
print(stack.pop())      #释放列表最后一个元素，也就是4
print(stack)            #现在的列表为[1,2,3]
print(stack.pop())      #释放列表最后一个元素，也就是3
print(stack)            #现在的列表为[1,2]
'''

#将列表当作队列使用
'''
把列表当作队列，在队列里第一个加入的元素，第一个取出（先进先出）
'''
#实例
'''
from collections import deque
queue = deque(['xxx','sss','hhh'])      #定义队列的元素为xxx,sss,hhh
queue.append('ni')                      #给队列末尾增加一个元素ni
queue.append('hao')                     #给队列末尾增加一个元素hao
print(queue.popleft())                  #输出第一个元素，取出来xxx
print(queue.popleft())                  #接着输出剩下列表里第一个元素，取出sss
print(queue)                            #最后列表里还有的元素有：hhh,ni,hao
'''

#列表推导式
'''
1、提供从序列创建列表的有效途径，一些操作应用于某个序列的每个元素，用其获得的结果作为生成新列表的元素。
或根据判断条件创建子序列
2、每个列表的推导式都在for之后跟一个表达式，然后有零到多个for或if子句
返回结果是一个根据表达从气候的for或if上下文环境中生成出来的列表
3、另，如果希望表达式推导出一个元组，就必须使用括号
'''
#实例：
'''
var = [2, 4, 6]                 #定义列表
print([3*x for x in var])       #每个数值乘三，获得一个新的列表
print([[x,x**2] for x in var])  #每个数值求幂，用元组的方式输出
print([3*x for x in var if x >3])       #用if子句作为过滤器

fruit = ['banana','apple', 'pear','grape']      #定义列表
print([a.strip() for a in fruit])       #将列表里的每个元素逐一掉用

#其他使用技巧
var1 = [1,2,3]
var2 = [5,10,11]
print([x*y for x in var1 for y in var2])
print([x+y for x in var1 for y in var2])
print([var1[i]*var2[i] for i in range(len(var1))])
'''
#列表推导式也可以使用复杂表达式或嵌套函数
'''
print([str(round (355/113, i)) for i in range(1,6)])
'''
#嵌套列表解析
#概念：python的列表还可以嵌套，以下展示了3*4的矩阵列表
#实例：将3*4列表转换为4*3列表
matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
]

'''
#方法1：
print([[row[i] for row in matrix] for i in range(4)])   

#方法2：
transposed = []
for i in range(4):
        transposed.append([row[i] for row in matrix])
print(transposed)

#方法3：
transposed = []
for i in range(4):
        transposed_row = []
        for row in matrix:
                transposed_row.append(row[i])
        transposed.append(transposed_row)
print(transposed)
'''
#del语句：
# 使用del语句可以从一个聊表中以索引赖删除一个元素
#可以用del语句从列表中删除一个切割，或清空整个列表
'''
a = [-1, 1, 111, 666, 888, 999.9]
del a[0]        #删除第一个元素
print(a)
del a[2:4]      #剩下的列表中删除索引为2-4的元素
print(a)
del a[:]        #删除剩下此刻列表里的所有元素
print(a)
'''
#元组与序列
#元组由若干逗号分割的值组成，另：元组输出时总是有括号的，以便于正确表达嵌套关系
#在输入时可能有或没有阔号，不过括号通常是必须的
'''
t = (1, 2, 3, 'hello')
print(t[0])     #输出1
print(t)        #输出(1, 2, 3, 'hello')

u = t,(11,22,33)
print(u)        #输出((1, 2, 3, 'hello'), (11, 22, 33))
'''

#集合
#集合时一个无序不重复元素的集，基本功能包括关系测试和消除重复元素
#可以用大括号({})创建集合。另：如需要创建空集合，必须用set()而非{}；后者创建的时一个空的字典

'''
简单演示：


fruit = {'banana','apple','pear','grape','orange'}
if('orange'in fruit):
        print('true')
else:
        print('False')
#集合也支持推导式
f = {x for x in 'zxcvbnm' if x not in 'zxcvb'}
print(f)
'''

#字典:
# 1、序列是以连续的整数位索引；字典是以关键字为索引，关键字可以是任意不可变类型
# 2、理解字典的最佳方式是把它看作无序的键值对集合，同一个字典内，关键字互不相同
#一对大括号创建一个新的字典
'''
tel = {'wang':1111,'li':222}
tel['wang1'] = 5555
print(tel)
print(tel['li'])

del tel['li']
print(tel)

print(list(tel.keys())) #输出列表里的键

if 'zhao' in tel:
        print('true')
else:
        print('False')

if 'zhao' not in tel:
        print('yes')
'''

#构造函数dict()直接从键值对元组列表中构建字典
"""
'''列表推导式指定特定的键值对'''
a = dict([('zhang',111),('san',222),('li',333),('si',444)])
print(a)
'''字典推导可以用来创建任意键和值的表达式字典'''
b = {x:x**2 for x in (2,4,6)}
print(b)
'''使用关键字参数指定键值对'''
c = dict(zhang=111,li=222,wang=333)
print(c)
"""
#遍历技巧
#字典各种遍历时，关键字和对应的值可以用items()方法解读出来
'''
tel = {'wang':1111,'li':222}
for a, b in tel.items():
        print(a,b)
#wang 1111
#li 222
'''
#在序列中遍历时，索引位置和对应的值可以使用enumerate()函数同时得到
'''
for i,v in enumerate(['a','b','c']):
        print(i,v)
'''
#遍历两个或更多序列时，可以使用zip()组合
'''
list1 = ['name','age','class']
list2 = ['aaa','22','nicai']

for a, b in zip(list1,list2):
        print('这是你的{0}? 是{1}.'.format(a,b))
'''
#要反向遍历一个序列，首先指定这个序列，然后调用reversed()函数
'''
for i in reversed(range(3,5,10)):
        print(i)
'''
#要按顺序遍历一个序列，使用sorted()函数返回一个已排序的序列，并不修改原值：

'''
'''
fruit = {'banana','apple','pear','grape','orange'}

for f in sorted(set(fruit)):
        print(f)