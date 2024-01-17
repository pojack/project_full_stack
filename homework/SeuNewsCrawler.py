import requests
from lxml import etree
import csv


class SeuNewsInfo:
    newsTime = ''
    newsTitle = ''

    def __init__(self):
        return


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "no-cache", "Connection": "keep-alive",
    # "Cookie": "JSESSIONID=7DD332B09FE54A72CC89B6FF86868C61",
    "Host": "www.seu.edu.cn", "Pragma": "no-cache", "Referer": "https://www.seu.edu.cn/ddyw_47245/list1.htm",
    "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 "
                  "Safari/537.36 Edg/120.0.0.0",
    "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Microsoft Edge\";v=\"120\"",
    "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": "\"Windows\""}  # 工具生成headers
fileName = 'SEU_NEWS.csv'
loopTimes = 10  # 循环次数
currentPageNum = 1  # 循环次数
currentRowNum = 1  # 循环次数
baseUrl = f'https://www.seu.edu.cn/ddyw_47245/list{currentPageNum}.htm'  # seu新闻的url
itemCountXpath = '//ul[@class="news_list list2"]/*'  # 每页记录数xpath
# 标题xpath
getNewsTitleXpath = lambda index: f'//ul[@class="news_list list2"]/a[{index}]/span[@class="news_title"]/text()'
# 新闻发布时间xpath
getNewsTimeXpath = lambda index: f'//ul[@class="news_list list2"]/a[{index}]/span[@class="news_meta"]/text()'
newsInfoList = []  # 新闻列表

for i in range(loopTimes):
    response = requests.get(url=baseUrl, headers=headers)
    statusCode = response.status_code
    if statusCode == 200:
        res_data = response.content.decode()
        html = etree.HTML(res_data)
        itemCount = len(html.xpath(itemCountXpath))
        # 逐行匹配 失配信息默认空字符串 todo 用xpath运算语法优化
        for j in range(itemCount):
            curIdx = j + 1
            curNewsTime = html.xpath(getNewsTimeXpath(curIdx))
            curNewsTitle = html.xpath(getNewsTitleXpath(curIdx))
            newsInfo = SeuNewsInfo()
            if len(curNewsTime) > 0:
                newsInfo.newsTime = curNewsTime[0]
            if len(curNewsTitle) > 0:
                newsInfo.newsTitle = curNewsTitle[0]
            newsInfoList.append(newsInfo)

        currentPageNum += 1
    else:
        print(f"爬取失败,响应码非200:{statusCode}")

with open(file=fileName, mode='w', newline='', encoding='utf8') as file:
    writer = csv.writer(file)
    # 写入表头
    writer.writerow(['标题', '发布时间'])
    for k in range(len(newsInfoList)):
        curNewsInfo = newsInfoList[k]
        writer.writerow([curNewsInfo.newsTitle, curNewsInfo.newsTime])
