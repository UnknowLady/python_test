#!/user/bin/python3
#coding=utf-8

#条件控制相关学习笔记

#概念：
    #1、每个条件后面都要使用冒号（:）,表示接下来是满足条件后要执行的语句块
    #2、使用缩进划分语句块，相同缩进数的语句在一起组成一个语句块
    #3、在python中没有Switch-case语句

'''
------------------以下为if语句形式---------------

if condition_1:             #判断语句1
    statement_block_1       #判断为True，则执行这条语句1
elif condition_2:           #如果语句1为False，则判断这条语句，
    statement_block_2       #判断为True，则执行这条语句2
else condition_3:           #如果语句2为False，则判断这条语句，
    statement_block_3       #判断为True，则执行这条语句3

-------------------以上为if语句形式---------------
'''

#实例：采用条件语句判断狗的年龄
'''
age = int(input("Age of the dog: "))
print()
if age < 0:
    print("This can hardly be true!")
elif age == 1:
    print("about 14 human years")
elif age ==2:
    print("about 22 human years")
elif age > 2:
    human = 22 + (age - 2)* 5
    print("human years: ", human)
'''

#实例2：采用条件语句演示数字猜谜游戏

numeber = 7
guess = -1

print("Gusess the number!")

while guess != numeber:
    guess = int(input("Is it..."))

    if guess == numeber:
        print("Hooray! you guess it right!")
    elif guess < numeber:
        print("It's bigger...")
    elif guess > numeber:
        print("It's not so big.")