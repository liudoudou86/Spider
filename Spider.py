#coding=utf-8

import requests
from bs4 import BeautifulSoup
from DingDingBot.DDBOT import DingDing


def gethtml():
    """
        url和headers是为了仿照浏览器进行访问
    """
    url = "https://top.baidu.com/board?tab=realtime"
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34"}
    try:
        txt = ''
        res = requests.get(url, headers) # 爬取网页
        soup = BeautifulSoup(res.text, 'lxml') # 使用bs4对网页进行分析
        result = soup.select('.c-single-text-ellipsis') # 对关键词进行class的定位
        for i in range(0,10):
            results = result[i].text.strip().replace('\n', '')
            txt += '【' + str(i+1) + '】'
            txt += results
            txt += '\n'
        '''
        with open('D:/Coding/数据.txt', mode= 'w', encoding= 'utf-8') as file:
            file.write(txt)
            '''
        # print(txt)
        return(txt)
    except:
        print("炸了！")

def send_msg(msg):
    """
        使用第三方包对钉钉发送数据
    """
    try:
        url = "https://oapi.dingtalk.com/robot/send?access_token=7050f5a5e20958eed4aaa270ea19376e700e0cac0aa8768b8be1566a12980a51"
        dd = DingDing(webhook = url)
        info = dd.Send_Text_Msg(Content= msg, atMobiles= ['13820303577'])
        print(info)
    except:
        print("没发出去~")

if __name__ == "__main__":
    msg = gethtml()
    send_msg(msg)