# -*- coding: UTF-8 -*-

__author__ = 'Ink.White'

from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
print(browser.page_source)
browser.close()