# coding:utf-8
"""
目的：登录后，主页面左侧目录 和 顶端页面元素 定位
作者：马令帅
修改日期：2016.12.14
"""
from selenium.webdriver.common.by import By
from projectName.test_case.page_obj.login_page import login
from time import sleep

class catelog(login):
    """用户登录成后，系统左侧目录 和 顶端页面元素"""
    #url = "/public/html/window_content.html"
    # 定位器：随访患者管理、随访工作管理、随访结果管理、随访统计分析、系统管理
    esz_catelog_sfhzgl = (By.CSS_SELECTOR, '[resourcename="SFHZGL"]')
    esz_catelog_sfhzgl_state = (By.XPATH, '//*[@id="mainMenu"]/li[1]')
    esz_catelog_sfgzgl = (By.CSS_SELECTOR, '[resourcename="SFGZGL"]')
    esz_catelog_sfgzgl_state = (By.XPATH, '//*[@id="mainMenu"]/li[2]')
    esz_catelog_sfjggl = (By.CSS_SELECTOR, '[resourcename="SFJGCK"]')
    esz_catelog_sfjggl_state = (By.XPATH, '//*[@id="mainMenu"]/li[3]')
    esz_catelog_sftjfx = (By.CSS_SELECTOR, '[resourcename="SFTJFX"]')
    esz_catelog_sftjfx_state = (By.XPATH, '//*[@id="mainMenu"]/li[4]')
    esz_catelog_xtgl = (By.CSS_SELECTOR, '[resourcename="XTGL"]')
    esz_catelog_xtgl_state = (By.XPATH, '//*[@id="mainMenu"]/li[5]')

    # 定位子菜单：全部患者列表、失访患者列表、疑似重复患者管理、数据质量分析
    esz_catelog_sfhzgl_QBHZLB = (By.CSS_SELECTOR, '[resourcename="QBHZLB"]')
    esz_catelog_sfhzgl_SFHZLB = (By.CSS_SELECTOR, '[resourcename="SFRYLB"]')
    esz_catelog_sfhzgl_YSCFHZGL = (By.CSS_SELECTOR, '[resourcename="NSCFHZGL"]')
    esz_catelog_sfhzgl_SJZLFX = (By.CSS_SELECTOR, '[resourcename="SJZLFX"]')

    # 随访工作管理：随访任务管理、全院随访情况统计、随访工作量统计、短信回复处理、电话接通率统计、患者来电记录
    esz_catelog_sfgzgl_SFRWGL = (By.CSS_SELECTOR, '[resourcename="SFRWGL"]')
    esz_catelog_sfgzgl_QYSFQKTJ = (By.CSS_SELECTOR, '[resourcename="SFGZJZ"]')
    esz_catelog_sfgzgl_SFGZLTJ = (By.CSS_SELECTOR, '[resourcename="SFGZLTJ"]')
    esz_catelog_sfgzgl_DXHFCL = (By.CSS_SELECTOR, '[resourcename="DXHFCL"]')
    esz_catelog_sfgzgl_DHJTLTJ = (By.CSS_SELECTOR, '[resourcename="DHJTLTJ"]')
    esz_catelog_sfgzgl_HZLDJL = (By.CSS_SELECTOR, '[resourcename="DHLDJL"]')

    # 随访结果管理：微信随访结果、短信随访结果、电话随访结果、调查问卷统计
    esz_catelog_sfjggl_WXSFJG = (By.CSS_SELECTOR, '[resourcename="WXSFJT"]')
    esz_catelog_sfjggl_DXSFJG = (By.CSS_SELECTOR, '[resourcename="DXSFJG"]')
    esz_catelog_sfjggl_DHSFJG = (By.CSS_SELECTOR, '[resourcename="DHSFJG"]')
    esz_catelog_sfjggl_DCWJTJ = (By.CSS_SELECTOR, '[resourcename="DCWJTJ"]')

    # 随访统计分析：一键统计、生存率高级统计
    esz_catelog_sftjfx_YJTJ = (By.CSS_SELECTOR, '[resourcename="YJTJ"]')
    esz_catelog_sftjfx_SCLGJTJ = (By.CSS_SELECTOR, '[resourcename="SCLGJTJ"]')

    # 进入全部患者列表
    def click_allpatientlist(self):
        # 获取 一级菜单状态，判断是否已经展开
        state = self.driver.find_element(*self.esz_catelog_sfhzgl_state).get_attribute("class")
        if state != "active":
            self.driver.find_element(*self.esz_catelog_sfhzgl).click()
        self.driver.find_element(*self.esz_catelog_sfhzgl_QBHZLB).click()

    # 进入失访患者列表
    def click_sfhzlb(self):
        # 获取 一级菜单状态，判断是否已经展开
        state = self.driver.find_element(*self.esz_catelog_sfhzgl_state).get_attribute("class")
        if state != "active":
            self.driver.find_element(*self.esz_catelog_sfhzgl).click()
        self.driver.find_element(*self.esz_catelog_sfhzgl_SFHZLB).click()

    # 进入疑似重复患者列表
    def click_yscfhzlb(self):
        # 获取 一级菜单状态，判断是否已经展开
        state = self.driver.find_element(*self.esz_catelog_sfhzgl_state).get_attribute("class")
        if state != "active":
            self.driver.find_element(*self.esz_catelog_sfhzgl).click()
        self.driver.find_element(*self.esz_catelog_sfhzgl_YSCFHZGL).click()

    # 进入数据质量分析
    def click_sjzlfx(self):
        # 获取 一级菜单状态，判断是否已经展开
        state = self.driver.find_element(*self.esz_catelog_sfhzgl_state).get_attribute("class")
        if state != "active":
            self.driver.find_element(*self.esz_catelog_sfhzgl).click()
        self.driver.find_element(*self.esz_catelog_sfhzgl_SJZLFX).click()

    # 进入随访任务管理
    def click_sfrwgl(self):
        # 获取 父级菜单状态，判断是否已经展开
        state = self.driver.find_element(*self.esz_catelog_sfgzgl_state).get_attribute("class")
        if state != "active":
            self.driver.find_element(*self.esz_catelog_sfgzgl).click()
        self.driver.find_element(*self.esz_catelog_sfgzgl_SFRWGL).click()

    # 进入 全院随访情况统计
    def click_qysfqktj(self):
        # 获取 父级菜单状态，判断是否已经展开
        state = self.driver.find_element(*self.esz_catelog_sfgzgl_state).get_attribute("class")
        if state != "active":
            self.driver.find_element(*self.esz_catelog_sfgzgl).click()
        self.driver.find_element(*self.esz_catelog_sfgzgl_QYSFQKTJ).click()

    # 进入 随访工作量统计
    def click_sfgzltj(self):
        # 获取 父级菜单状态，判断是否已经展开
        state = self.driver.find_element(*self.esz_catelog_sfgzgl_state).get_attribute("class")
        if state != "active":
            self.driver.find_element(*self.esz_catelog_sfgzgl).click()
        self.driver.find_element(*self.esz_catelog_sfgzgl_SFGZLTJ).click()

    # 进入 短信回复处理
    def click_dxhfcl(self):
        # 获取 父级菜单状态，判断是否已经展开
        state = self.driver.find_element(*self.esz_catelog_sfgzgl_state).get_attribute("class")
        if state != "active":
            self.driver.find_element(*self.esz_catelog_sfgzgl).click()
        self.driver.find_element(*self.esz_catelog_sfgzgl_DXHFCL).click()

    # 进入 电话接通率统计
    def click_dhjtltj(self):
        # 获取 父级菜单状态，判断是否已经展开
        state = self.driver.find_element(*self.esz_catelog_sfgzgl_state).get_attribute("class")
        if state != "active":
            self.driver.find_element(*self.esz_catelog_sfgzgl).click()
        self.driver.find_element(*self.esz_catelog_sfgzgl_DHJTLTJ).click()

    # 进入 患者来电记录
    def click_hzldjl(self):
        # 获取 父级菜单状态，判断是否已经展开
        state = self.driver.find_element(*self.esz_catelog_sfgzgl_state).get_attribute("class")
        if state != "active":
            self.driver.find_element(*self.esz_catelog_sfgzgl).click()
        self.driver.find_element(*self.esz_catelog_sfgzgl_HZLDJL).click()

    # 进入 微信随访结果
    def click_wxsfjg(self):
        # 获取 父级菜单状态，判断是否已经展开
        state = self.driver.find_element(*self.esz_catelog_sfjggl_state).get_attribute("class")
        if state != "active":
            self.driver.find_element(*self.esz_catelog_sfjggl).click()
        self.driver.find_element(*self.esz_catelog_sfjggl_WXSFJG).click()

    # 进入 短信随访结果
    def click_dxsfjg(self):
        # 获取 父级菜单状态，判断是否已经展开
        state = self.driver.find_element(*self.esz_catelog_sfjggl_state).get_attribute("class")
        if state != "active":
            self.driver.find_element(*self.esz_catelog_sfjggl).click()
        self.driver.find_element(*self.esz_catelog_sfjggl_DXSFJG).click()

    # 进入 电话随访结果
    def click_dhsfjg(self):
        # 获取 父级菜单状态，判断是否已经展开
        state = self.driver.find_element(*self.esz_catelog_sfjggl_state).get_attribute("class")
        if state != "active":
            self.driver.find_element(*self.esz_catelog_sfjggl).click()
        self.driver.find_element(*self.esz_catelog_sfjggl_DXSFJG).click()

    # 进入 调查问卷统计
    def click_dcwjtj(self):
        # 获取 父级菜单状态，判断是否已经展开
        state = self.driver.find_element(*self.esz_catelog_sfjggl_state).get_attribute("class")
        if state != "active":
            self.driver.find_element(*self.esz_catelog_sfjggl).click()
        self.driver.find_element(*self.esz_catelog_sfjggl_DCWJTJ).click()

    # 进入 一键统计
    def click_yjtj(self):
        # 获取 父级菜单状态，判断是否已经展开
        state = self.driver.find_element(*self.esz_catelog_sftjfx_state).get_attribute("class")
        if state != "active":
            self.driver.find_element(*self.esz_catelog_sftjfx).click()
        self.driver.find_element(*self.esz_catelog_sftjfx_YJTJ).click()

    # 进入 生存率高级统计
    def click_sclgjtj(self):
        # 获取 父级菜单状态，判断是否已经展开
        state = self.driver.find_element(*self.esz_catelog_sftjfx_state).get_attribute("class")
        if state != "active":
            self.driver.find_element(*self.esz_catelog_sftjfx).click()
        self.driver.find_element(*self.esz_catelog_sftjfx_SCLGJTJ).click()

    # 系统管理：系统功能简介、管理员信息、医院信息、本机号设置、组织架构管理、角色及权限、用户管理、模板管理、疾病管理、科室管理、系统全局配置、日增数据统计
    esz_catelog_xtgl_XTGNJJ = (By.CSS_SELECTOR, '[resourcename="XTGNJS"]')
    esz_catelog_xtgl_GLYXX = (By.CSS_SELECTOR, '[resourcename="GLYXX"]')
    esz_catelog_xtgl_YYXX = (By.CSS_SELECTOR, '[resourcename="YYXX"]')
    esz_catelog_xtgl_BJHSZ = (By.CSS_SELECTOR, '[resourcename="BJHPZ"]')
    esz_catelog_xtgl_ZZJGGL = (By.CSS_SELECTOR, '[resourcename="ZZJGGL"]')
    esz_catelog_xtgl_JSJQX = (By.CSS_SELECTOR, '[resourcename="JSJQX"]')
    esz_catelog_xtgl_YHGL = (By.CSS_SELECTOR, '[resourcename="YHGL"]')
    esz_catelog_xtgl_MBGL = (By.CSS_SELECTOR, '[resourcename="MBGL"]')
    esz_catelog_xtgl_JBGL = (By.CSS_SELECTOR, '[resourcename="JBGL"]')
    esz_catelog_xtgl_KSGL = (By.CSS_SELECTOR, '[resourcename="KSGL"]')
    esz_catelog_xtgl_XTQJPZ = (By.CSS_SELECTOR, '[resourcename="XTQJPZ"]')
    esz_catelog_xtgl_RZSJTJ = (By.CSS_SELECTOR, '[resourcename="RZSJTJ"]')

    # 进入 系统功能简介
    def click_xtgnjj(self):
        # 获取 父级菜单状态，判断是否已经展开
        state = self.driver.find_element(*self.esz_catelog_xtgl_state).get_attribute("class")
        if state != "active":
            self.driver.find_element(*self.esz_catelog_xtgl).click()
        self.driver.find_element(*self.esz_catelog_xtgl_XTGNJJ).click()

    # 进入 管理员信息
    def click_glyxx(self):
        # 获取 父级菜单状态，判断是否已经展开
        state = self.driver.find_element(*self.esz_catelog_xtgl_state).get_attribute("class")
        if state != "active":
            self.driver.find_element(*self.esz_catelog_xtgl).click()
        self.driver.find_element(*self.esz_catelog_xtgl_GLYXX).click()

    # 进入 医院信息
    def click_yyxx(self):
        # 获取 父级菜单状态，判断是否已经展开
        state = self.driver.find_element(*self.esz_catelog_xtgl_state).get_attribute("class")
        if state != "active":
            self.driver.find_element(*self.esz_catelog_xtgl).click()
        self.driver.find_element(*self.esz_catelog_xtgl_YYXX).click()

    # 进入 本机号设置
    def click_bjhsz(self):
        # 获取 父级菜单状态，判断是否已经展开
        state = self.driver.find_element(*self.esz_catelog_xtgl_state).get_attribute("class")
        if state != "active":
            self.driver.find_element(*self.esz_catelog_xtgl).click()
        self.driver.find_element(*self.esz_catelog_xtgl_BJHSZ).click()

    # 进入 组织架构管理
    def click_zzjggl(self):
        # 获取 父级菜单状态，判断是否已经展开
        state = self.driver.find_element(*self.esz_catelog_xtgl_state).get_attribute("class")
        if state != "active":
            self.driver.find_element(*self.esz_catelog_xtgl).click()
        self.driver.find_element(*self.esz_catelog_xtgl_ZZJGGL).click()

    # 进入 角色及权限
    def click_jsjqx(self):
        # 获取 父级菜单状态，判断是否已经展开
        state = self.driver.find_element(*self.esz_catelog_xtgl_state).get_attribute("class")
        if state != "active":
            self.driver.find_element(*self.esz_catelog_xtgl).click()
        self.driver.find_element(*self.esz_catelog_xtgl_JSJQX).click()

    # 进入 用户管理
    def click_yhgl(self):
        # 获取 父级菜单状态，判断是否已经展开
        state = self.driver.find_element(*self.esz_catelog_xtgl_state).get_attribute("class")
        if state != "active":
            self.driver.find_element(*self.esz_catelog_xtgl).click()
        self.driver.find_element(*self.esz_catelog_xtgl_YHGL).click()

    # 进入 模板管理
    def click_mbgl(self):
        # 获取 父级菜单状态，判断是否已经展开
        state = self.driver.find_element(*self.esz_catelog_xtgl_state).get_attribute("class")
        if state != "active":
            self.driver.find_element(*self.esz_catelog_xtgl).click()
        self.driver.find_element(*self.esz_catelog_xtgl_MBGL).click()

    # 进入 疾病管理
    def click_jbgl(self):
        # 获取 父级菜单状态，判断是否已经展开
        state = self.driver.find_element(*self.esz_catelog_xtgl_state).get_attribute("class")
        if state != "active":
            self.driver.find_element(*self.esz_catelog_xtgl).click()
        self.driver.find_element(*self.esz_catelog_xtgl_JBGL).click()

    # 进入 科室管理
    def click_ksgl(self):
        # 获取 父级菜单状态，判断是否已经展开
        state = self.driver.find_element(*self.esz_catelog_xtgl_state).get_attribute("class")
        if state != "active":
            self.driver.find_element(*self.esz_catelog_xtgl).click()
        self.driver.find_element(*self.esz_catelog_xtgl_KSGL).click()

    # 进入 系统全局配置
    def click_xtqjpz(self):
        # 获取 父级菜单状态，判断是否已经展开
        state = self.driver.find_element(*self.esz_catelog_xtgl_state).get_attribute("class")
        if state != "active":
            self.driver.find_element(*self.esz_catelog_xtgl).click()
        self.driver.find_element(*self.esz_catelog_xtgl_XTQJPZ).click()

    # 进入 日增数据统计
    def click_rzsjtj(self):
        # 获取 父级菜单状态，判断是否已经展开
        state = self.driver.find_element(*self.esz_catelog_xtgl_state).get_attribute("class")
        if state != "active":
            self.driver.find_element(*self.esz_catelog_xtgl).click()
        self.driver.find_element(*self.esz_catelog_xtgl_RZSJTJ).click()


if __name__ == "__main__":
    from selenium import webdriver
    driver = webdriver.Chrome()
    log = catelog(driver)
    log.user_login()
    sleep(3)
    log.click_sfrwgl()
    log.click_qysfqktj()
    log.click_dxhfcl()
    log.click_sclgjtj()
    log.click_dhsfjg()
    log.click_yjtj()
    log.click_xtgnjj()