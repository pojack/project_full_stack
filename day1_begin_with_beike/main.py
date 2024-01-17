# ' https://sh.ke.com/xiaoqu/beicai/'

# 需求 爬取贝壳二手房的相关信息

import requests
from lxml import etree
import csv

# url='https://sh.ke.com/xiaoqu/beicai/'
# 翻页  一般我们要去找规律
# 第一页  https://sh.ke.com/xiaoqu/beicai/

# https://sh.ke.com/xiaoqu/beicai/pg1/
# 第二页   https://sh.ke.com/xiaoqu/beicai/pg2/
# 第三页 https://sh.ke.com/xiaoqu/beicai/pg3/

# if i==1:
#     url='https://sh.ke.com/xiaoqu/beicai/'
# if i>2:
#     url=f'https://sh.ke.com/xiaoqu/beicai/pg{i}/'
priceArr = [];
neibourArr = [];
for i in range(1, 11):
    if i == 1:
        url = 'https://sh.ke.com/xiaoqu/beicai/'

        response = requests.get(url=url)
        res_data = response.content.decode()  # 字节流解码
        html = etree.HTML(res_data)  # etree结构化字符串数据
        priceArr = html.xpath('//*[@id="beike"]/div[1]/div[4]/div[1]/div[3]/ul/li/div[2]/div[1]/div[1]/span/text()')
        neibourArr = html.xpath('//*[@id="beike"]/div[1]/div[4]/div[1]/div[3]/ul/li/div[1]/div[1]/a/text()')
        print(neibourArr)

    if i >= 2:
        url = 'https://sh.ke.com/xiaoqu/beicai/'

        response = requests.get(url=url)
        res_data = response.content.decode()
        html = etree.HTML(res_data)
        danjia1 = html.xpath('//*[@id="beike"]/div[1]/div[4]/div[1]/div[3]/ul/li/div[2]/div[1]/div[1]/span/text()')
        xiaoqu1 = html.xpath('//*[@id="beike"]/div[1]/div[4]/div[1]/div[3]/ul/li/div[1]/div[1]/a/text()')
        neibourArr.extend(xiaoqu1)
        priceArr.extend(danjia1)

# todo 1.with 关键字? 2.csv.writer() 3.open()
with open(file='贝壳二手房.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['小区', '单价'])  # 写入表头
    for i in range(len(neibourArr)):
        writer.writerow([neibourArr[i], priceArr[i]])  # 写入每一行数据

# 现在有个需求 就是吧我能不能吧小区  和单价  放在csv文件当中
# 爬取数据  现在是不是要存储数据   csv中


# #xpath
#
#
# #小区名字
# //*[@id="beike"]/div[1]/div[4]/div[1]/div[3]/ul/li/div[1]/div[1]/a/text()
# #单价
# //*[@id="beike"]/div[1]/div[4]/div[1]/div[3]/ul/li/div[2]/div[1]/div[1]/span/text()

# html=etree.HTML(res_data)
# #单价
# danjia=html.xpath('//*[@id="beike"]/div[1]/div[4]/div[1]/div[3]/ul/li/div[2]/div[1]/div[1]/span/text()')
# print(danjia)
# print(len(danjia))
# 小区
# xiaoqu=html.xpath('//*[@id="beike"]/div[1]/div[4]/div[1]/div[3]/ul/li/div[1]/div[1]/a/text()')
# print(xiaoqu)
# print(len(xiaoqu))
