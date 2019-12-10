#grammmar主要描写的是python3的基本语法

#编码code
#默认情况下，python3源码文件以UTF-8编码，所有字符串都是Unicode字符串
# -*- coding:cp-1252 -*-   指定源码文件指定为1252的编码

#标识符
#第一个字符必须是字母表中字母或下划线_
#标识符的其他部分有字母、数字和下划线组成
#标识符对大小写敏感

#python保留字
#保留字即关键字，不能把它们用作任何标识符名称
import keyword
keyword.kwlist
#['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

#注释
#python中单行注释以#开头，多行注释用三个单引号（'''）或者三个双引号（""""）将注释括起来

'''
#数据类型
整数   如：1
长整数 比较大的整数
浮点数 如：1.23、3E2
复数   如：1 + 2k
'''

"""
#字符串
python中单引号和双引号使用完全相同
使用三引号可以指定一个多行字符串
转义符'\'
自然字符传，通过在字符串之前加r或R  如：r"this is a line with \n" 则会\n显示，不会换行
python允许unicode字符串，加前缀u或者U
字符串是不可变的
按照字面意义级联字符串，"this" "is" "string"会自动转换为 this is string
"""