# coding:utf-8
"""
目的：重写unitest的 setUp 和 tearDown
作者： 马令帅
修改日期：2016.12.08
"""

from driver import browser
import unittest

class MyTest(unittest.TestCase):

    def setUp(self):
        self.driver = browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        #self.driver.get("http://demo.esuizhen.com/")

    def tearDown(self):
        self.driver.quit()




