#!/user/bin/python3
#coding=utf-8

#Python 模块相关学习笔记  （模块：module）

#概念
'''
1、模块使人有逻辑的组织代码段
2、把相关的代码分配到一个模块里能让代码更好用，更易懂
3、模块也是python对象，具有随机的名字属性用来绑定或引用
4、模块能定义函数、类和变量。模块也能包含可执行的代码
#一个叫做aname模块里的python代码一般能在一个叫aname.py文件找到，下里是哥简单模块的support.py


'''
def print_func( par ):
    print("hello:", par)
    return

#import语句
'''
想要使用python源文件，只需在另一个源文件里执行import语句，语法如下：
import module1[,module2[,... moduleN]]
当前解释器遇到import语句，如果模块在当前的搜索路径就会被导入。
搜索路径是一个解释器会先进行搜索的所有目录的列表，如想要导入模块hello.py,需要吧命令放在脚本的顶端
'''

#导入模块
import Module

#现在调用模块里包含的函数
Module.print_func("xixi")
