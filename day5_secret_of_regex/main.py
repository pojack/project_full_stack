#正则
#python中 第三方库  re
import re

#re模块当中  match 方法

#match 从字符串的开始位置进行匹配，匹配成功返回match对象，匹配失败返回None

# res=re.match('i','mingming')   #None
# print(res)

# res=re.match('m','mingming')   #None
# print(res.group())
#group方法  group方法提取匹配到的数据

#匹配单个字符
#  .   匹配任意一个字符（除了\n)

# res=re.match('.','1\n24')
# # print(res)
# print(res.group())

#[  ]  匹配[]中列举的字符

#
# res=re.match('[Aa]','Aabc123')
# print(res.group())

#[0123456789] [0-9]

res=re.match('[0-46-9]','4f5678hfdsty')
print(res.group())
#[0-9]    [0123456789]
#我们现在除5以外的数字
# [012346789]   [0-46-9]


#[012346789]  [0-9]    \d          \D  用来匹配非数字
#[a-z]   [A-Z]     [a-zA-Z]         \w  用来匹配字母，下划线、汉字，数字

#\s  匹配空格   \S 匹配非空格




