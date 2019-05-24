#-*- coding:utf-8 -*-

__author__ = 'Ink.White'

import requests
import re
import json
from requests.exceptions import RequestException
import time


def get_one_page(url):
    try:
        headers = {'UserAgent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
    except RequestException:
        return None

def parse_one_page(html):
    items = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?class="name".*?title="(.*?)".*?class="star">(.*?)</p>.*?class="releasetime">(.*?)</p>.*?class="integer">(.*?)</i>.*?class="fraction">(.*?)</i></p>',re.S).findall(html)
    # print(items)   # list
    for item in items:
        # print(item) # tuple
        yield {
            'index':item[0],
            'image':item[1],
            'title':item[2].strip(),
            'actor':item[3].strip(),
            'time':item[4].strip(),
            'score':item[5].strip()+item[6].strip()
        }

def write_to_file(content):
    with open('result.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False) +'\n')   # json.dumps 将字段转化为字符串  写入文件中 字典格式无法直接write
        # print(type(json.dumps(content,ensure_ascii=False)))

def main(offset):
    url = 'https://maoyan.com/board/4?offset='+str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)

if __name__ == '__main__':
    for i in range(10):
        main(offset=i*10)
        time.sleep(1)