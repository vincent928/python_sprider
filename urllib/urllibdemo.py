# -*- coding: utf-8 -*-
# @Author = moon
# @Create = 2018/4/24 15:18
# @File = urllibdemo.py

#捕获超时异常

import socket
import urllib.request
import urllib.error

try:
    response = urllib.request.urlopen("http://httpbin.org/get",timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print('TIME OUT')



















