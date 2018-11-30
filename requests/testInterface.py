# -*- coding: utf-8 -*-
# @Author = moon
# @Create = 2018/5/13 18:30
# @File = testInterface.py

import requests
from pyquery import PyQuery as pq

url = 'https://www.cnblogs.com/lifei66/p/7976408.html'
r = requests.get(url).text
doc = pq(r)
print(doc("#cnblogs_post_body"))




















