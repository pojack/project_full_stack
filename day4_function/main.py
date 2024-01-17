#函数

#函数  对相同功能的一段代码的封装

"""
def 函数名(参数1,参数2，参数3):    #形参  作用范围在函数体这块
    函数语句
    return 返回值
"""
#函数的定义     #实参向形参传递的过程 要一一对应   在我们定义函数的时候 如果没有return  返回出去  那么就返回None
# def add(a,b):
#     c=a+b
#
#
# #函数调用   函数名(实参)   参数能不能是一个函数名？？？    是可以滴
# #
# d=add(1,2)
# print(d)
# # print(add(1,2))


#
# def add(a,b):
#     c=a+b
#     return c
#

def add(a,b):
    c=a+b
    return c


#lambda表达式   lambda 参数1,参数2:返回值

# add=lambda a,b:a+b
#
# print(add(1,2))


# add(1,2)
#

# 函数的参数
#在我们python当中  我们在参数的前面加上一个*，*参数  参数 可以去接受任意个

# def func(*args):
#     print(args)
# #args前面加上一个*，表示这个参数为可变参数，那么在函数调用时候，参数的个数是不限制的
# #()
# func(      )
# func(1)
# func(1,2,3,4)
#func(1,2,3,4)
# def func(*args):
#     sum=0
#     for i in args:
#         sum=i+sum
#     return sum
#
# print(func(1,2,3,4))
#默认参数
# def func(a,b=1):      #b为默认参数
#     return a+b
#
#
# print(func(1))
# print(func(1,2))

#关键字参数   **       key=value
#
# def func(**kwargs):   #参数的个数可以接受任意个
#     print(kwargs)
# #{} 字典   { }
# func()
# func(name='xiaoxiao',age=18,sex='男')


#函数的变量作用域   全局变量  局部变量

#全局变量 和局部变量  同名 那么就使用局部变量  使用内部
#在函数体使用全局变量  没问题  但是你如果对全局变量的值（不可变）要进行修改 必须使用global关键字进行声明
# d=5
# def func():
#     #使用global关键字进行全局变量的声明
#     global d
#     d=d+5
#     print(d)
# func()


#
# list1=[1,2,3,4]
# def func():
#     list1[0]=2
#     print(list1[0])
# func()




#递归  100的和  100+99的和   100+99+98的和    递归一定要注意  有一个结束入口！！！

# def func(num):
#     if num==1:
#         return 1
#     else:
#         return num+func(num-1)
#
# print(func(100))
#计算5！
def func1(num):
    if num==1:
        return 1
    else:
        return num*func1(num-1)

print(func1(5))

#高阶函数

# map
# map(  )
#map(第一个参数为函数名，第二个参数为可迭代对象）

# def square(n):
#     return n**2
#
# list1=[1,2,3,4,5]
#
# new_list=list(map(square,list1))
# print(new_list)

#对列表中的偶数平方  奇数  乘以2


def square(n):
    if n%2==0:
        return n**2
    else:
        return n*2

list1=[1,2,3,4,5]

new_list=list(map(square,list1))
print(new_list)