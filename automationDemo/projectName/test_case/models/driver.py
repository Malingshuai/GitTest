# coding:utf-8
__author__ = 'lsmad'
from selenium import webdriver
import time
from selenium.webdriver import Remote

#启动浏览器驱动
def browser():

    driver = webdriver.Chrome()
    #driver = webdriver.Firefox()
    #host="127.0.0.1:4444"                #运行主机：端口号 （本机默认：127.0.0.1:4444）
    #dc = {'browserName':'chrome'}       #指定浏览器（'chrome','firefox'）
    #driver = Remote(command_executor='http://' + host + '/wd/hub',desired_capabileties=dc)

    return driver


if __name__ == '__main__':
    dr = browser()
    time.sleep(5)
    dr.get("http://www.baidu.com")
    dr.quit()
