# -*- coding: utf-8 -*-
# @Author = moon
# @Create = 2018/4/24 15:39
# @File = cookietextdemo.py

# 将cookie信息保存text文本

import http.cookiejar,urllib.request

filename = 'cookie.text'
cookie = http.cookiejar.MozillaCookieJar(filename)
# cookie = http.cookiejar.LWPCookieJar(filename) 什么方式存储就什么方式读取
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open("http://www.baidu.com")
cookie.save(ignore_expires=True,ignore_discard=True)




















