# -*- encoding=utf8 -*-
# Description：贝壳二手房
# Author：刘豆豆
# Time：2022/04/24

import requests
from pyquery import PyQuery as pq


def getHouse(url):
    """
    url和headers是为了仿照浏览器进行访问
    """
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34"}
    try:
        txt = ''
        res = requests.get(url, headers) # 爬取网页
        doc = pq(res.text)
        ul = doc('.sellListContent')
        divs = ul.children('.clear .info.clear').items()
        count = 0
        region = ['元兴新里', '庆荣里', '津滨雅都公寓', '长安里', '三德里', '安德公寓', '德恩里', '盛瑞公寓', '黄埔里', '珠海里']
        for div in divs:
            count += 1
            link = div.children('.title a').attr('href')
            address = div.children('.address a').text()
            houseinfo = div.children('.address .houseInfo').text()
            price = div.children('.address .priceInfo .totalPrice.totalPrice2').text()
            if address in region:
                txt += '[' + address + '] ' + price + ' | ' + houseinfo + ' ---> ' + link
                txt += '\n'
        print(txt)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    
    for i in range (1, 5):
        getHouse(f'https://tj.ke.com/ershoufang/taoyuanjie/pg{i}lc1lc2a2l1l2p4p5/')