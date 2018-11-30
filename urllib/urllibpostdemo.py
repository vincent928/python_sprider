# -*- coding: utf-8 -*-
# @Author = moon
# @Create = 2018/4/24 15:09
# @File = urllibpostdemo.py


import urllib.parse
import urllib.request

data = bytes(urllib.parse.urlencode({'word':'hello'}),encoding='UTF-8')
response = urllib.request.urlopen('http://httpbin.org/post',data=data)
print(response.read().decode('UTF-8'))




















