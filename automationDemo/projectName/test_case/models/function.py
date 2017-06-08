# coding:utf-8
__author__ = 'lsmad'

from selenium import webdriver
import os

#截图函数
def insert_img(driver,file_name):
    #获取当前路径
    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir)
    #将获取的路径中的"\\"替换为："/"
    base_dir = base_dir.replace('\\','/')
    #分隔路径，获取父目录
    base = base_dir.split('test_case')[0]
    # 指定截图的相对位置
    file_path = base + "/report/image/" + file_name
    # 保存截图到指定位置
    driver.get_screenshot_as_file(file_path)

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    insert_img(driver,'baidu.jpg')
    driver.quit()