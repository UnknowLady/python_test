#!/user/bin/python3
#coding=utf-8

'''
按位运算符是把数字看作二进制来进行计算的，注释的文本为按位运算法规则

运算符&：按位“与”运算符，参与运算的两个值，如果相应位都为1，则该为的结果为1，否则为0
运算符|：按位“或”运算符，只要对应的两个二进制位有一个1时，结果位就为1.
运算符^:按位“异或”运算符，当两个对应的二进位相异时，结果就为1
运算符~:按位“取反”运算符，对数据的每个二进制位取反，即把0变为1，把1变为0。
运算符<<:左移动运算符：运算数的各二进位全部左移若干位，由“<<”右边的数指定移动的位数，高位丢弃，低位补0
运算符>>:右移动运算符：把“>>>”左边的运算数的各二进位全部右移若干位，“>>>”右边的数指点移动的位数。
'''
#这个案例为python位运算符的操作

a = 60      # 60 = 0011 1100
b = 13      # 13 = 0000 1101

c = a & b  # 解释= 0000 1100   结果（12）
print("1、c的值为：", c)

c = a | b  # 解释= 0011 1101   结果（61）
print("2、c的值为：", c)

c = a ^ b  # 解释= 0011 0001   结果（49）
print("3、c的值为：", c)

c = ~a     # 解释= 1100 0011    结果（-61）
print("4、c的值为：", c)

c = a << 2 # 解释= 1111 0000    结果（240）   
print("5、c的值为：", c)

c = a >> 2 #解释= 0000 1111     结果（15）
print("6、c的值为：", c)
