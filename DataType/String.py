#!/user/bin/python3
#coding=utf-8

#字符串运算的相关笔记

#概念：除了数字，python也能操作字符串，字符串有几种表达方式，可以使用单引号和双引号括起来
'''
    >>> 'spam eggs'
    'spam eggs'
    >>> 'doesn\'t'
    "doesn't"
    >>> "doesn't"
    "doesn't"
    >>> '"yes",he said.'
    '"yes",he said.'
    >>> "\"yes,\" he said."
    '"yes," he said.'
    >>> '"Isn\'t," she said.'
    '"Isn\'t," she said.'
'''
#python中使用反斜杠转义引号和其他特殊字符来准确的表示。
#如果字符串包含有单引号，但不包含双引号，则字符串会用双引号括起来，否则用单引号括起来。对于这样的输入字符串，print()函数会产生更易读的输出

#以下为跨行字符串的几种表示方式

# NO1：使用 \n 来添加新行
'''
    >>> s = 'First line. \nSecond line.'
    >>> s #不使用print(),\n 包含在输出中。
    'First line. \nSecond line.'
    >>> print(s) #使用print(),\n会输出新行
    First line.
    Second line.
'''
# NO2：使用反斜线（\）来续行
'''
    hello = "This is a rather long string containing\n\
    several lines of text just as you would do in C.\n\
        Note that whitespace at the beginning of the line is\
    significant."

    print(hello)
'''
# N03:可以被三个双引号或者三个单引号括起来。使用三引号时，换行符不需要转义，他们会包含在字符串中。
    #实例：使用转义符，避免最开始产生不必要的空行
'''
    print("""\
    Usage: thingy[OPTIONS]
    -h                  Display this usage message
    -H hostname         Hostname to connect to
    """)
'''
# NO4:如果我们使用"原始"字符串，那么 \n 不会被转换成换行，行末的的反斜杠，以及源码中的换行符，都将作为数据包含在字符串内。
'''
    hello = r"This is a rather long string containing\n\
        serveral lines of text much as you would do in C"
    print(hello)
''' 



# 1、字符串可以使用 + 运算符链接在一起，或者用 * 运算符重复
"""
    >>> word = 'help' + 'A'
    >>> word
    'helpA'
    
    >>> '<' + word*5 +'>'
    '<helpAhelpAhelpAhelpAhelpA>'
"""
# 2、字符串可以被索引，字符串的第一个字符的索引为0。参考如下例子
"""
    >>> word ='help' + 'A'
    >>> word
    'helpA'
    >>> word[4]
    'A'
    >>> word[0:2]
    'he'
    >>> word[2:4]
    'lp'
    >>> word[:2]    #显示前两个字符
    'he'
    >>> word[2:]    #除了前两个字符外的，其他字符
    'lpA'
    >>>
"""
# 3、用组合内容的方法来创建新的字符串简单且高效，如以下例子
"""
    >>> 'x'
    'x'
    >>> 'x' + word[1:]
    'xelpA'
    >>> 'Splat' + word[4]
    'SplatA'
    >>> word[:2] + word[2:]        #分切规律——> s[:i] + s[i:] = s
    'helpA'
"""
# 4、过大的索引将被字符串的大小取代，上限值小于小于下限值时将返回一个空的字符串
"""
    >>> word[1:20]
    'elpA'
    >>> word[5:]
    ''
    >>> word[2:1]
    ''
"""
# 5、在索引中可以使用负数，这将会从右往左计数，例如：
"""
    >>> word[-1]    #最后一个字符
    'A'
    >>> word[-2]    #倒数第二个字符
    'p'
    >>> word[-2:]   #最后两个字符
    'pA'
    >>> word[:-2]   #除最后两个字符之外，其前面的所有字符
    'hel'
    >>> word[-0]    #-0和0完全一样，-0不会从右开始计算
    'h'
"""
# 6、以下为索引工作方式的参考
'''
    +---+---+---+---+---+
    | H | e | l | p | A |
    +---+---+---+---+---+
      0   1   2   3   4    
     -5  -4  -3  -2  -1
'''
# 7、内置函数len() 一般用于返回一个字符串的长度
'''  
    >>> s = 'xxxhhedededleddededesisjdc'
    >>> len(s)
    26
'''
