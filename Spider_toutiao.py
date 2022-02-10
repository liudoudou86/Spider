# Description：双码打卡
# Author：刘豆豆
# Time：2022/02/07
#coding=utf-8

import requests
from bs4 import BeautifulSoup
from DingDingBot.DDBOT import DingDing


def gethtml():
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
        for i in range(0,10):
            results = result[i].text.strip().replace('\n', '')
            links = result[i].get('href')
            txt += '>'
            txt += '[' + str(i+1) + '] '
            txt += '['
            txt += results # 将链接隐藏进标题内容中
            txt += ']'
            txt += '(https://toutiao.io/'
            txt += links
            txt += ')'
            txt += '\n\n'
        '''
        with open('D:/Coding/数据.txt', mode= 'w', encoding= 'utf-8') as file:
            file.write(txt)
        '''
        # print(txt)
        return txt
    except:
        print("炸了!")

def send_msg(msg):
    """
    使用第三方包对钉钉发送数据
    """
    try:
        url = "https://oapi.dingtalk.com/robot/send?access_token=7050f5a5e20958eed4aaa270ea19376e700e0cac0aa8768b8be1566a12980a51"
        dd = DingDing(webhook = url)
        info = dd.Send_MardDown_Msg(Title= '开发者头条', Content= '### **开发者头条:**\n' + msg, isAtAll= True)
        print(info)
    except:
        print("没发出去~")

if __name__ == "__main__":
    msg = gethtml()
    send_msg(msg)