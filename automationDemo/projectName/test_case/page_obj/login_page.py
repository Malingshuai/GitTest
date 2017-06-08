# coding:utf-8
"""
目的：登录页面元素定位
作者：马令帅
修改日期：2016.12.12
"""
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from time import sleep
from projectName.test_case.page_obj.page import page


class login(page):
    """用户登录页面"""
    url = "/public/html/"

    # 定位器：用户名、密码、登录按钮、错误提示框、退出按钮
    esz_login_username = (By.CLASS_NAME, "userName")
    esz_login_password = (By.CLASS_NAME, "cryptPasswd")
    #esz_login_button_login = (By.CLASS_NAME, "btn btnlogin")             # Selenium2不支持类名中有空格
    esz_login_button_login = (By.XPATH, '//*[@id="contentBody"]/section/div[2]/input')
    esz_login_error_button = (By.CLASS_NAME, "sure")
    esz_login_success_button = (By.ID, "logoutBtn")

    #输入用户名
    def login_username(self,username):
        self.find_element(*self.esz_login_username).clear()
        self.find_element(*self.esz_login_username).send_keys(username)

    #输入密码
    def login_password(self, password):
        self.find_element(*self.esz_login_password).clear()
        self.find_element(*self.esz_login_password).send_keys(password)

    #点击登录
    def login_button(self):
        self.find_element(*self.esz_login_button_login).click()

    #错误提示
    def login_error(self):
        return self.find_element(*self.esz_login_error_button)

    #登录成功
    def login_success(self):
       return self.find_element(*self.esz_login_success_button).text

    #默认登录（统一登录入口，不用于执行测试用例）
    def user_login(self, username="zlsfadmin", password="123456"):
        try:
            self.open()                        #打开网址
            sleep(1)
            self.login_username(username)      #输入用户名
            self.login_password(password)      #输入密码
            self.login_button()                #点击登录
        except NoSuchElementException, tss:
            print(u"元素定位失败！")
            print(tss)
        except BaseException, tss:
            print(u"登录失败！")
            print(tss)


if __name__=="__main__":
    from selenium import webdriver
    driver = webdriver.Chrome()
    log = login(driver)
    log.user_login()