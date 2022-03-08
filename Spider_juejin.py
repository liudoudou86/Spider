# -*- encoding=utf8 -*-
# Description：掘金综合3天热榜爬虫
# Author：刘豆豆
# Time：2022/03/07

import requests
import jsonpath
from DingDingBot.DDBOT import DingDing


def gethtml():
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

def send_msg(msg):
    """
    使用第三方包对钉钉发送数据
    """
    try:
        url = "https://oapi.dingtalk.com/robot/send?access_token=7050f5a5e20958eed4aaa270ea19376e700e0cac0aa8768b8be1566a12980a51"
        dd = DingDing(webhook = url)
        info = dd.Send_MardDown_Msg(Title= '掘金', Content= '#### **掘金热榜:**\n' + msg, isAtAll= True)
        print(info)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    msg = gethtml()
    send_msg(msg)