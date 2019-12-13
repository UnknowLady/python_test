#!/user/bin/python3
#coding=utf-8

#字典运算的相关笔记

#概念
    #·字典是另一种可变的容器，且可以存储任意类型的对象
    #.字典的每个键值(key=>vaule)对用冒号(:)分割，每个对号之间用逗号(,)分割，整个字典包括在花括号({})中，格式如下:
'''
    d = {key1 ：value1, key2 : vlaue2}

    #键必须是唯一的，值不必
    # 值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组      
'''
# 1、dictionary字典创建
'''
    dict1 ={'aa':123, 'bb':'abc'}   #随意创建，反正都对
    dict2 ={'1.1':11, '1.2':'abc'}  #随意创建，反正都对
'''
# 2、访问字典里的值
'''
    dict ={'name':'jing', 'Age':22,'Sex':'女'} #创建字典
    print(dict['name'])     #访问name
    print(dict['hhh'])      #访问字典里没有的键，会输出错误哦
'''
# 3、dictionary字典修改（修改，添加）
'''
    dict ={'name':'jing', 'Age':22,'Sex':'女'}  #创建字典
    dict['Age'] = 3         #更新键Age的值
    dict['sex'] = '未知'    #sex和Sex两个是不同的键，在这里的作用是增加新的键/值

    print(dict['Age'])  #输出修改后的Age的值
    print(dict)         #输出字典dict
'''
# 4、dictionary字典删除
'''
    dict = {'name':'jing', 'Age':18}

    del dict['name']    #删除键'name'
    dict.clear()    #删除字典
    del dict        #删除字典
    print(dict['Age'])  #这里会报错，执行del后字典就不会存在
'''

# 5、dictionary字典键的特性
    #（1）、不允许同一个键出现两次，如同一个键被赋值两次，则后一个会被记住
'''
    dict = {'name':'jing','name':'jingzi'}  #创建字典
    print("dict[name]为：", dict['name'])   #只会记住后一个
'''
    #（2）、键必须不可变，所以可以用数字，字符串或元组充当，不可用列表
'''
    dict ={['name']:'jing','age':3}
    print(dict['name']) #报错，TypeError: unhashable type: 'list'
'''
# 6、dictionary字典的内置函数
    #.内置函数（1）、计算字典元素个数——> len(dict)
'''
    >>> dict ={'name':'jing', 'Age':3}
    >>> len(dict)
    2
'''
    #.内置函数（2）、输出字典以可打印的字符串表示——> str(dict)
'''
    >>> dict ={'name':'jing', 'Age':3}
    >>> str(dict)
    "{'name': 'jing', 'Age': 3}"
'''
     #.内置函数（3）、返回输出的变量类型，如变量是字典就返回字典——> type(dict)
'''
    >>> dict ={'name':'jing', 'Age':3}
    >>> type(dict)
    <class 'dict'>
'''
# 6、dictionary字典的内置方法
    #NO1——> radiansdict.clear() 删除字典内的所有元素
'''
#描述：字典clear()函数用于删除字典内的所有元素
#语法：dict.clear()
#实例
    dict = {'name':'jing', 'Age':3}
    print("字典的长度：%d" % len(dict))     #字典的长度2
    dict.clear()
    print("字典删除后的长度：%d" % len(dict))   #字典删除后长度0
'''
    #NO2——> radiansdict.copy() 返回一个字典的浅复制
'''
#描述：字典copy()函数用于返回一个浅复制
#语法：dict.copy()
#实例
    dict1 = {'name':'jing', 'Age':3}
    dict2 =dict1.copy()
    print("新复制的字典为：", dict2)
'''
    #NO3——> radiansdict.fromkeys() 创建一个新的字典
