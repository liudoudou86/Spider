# -*- encoding=utf8 -*-
# Description：百度热榜\开发者头条\掘金
# Author：刘豆豆
# Time：2022/04/24

import requests
from bs4 import BeautifulSoup
import jsonpath
from DingDingBot.DDBOT import DingDing


def get_baidu():
    """
    url和headers是为了仿照浏览器进行访问
    """
    url = "https://top.baidu.com/board?tab=realtime"
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34"}
    try:
        txt = ''
        res = requests.get(url, headers) # 爬取网页
        soup = BeautifulSoup(res.text, 'lxml') # 使用bs4对网页进行分析
        result = soup.select('.title_dIF3B') # 对关键词进行class的定位
        for i in range(0,12):
            results = result[i].text.strip().replace('\n', '')
            links = result[i].get('href')
            txt += '>[' + str(i+1) + '] ' # 序列号
            txt += '[' + results + ']' # 将链接隐藏进标题内容
            txt += '(' + links +')'
            txt += '\n\n'
        '''
        with open('D:/Coding/数据.txt', mode= 'w', encoding= 'utf-8') as file:
            file.write(txt)
        '''
        # print(txt)
        return txt
    except Exception as e:
        print(e)

def get_toutiao():
    """
    url和headers是为了仿照浏览器进行访问
    """
    url = "https://toutiao.io/"
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43"}
    try:
        res = requests.get(url=url, headers=headers) # 爬取网页
        soup = BeautifulSoup(res.text, 'lxml') # 使用bs4对网页进行分析
        result = soup.select('a[target="_blank"]') # 对关键词进行class的定位
        txt = ''
        for i in range(0,12):
            results = result[i].text.strip().replace('\n', '')
            links = result[i].get('href')
            txt += '>[' + str(i+1) + '] ' # 序列号
            txt += '[' + results + ']' # 将链接隐藏进标题内容
            txt += '(https://toutiao.io/' + links +')'
            txt += '\n\n'
        '''
        with open('D:/Coding/数据.txt', mode= 'w', encoding= 'utf-8') as file:
            file.write(txt)
        '''
        # print(txt)
        return txt
    except Exception as e:
        print(e)

def get_juejin():
    """
    url和headers是为了仿照浏览器进行访问
    """
    session = requests.session()
    url = "https://api.juejin.cn/recommend_api/v1/article/recommend_all_feed?aid=2608&uuid="
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43"}
    json = {
    "id_type":2,
    "client_type":2608,
    "sort_type":3,
    "cursor":"0",
    "limit":12
    }
    try:
        res = session.request(url = url,method='post',json = json,headers = headers)
        data = res.json()
        result = jsonpath.jsonpath(data, '$..article_info.title') # 通过jsonpath获取标题
        link = jsonpath.jsonpath(data, '$..item_info.article_id')
        txt = ''
        for i in range(0,12):
            results = result[i]
            links = link[i]
            txt += '>[' + str(i+1) + '] ' # 序列号
            txt += '[' + results + ']' # 将链接隐藏进标题内容
            txt += '(https://juejin.cn/post/' + links +')'
            txt += '\n\n'
        # print(txt)
        return txt
    except Exception as e:
        print(e)

def send_msg(title, msg):
    """
    使用第三方包对钉钉发送数据
    """
    try:
        url = "https://oapi.dingtalk.com/robot/send?access_token=7050f5a5e20958eed4aaa270ea19376e700e0cac0aa8768b8be1566a12980a51"
        dd = DingDing(webhook = url)
        info = dd.Send_MardDown_Msg(Title= title, Content= '#### **' + title + ':**\n' + msg, isAtAll= True)
        print(info)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    
    filefly = [('百度热榜', get_baidu()), ('开发者头条', get_toutiao()), ('掘金', get_juejin())]
    for title, msg in filefly:
        send_msg(title ,msg)