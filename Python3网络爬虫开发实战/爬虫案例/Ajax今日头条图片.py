# -*- coding: UTF-8 -*-

__author__ = 'Ink.White'

from urllib.parse import urlencode
import requests
import urllib.request
import os
from hashlib import md5

def get_page(offset):
    headers = {
        'Host':'www.toutiao.com',
        'Referer':'https://www.toutiao.com/search/?keyword=%E6%A8%A1%E7%89%B9',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'
    }
    params = {
        "aid":"24",
        "app_name":"web_search",
        "offset":offset,
        "format":"json",
        "keyword":"模特",
        "autoload":"true",
        "count":"20",
        "en_qc":"1",
        "cur_tab":"1",
        "from":"search_tab"
    }
    url =  "https://www.toutiao.com/api/search/content/?" + urlencode(params)
    print(url)
    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            print(response.json())
            return response.json()
    except requests.ConnectionError as e:
        return e

def get_image(json):
    if json.get('data'):
        for item in json('data'):
            title = item.get('title')
            images = item.get('image_detail')
            for image in images:
                yield {
                    'image':images.get('url'),
                    'title':title
                }

def save_image(item):
    if not os.path.exists(item.get('title')):
        os.mkdir(item.get('title'))
        try:
            response = requests.get(item.get(image))
            if response.status_code == 200:
                file_path = '{0}/{1}.{2}'.format(item.get('title'),md5(response.content).hexdigest(),'jpg')
                if not os.path.exists(file_path):
                    with open(file_path,'wb') as f:
                        f.write(response.content)
                else:
                    print('Already Downloaded',file_path)
        except requests.ConnectionError as e:
            print(e)

from multiprocessing.pool import Pool
def main(offset):
    json = get_page(offset)
    for item in get_image(json):
        print(item)
        save_image(item)

GROUP_START = 1
GROUP_STOP = 20

if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START,GROUP_STOP+1)])
    pool.map(main,groups)
    pool.close()
    pool.join()