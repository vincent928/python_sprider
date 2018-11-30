# -*- coding: utf-8 -*-
# @Author = moon
# @Create = 2018/4/24 15:34
# @File = cookiedemo.py

#获取并打印cookie

import http.cookiejar,urllib.request

cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
print("{")
for item in cookie:
    print(item.name+"='"+item.value+"'")
print("}")

















