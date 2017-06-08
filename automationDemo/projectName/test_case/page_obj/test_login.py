# coding:utf-8

"""
目的：登录页面元素定位
作者：马令帅
修改日期：2016.12.12
"""

from ddt import ddt, data,unpack
from login_page import login
from projectName.test_case.models import myunit


@ddt
class test_login(myunit.MyTest):
    """登录case"""

    @data(["zlsfadmin", "123456", "ok"],
          ["zlsfadmin", "1234563", "no"])
    @unpack
    def test_01(self, username, password, result):
        log = login(self.driver)
        log.open()
        log.login_username(username)
        log.login_password(password)
        log.login_button()
        # 判断预期，获取对应的断言点，检验用例是否通过
        if result == "ok":
           self.assertEqual(log.login_success(), u"退出", msg=u"测试未通过！")
        elif result == "no":
            self.assertTrue(log.login_error(), msg=u"测试未通过！")


if __name__ == "__main__":
    myunit.MyTest.main