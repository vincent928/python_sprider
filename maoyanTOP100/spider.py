# -*- coding: utf-8 -*-
# @Author = moon
# @Create = 2018/4/28 21:18
# @File = spider.py
import json
import re
import requests
from requests.exceptions import RequestException

def get_one_page(url):
    try:
        header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'}
        response = requests.get(url,headers=header)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         +'.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>'
                         +'.*?fraction">(.*?)</i>.*?</dd>',re.S)
    items = re.findall(pattern,html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'star': item[3].strip()[3:],
            'releasetime': item[4].strip()[5:],
            'integer': item[5]+item[6]
        }

def write_to_file(content):
    with open('result.text','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False) + '\n')


def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)

if __name__ == '__main__':
    for i in range(10):
        main(i*10)





















