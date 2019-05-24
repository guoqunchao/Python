# -*- coding: UTF-8 -*-

__author__ = 'Ink.White'

from urllib.parse import urlencode
import requests
from pyquery import PyQuery
import time

base_url = 'http://m.weibo.cn/api/container/getIndex?'
headers = {
    'Host': 'm.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/2830678474',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

def get_page(page):
    '''https://m.weibo.cn/api/container/getIndex?type=uid&value=2830678474&containerid=1076032830678474&page=2'''
    params = {
        'type': 'uid',
        'value': '2830678474',
        'containerid': '1076032830678474',
        'page': page
    }
    url = base_url + urlencode(params)
    print(url)
    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print('Error',e)

def parse_page(json):
    if json:
        # print(json)
        items = json.get('data').get('cards')
        for item in items:
            item = item.get('mblog')
            # print(item)
            weibo = {}
            weibo['id'] = item.get('id')
            weibo['text'] = PyQuery(item.get('text')).text()
            weibo['attitudes'] = item.get('attitudes_count')
            weibo['comments'] = item.get('comments_count')
            weibo['reposts'] = item.get('reposts_count')
            yield weibo


if __name__ == '__main__':
    for page in range(2,12):
        json = get_page(page)
        results = parse_page(json)
        for result in results:
            print(result)