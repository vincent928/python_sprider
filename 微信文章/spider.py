# -*- coding: utf-8 -*-
# @Author = moon
# @Create = 2018/5/4 13:16
# @File = spider.py
from urllib.parse import urlencode
from requests import ConnectionError
from pyquery import PyQuery as pq
import requests

base_url = 'http://weixin.sogou.com/weixin?'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36',
    'Cookie': 'SUV=00570B5D654457C25AE04B233D77C407; IPLOC=CN3301; SUID=779E0A702613910A000000005AEBEBC7; ABTEST=0|1525410761|v1; SNUID=8771E59FF0EA84AAB17755C0F01E8981; weixinIndexVisited=1; sct=1; JSESSIONID=aaaymB6RjsXPa6Jlw2Kmw; ppinf=5|1525411390|1526620990|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZToyNzolRTYlOTklOTMlRTYlOTUlOEYlRUUlODQlQkN8Y3J0OjEwOjE1MjU0MTEzOTB8cmVmbmljazoyNzolRTYlOTklOTMlRTYlOTUlOEYlRUUlODQlQkN8dXNlcmlkOjQ0Om85dDJsdUJpTFE3M3B2OVhwUmxLWkxDVVloY29Ad2VpeGluLnNvaHUuY29tfA; pprdig=Ma3iQKuXunt7AUYqKRuEu_DkXbUaVyVy12f1KlsLJzQbcT-vg2Brq_BPBdQuElF8gVTvnrB_q13zAOEcoK7xXH9unBZs3WPguYZlbty7VAr4wulirQjn67Bwpy93UhjpTMxKcjot6wXheKoBXi7CV8HOutQRkL_dH-OlVpgB1ss; sgid=12-34872463-AVrr7j4WQQ4s4T1HgfYcyOw; ppmdig=15254113910000007020f659660aa3267dbf0a51c86e6ea9',
    'Host': 'weixin.sogou.com',
    'Upgrade-Insecure-Requests': '1'
}
key_word = 'java'
# 代理
proxy_pool_url = 'http://127.0.0.1:5000/get'
proxy = None
max_count = 5

# 获取代理ip
def get_proxy():
    try:
        response = requests.get(proxy_pool_url)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        return None

# 配合代理获取搜索页面
def get_html(url, count=1):  # 获取html页面
    print('Crawing', url)
    print('Trying Count', count)
    global proxy
    if count >= max_count:
        print('Tried too many counts')
        return None
    try:
        if proxy:
            proxies = {
                'http': 'http://' + proxy
            }
            response = requests.get(url, allow_redirects=False, headers=headers, proxies=proxies)
        else:
            response = requests.get(url, allow_redirects=False, headers=headers)
        if response.status_code == 200:
            return response.text
        if response.status_code == 302:  # 状态码为302时，需要更换代理
            # need proxy
            print('302')
            proxy = get_proxy()
            if proxy:
                print('Using Proxy', proxy)
                return get_html(url)
            else:
                print('Get Proxy Failed')
                return None
    except ConnectionError as e:
        print('Error Occurred', e.args)
        proxy = get_proxy()
        count += 1
        return get_html(url, count)

# 获取搜索请求url地址
def get_index(keyword, page):
    data = {
        'query': keyword,
        'type': 2,  # type=2文章 （其他值为公众号）
        'page': page
    }
    queries = urlencode(data)
    url = base_url + queries  # 以上是拼接请求url
    html = get_html(url)  # 获取html页面资源
    return html

# 解析搜索页面
def parse_html(html):
    doc = pq(html)
    items = doc('.news-box .news-list li .txt-box h3 a').items()
    for item in items:
        yield item.attr('href')

# 获取微信文章页面
def get_detail(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        return None

# 解析文章详情页面
def parse_detail(html):
    doc = pq(html)
    title = doc('.rich_media_title').text()        # 文章标题
    content = doc('.rich_media_content').text()     # 文章内容
    date = doc('#post-date').text()                 # 发布日期
    nickname = doc('.rich_media_meta_list .rich_media_meta_nickname').text()    #作者
    wechat = doc('#js_profile_qrcode > div > p:nth-child(3) > span').text()        # 微信公众号
    return {
        'title':title,
        'content':content,
        'date':date,
        'nickname':nickname,
        'wechat':wechat
    }

def main():
    for page in range(1, 100):
        html = get_index(key_word, page)
        if html:
            article_urls = parse_html(html)
            for article_url in article_urls:
                article_html = get_detail(article_url)
                if article_html:
                    article_data = parse_detail(article_html)
                    print(article_data)


if __name__ == '__main__':
    main()
