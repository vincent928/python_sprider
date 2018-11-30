# -*- coding: utf-8 -*-
# @Author = moon
# @Create = 2018/4/24 15:43
# @File = cookieloaddemo.py


#读取cookie文件信息

import http.cookiejar,urllib.request

cookie = http.cookiejar.MozillaCookieJar()
cookie.load('cookie.text',ignore_discard=True,ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open("http://www.baidu.com")
print(response.read().decode('UTF-8'))





