'''
#描述：fromkeys()用于创建一个新的字典，以序列seq()中元素做字典的键，value为字典所有键对应的初始值
#语法：dict.fromkeys(seq[, value])
#参数：seq ——字典键值列表
       value——可选参数，设置键序列（seq）的值

    seq = ('name','sex','age')
    dict = dict.fromkeys(seq)
    print("新的字典为： %s" % str(dict))

    dict = dict.fromkeys(seq, 10)
    print("新的字典为： %s" % str(dict))
'''
#NO4——> radiansdict.get(key,defalut=None)   返回指定键的值，如果值不在字典中返回defalut值
'''
#描述：get()函数用于返回指定键的值，如果值不在字典中就返回默认值
#语法：dict.get(key,defalut=None)
#参数： key——字典中要查找的键
        default——如果指定键的值不存在时，返回该默认值的值

    dict = {'Name': 'jing', 'Age': 24}

    print ("Age 值为 : %s" %  dict.get('Age'))
    print ("Sex 值为 : %s" %  dict.get('Sex', "Nv"))
'''  
 #NO5——> key in dict 如果键在字典dict中，返回true；否则，返回false
'''
 #描述：字典in操作符用于判断是否存在字典中，如果键在字典dict里返回true，否则返回false
 #语法：has_key()方法语法   key in dict
 #参数： key——字典中要找的值

dict ={'Name':'jing', 'Age':24,'Sex':"女"}
if 'Age' in dict:           #检测Age是否存在
    print("键Age在字典中哦")
else:
    print("键Age不在字典中哦")

if 'buzai' in dict:         #检测buzai是否存在
    print("键buzai在字典中哦")
else:
    print("键buzai不在字典中哦")
 
'''
#NO6——> radiansdict.items() 以列表返回可遍历的（键，值）元组数组                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
'''
 #描述：字典items()方法以列表返回可遍历的元组数组。
 #语法：items()方法语法   dict.items()
 #参数: NA

 #实例：返回可遍历的（键，值）元组数组

dict ={'Name':'jing','Age':24}
print ("value: %s" % dict.items())

'''
#NO7——> radiansdict.keys()  以列表返回一个字典所有的键
'''
 #描述：字典keys()方法以列表返回所有的键。
 #语法：dict.keys()方法语法   dict.keys()
 #参数: NA

 #实例：返回列表里的键

dict = {'Name':'jing',"Age":24}
print("返回列表里的键：%s" % dict.keys())
'''
#NO8——> radiansdict.setdefalut(key,default=None)  和get()类似,但键不存在字典中，将会添加键并将值设为default
'''
 #描述：字典setdefalut()方法与get()方法类似，如果键不存在字典中，将会添加值并将值设置为None
 #语法：dict.setdefault(key, default=None)
 #参数: key——查找的键值
        defaule——键不存在时，设置的默认键值

 #实例：键值存在时，输出存在键值,键值不存在时，输出默认键值

dict = {'Name':'jing', 'Age':25}
print ("Age键的值为：%s" % dict.setdefault('Age', None))    #键值存在时，输出存在键值
print ("Sex键的值为：%s" % dict.setdefault('Set', None))    #键值不存在时，输出默认键值

print("新的字典为：", dict)
'''
#NO9——> radiansdict.update(dict2)   把字典dict2的键/值更新到dict里
'''
 #描述：字典update()函数吧字典dict2的键/值更新到dict里
 #语法：dict.update(dict2)
 #参数: dict2——添加到指定字典dict里的字典

#实例：将字典dict2更新到dict里

dict = {'Name':'jing', 'Age':25}
dict2 = {'Sex':'女'}

dict.update(dict2)  #将字典dict2更新到dict里
print("最新的dict字典为：", dict )
'''
#NO10——> radiansdict.values()   以列表返回字典中的所有值
''' 
 #描述：values()方法以列表返回字典中的所有值
 #语法：dict.values()
 
 #实例:以列表返回字典中的所有值

dict = {'Name': 'jing', 'Age': 25, 'Sex': '女'}

print("字典中的所有值为：", list(dict.values()))
'''
