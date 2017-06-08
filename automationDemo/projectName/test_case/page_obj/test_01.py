# coding:utf-8

"""
目的：登录页面元素定位
作者：马令帅
修改日期：2016.12.12
"""

from login_page import login
from selenium import webdriver
from time import sleep
driver =webdriver.Chrome()
log = login(driver)
log.open()
sleep(5)
log.login_username("zlsfadmin")
log.login_password("123456")
log.login_button()






