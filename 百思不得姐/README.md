# Python3.6

## 学习爬虫--爬取百思不得姐图片，并下载到本地

```python

import requests,re,urllib.request

def  getPic(page):
    response = requests.get("http://www.budejie.com/pic/%s" % page)
    html = response.text
    reg = r'data-original="(.*?)"'
    for i in re.findall(reg, html):
        filename = i.split("/")[-1]
        print("正在下载:%s" % filename)
        urllib.request.urlretrieve(i, "pic/%s" % filename)

for i in range(1,10):
    getPic(i)

```