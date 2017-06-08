# coding:utf-8
"""
目的：所有页面的基础类，需要外部 传参：driver 和 URL
作者：马令帅
修改日期：2016.12.12
"""

class page():
    """基础类，用于所有页面的继承"""
    login_url = "http://demo.esuizhen.com"
    def __init__(self, driver, esz_url=login_url):
        '''构造函数，用于初始化参数'''
        self.driver = driver
        self.base_url = esz_url
        self.timeout = 30

    def on_page(self):
        """断言，当前打开的URL 与 预期打开的地址是否一致"""
        return self.driver.current_url == (self.base_url + self.url)

    def __open(self, url):
        """获取指定的URL页面"""
        url = self.base_url + url
        self.driver.get(url)
        assert self.on_page(), "Did not land on %s" % url

    def open(self):
        '''打开网站'''
        self.__open(self.url)

    def find_element(self, *loc):
        """统一提供页面元素定位的方法（单个元素定位）"""
        return  self.driver.find_element(*loc)

    def find_elements(self, *loc):
         """统一提供页面元素定位的方法(一组元素定位)"""
         return self.driver.find_elements(*loc)

    def script(self, src):
        """提供调用 JavaScript 代码"""
        return self.driver.execute_script(src)

