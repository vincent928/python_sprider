# -*- coding: utf-8 -*-
# @Author = moon
# @Create = 2018/4/24 14:39
# @File = reponsedemo.py

import requests

#下载百度图片

reponse = requests.get('https://www.baidu.com/img/bd_logo1.png')
print(reponse.content)


with open('g:/var/tem/1.png','wb') as f:
    f.write(reponse.content)
    f.close()
















