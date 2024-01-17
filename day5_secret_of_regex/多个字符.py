#匹配多个字符
import re
# *  匹配前一个字符出现0次或者无限次 [0,+无穷大]  有多少给我匹配多少
# import re
# res=re.match('\d*','12345678905678978909ghjg8765434567890987654321')
# print(res.group())

# +  匹配前一个字符出现1次或者无限次 [1,+无穷大]

# res1=re.match('\d+','a12345678905678978909ghjg8765434567890987654321')
# print(res1.group())

#?       匹配前一个字符出现0次或者1次  [0,1]

#
# res=re.match('\d?','a123abc')
# print(res.group())



#  {11} 匹配前一个字符出现多少次   只能匹配到11位   超过11位匹配不到
#
# res=re.match('\d{11,11}','173556721803')
# print(res.group())

# {m,n} 最少m 最多n


#匹配开头和结尾

#  ^匹配字符串的开头
#
# res=re.match('\d','173556721803')
# print(res.group())

#  ^  在[]中表示对...取反的意思
# res=re.match('[^Pp]','jpython')
# print(res.group())

#结尾  $  匹配字符串的结尾
# res=re.match('ming','ming')
# print(res.group())

#匹配分组 |   匹配左右任意一个表达式


res=re.match('\d|\s',' 123abc')
print(res.group())













