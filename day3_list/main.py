# ** 幂运算
# and  or   True  False
# 变量
# 解构
a, b = [1, 2]
#
# a,b=1
# 选择 循环
# for i in range(1,100,1):
#     print(i)


# 列表  list

# [         ]

list1 = [1, 2, 3, 4]
print(type(list1))
# 索引   从左往右   0开始    从右往左   -1开始
print(list1[0], list1[-4])

# 切片
# [开始位置:结束位置:步长]     结束位置取不到 步长为正数   从左往右   步长为负数  从右往左
#
# a='helloworld'
# print(a[0:5:1])


# 列表的遍历

#
# list1=[1,2,3,4,5,6]
# for i in list1:
#     print(i)


# 列表推导式

# list1=[1,2,3,4,5,6]
# #构造一个新的空列表
# list2=[]
# for i in list1:
#     if i%2==1:
#         list2.append(i*2)
#
# print(list2)
#
# #列表推导式
# #[ 表达式     for i in 可迭代对象  条件           ]
#
# list2=[i*2 for i in list1 if  i%2==1 ]
# print(i*2)


list1=[1,2,3]
list2=[4,5,6]
list1.extend(list2)
print(list1)



#字符串

# *
#
#
# a='11'  11111111
# print(a*4)   a+a+a+a

#字符串的长度   len
# in not in  在不在








