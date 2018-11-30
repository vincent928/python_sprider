# -*- coding: utf-8 -*-
# @Author = moon
# @Create = 2018/4/24 16:01
# @File = requestsdemo.py

# GET请求

import requests
import json
# from requests.packages import urllib3
from requests.exceptions import ReadTimeout, ConnectTimeout

# response = requests.get('http://httpbin.org/get')
# print(response.text)

## 带参数的GET请求

# response2 = requests.get("http://httpbin.org/get?name=germey&age=22")
# print(response2.text)

## 方法2

# data = {
#     'name':'germey',
#     'age':22
# }

# response3 = requests.get('http://httpbin.org/get', params=data)
# print(response3.text)

## 解析json数据

# response4 = requests.get('http://httpbin.org/get')
# print(type(response4.text))
# print(response4.json())
# print(json.loads(response4.text))
# print(type(response4.json()))

# 下载二进制文件并保存

# response5 = requests.get('https://www.baidu.com/img/bd_logo1.png')
# print(type(response5.text),type(response5.content))
# with open('logo.png','wb') as f:
#     f.write(response5.content)
#     f.close()


## 添加headers，有些网站会检验请求头

# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 \
#     (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'
# }
#
# response6 = requests.get('https://www.zhihu.com/explore',headers=headers)
# print(response6.text)



## response的属性

# response7 = requests.get("http://www.jianshu.com")
# print(type(response7.status_code),response7.status_code)
# print(type(response7.headers),response7.headers)
# print(type(response7.url),response7.url)
# print(type(response7.cookies),response7.cookies)
# print(type(response7.history),response7.history)


## 高级操作
## 文件上传

# files = {
#     'file':open('logo.png','rb')
# }
# response8 = requests.post('http://httpbin.org/post',files=files)
# print(response8.text)


# 获取cookie

# response9 = requests.get('http://www.baidu.com')
# print(response9.cookies)
# for key,value in response9.cookies.items():
#     print(key+"="+value)


## 会话维持，模拟登陆

# requests.get('http://httpbin.org/cookies/set/number/123456789')
# response10 = requests.get('http://httpbin.org/cookies')                 #这边相当于两个独立浏览器分别访问
# print(response10.text)

# s = requests.Session()      #创建Session，通过Session对象分别访问，保持会话
# s.get('http://httpbin.org/cookies/set/number/123456789')
# response10 = s.get('http://httpbin.org/cookies')
# print(response10.text)


## 证书验证

# response11 = requests.get('https://www.12306.cn')    # 访问一个https网站，会先检验证书是否合法
# print(response11.text)

# urllib3.disable_warnings()          # 导入from requests.packages import urllib3 并调用 disable_warnings()忽略警告
# response12 = requests.get('https://www.12306.cn', verify=False)  # 是否检验证书，默认True
# print(response12.status_code)


## 代理设置

# proxies = {
#     "http":"http://127.0.0.1:9743",
#     "https":"https://127.0.0.1:9743"
# }
# response13 = requests.get('https://www.taobao.com',proxies=proxies)
# print(response13.status_code)



## 超时设置

# try:
#     response14 = requests.get("http://httpbin.org/get", timeout=0.1)
#     print(response14.status_code)
# except ReadTimeout:
#     print('Time OUT')
# except ConnectTimeout:
#     print('ConnectTimeout')


## 认证设置 有些网站需要用户登录

r = requests.get('http://www.zhihu.com',auth=('17706440370','77494682'))
print(r.status_code)












