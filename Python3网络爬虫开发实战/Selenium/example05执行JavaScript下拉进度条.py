# -*- coding: UTF-8 -*-

__author__ = 'Ink.White'

# pip install tesserocr pillow
from selenium import webdriver

browser = webdriver.Chrome()
# browser.get('https://www.zhihu.com/explore')
browser.get('https://www.taobao.com')
browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
browser.execute_script('alert("To Bottom")')