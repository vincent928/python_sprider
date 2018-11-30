# Python3.6

## 学习爬虫--爬取今日头条图片，保存到mongodb并下载到本地

分析ajax返回的json信息
爬虫抓取感觉最主要的还是分析获得页面数据的策略方法
后面的方式大同小异

```python

import json
import re
from urllib.parse import urlencode
from hashlib import md5
import os
import pymongo
import requests
from requests import RequestException
from multiprocessing import Pool   # 引入线程池，开启多线程下载
from 今日头条街拍.mongodb import *




client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]

def data_page_index(offset, keyword):
    data = {
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': '20',
        'cur_tab': '3',
        'from': 'gallery',
    }
    headers = {
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'
    }
    url = 'https://www.toutiao.com/search_content/?' + urlencode(data)
    response = requests.get(url,headers=headers)
    try:
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求索引页面出错')
        return None

def parse_page_index(html):
    data = json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')

def get_page_detail(url):
    headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'
    }
    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求详情页面出错',url)
        return None

def parse_page_detail(html,url):
    title_pattern = re.compile('BASE_DATA.galleryInfo = {.*?title:.*?\'(.*?)\',',re.S)
    title = re.search(title_pattern,html)
    if title:
       result_title = title.group(1)
    images_pattern = re.compile('gallery: JSON.parse\("(.*?)"\),',re.S)
    result = re.search(images_pattern,html)
    if result:
        data = json.loads(result.group(1).replace("\\\"","\"").replace("\\\\","\\"))
        if data and 'sub_images' in data.keys():
            sub_images = data.get('sub_images')
            images = [item.get('url') for item in sub_images]
            for image in images: download_image(image)
            return {
                'title': result_title,
                'url': url,
                'images': images
            }

def save_to_mongo(result):
    if db[MONGO_TABLE].insert(result):
        print("存储到MongoDB成功",result)
        return True
    return False

def download_image(url):
    print("当前正在下载：",url)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            save_image(response.content) # .content 返回二进制结果 .text 返回文本内容
        return None
    except RequestException:
        print('请求图片出错', url)
        return None

def save_image(content):
    file_path = '{0}/{1}.{2}'.format(os.getcwd()+'/pic', md5(content).hexdigest(),'jpg')
    if not os.path.exists(file_path):
        with open(file_path,'wb') as f:
            f.write(content)

def main(offset):
    html = data_page_index(offset,KEY_WORD)
    for url in parse_page_index(html):
        html = get_page_detail(url)
        if html:
           result = parse_page_detail(html,url)
           if result: save_to_mongo(result)

if __name__ == '__main__':
    groups = [x*20 for x in range(GROUP_START,GROUP_END + 1)]
    pool = Pool()
    pool.map(main,groups)



```