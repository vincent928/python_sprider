# -*- coding: utf-8 -*-
# @Author = moon
# @Create = 2018/4/24 14:56
# @File = chromedemo.py

#模拟浏览器打开页面，解决javascript渲染问题

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.taobao.com")
print(driver.page_source)



















