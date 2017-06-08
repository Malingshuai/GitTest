# coding:utf-8
"""
目的：登录后，全部患者列表，页面元素定位
作者：马令帅
修改日期：2016.12.14
"""
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from projectName.test_case.page_obj.catelog_page import catelog
from selenium.common.exceptions import NoSuchElementException


class allpatientlist(catelog):
    '''全部患者列表'''

    # 切换到 iframe 表单内嵌页面中
    def __iniframe(self):
        '''进入到 iframe 框架下操作数据'''
        self.driver.switch_to.frame("onlyIframe")

    # 跳出 iframe 当前内嵌页面
    def __outiframe(self):
        '''跳出当前 iframe 表单'''
        self.driver.switch_to.parent_content("onlyIframe")

    # 定位 iframe 表单内嵌的页面元素
    # 数据统计：患者总数、周期内已完成任务的患者总数、任务进行中的患者总数、任务进行中患者总数、尚未分入任务的患者总数、可随访总数、随访死亡患者、随访失访人数、随访过后无需随访患者数
    # esz_iframe_hzzs = (By.ID, "num_11")
    # esz_iframe_zqnhzzs = (By.ID, "num_12")
    # esz_iframe_rwjxzhzzs = (By.ID, "num_13")
    # esz_iframe_swfrrwhzs = (By.ID, "num_14")
    # esz_iframe_ksfzs = (By.ID, "num_21")
    # esz_iframe_sfswhz = (By.ID, "num_22")
    # esz_iframe_sfsfrs = (By.ID, "num_23")
    # esz_iframe_wxsfhzs = (By.ID, "num_24")
    esz_iframe_hztj = [(By.ID, "num_11"), (By.ID, "num_12"), (By.ID, "num_13"), (By.ID, "num_14"),
                       (By.ID, "num_21"), (By.ID, "num_22"), (By.ID, "num_23"), (By.ID, "num_24")]

    # 返回 统计结果
    def patientnum(self):
        '''依次获取统计结果，并存入到patientnum数组中'''
        self.__iniframe()
        patientnum = []
        for temp in self.esz_iframe_hztj:
            num_temp = self.find_element(*temp).text
            num_temp = int(num_temp)
            patientnum.append(num_temp)
        return patientnum

    # 查询条件：病案号、患者姓名、手机号、更多条件;
    # 诊断名称、诊断疾病编码;
    # 病理诊断名称、病理诊断编码;
    # 病种、确诊时间;
    # 出院次数、出院时间；
    # 查询按钮
    esz_iframe_allpatientlist_cxtj = [(By.ID, "j-medical-record"), (By.ID, "j-name"), (By.ID, "j-telephone"), (By.ID, "j-select_more"),
                                      (By.CSS_SELECTOR, '[e-combine="sourceDiagnosis"]'), (By.CSS_SELECTOR, '[e-combine="sourceDiseaseCode"]'),
                                      (By.CSS_SELECTOR, '[e-combine="sourcePathologyDiagnosis"]'), (By.CSS_SELECTOR, '[e-combine="sourcePathologyDiseaseCode"]'),
                                      (By.XPATH, "/html/body/span/span/span[1]/input"), (By.XPATH, '//*[@id="select_more_dom"]/ul/li[5]/input[1]'), (By.XPATH, '//*[@id="select_more_dom"]/ul/li[5]/input[2]'),
                                      (By.ID, "select2-usae-container"), (By.XPATH, '//*[@id="select_more_dom"]/ul/li[6]/input[1]'), (By.XPATH, '//*[@id="select_more_dom"]/ul/li[6]/input[2]'),
                                      (By.CSS_SELECTOR, '[e-type="j-select-btn"]')]



    # 输入条件，查询
    def select_allpatientlist(self, patientNo, patientName, mobile, diagnosisName, diseaseCode, binglizhenduanName, binglizhenduanCode, bingzhong, quezhenStartTime, quezhenEndTime, outhospitalStart, outhospitalEnd):
        '''实现输入查询条件，点击查询操作'''

        try:
            self.find_element(*self.esz_iframe_allpatientlist_cxtj[0]).send_keys(patientNo)   # 输入病案号
            self.find_element(*self.esz_iframe_allpatientlist_cxtj[1]).send_keys(patientName) # 输入患者姓名
            self.find_element(*self.esz_iframe_allpatientlist_cxtj[2]).send_keys(mobile)      # 输入患者手机号

            # 获取跟多条件是否展开状态 （select_more_close展开状态、select_more_open收起状态）
            __state = self.find_element(*self.esz_iframe_allpatientlist_cxtj[3]).get_attribute('e-type')
            if __state == "select_more_open":
                self.find_element(*self.esz_iframe_allpatientlist_cxtj[3]).click()

            self.find_element(*self.esz_iframe_allpatientlist_cxtj[4]).send_keys(diagnosisName)             # 输入诊断名称
            self.find_element(*self.esz_iframe_allpatientlist_cxtj[5]).send_keys(diseaseCode)               # 输入诊断疾病编码
            self.find_element(*self.esz_iframe_allpatientlist_cxtj[6]).send_keys(binglizhenduanName)        # 输入病理名称
            self.find_element(*self.esz_iframe_allpatientlist_cxtj[7]).send_keys(binglizhenduanCode)        # 输入病理编码

            # 展开病种下拉筛选框
            esz_iframe_bingzhongid = (By.XPATH, '//*[@id="select_more_dom"]/ul/span[2]/span[1]/span')
            esz_iframe_bingzhongstate = self.find_element(*esz_iframe_bingzhongid).get_attribute('aria-expanded')   # aria-expanded="false"时，表示没有展开下拉菜单
            if esz_iframe_bingzhongstate == 'false':
                self.find_element(*esz_iframe_bingzhongid).click()
                self.find_element(*self.esz_iframe_allpatientlist_cxtj[8]).send_keys(bingzhong)
                self.find_element(*self.esz_iframe_allpatientlist_cxtj[8]).send_keys(Keys.ENTER)
            elif esz_iframe_bingzhongstate == 'true':
                self.find_element(*self.esz_iframe_allpatientlist_cxtj[8]).send_keys(bingzhong)               # 输入病种
                self.find_element(*self.esz_iframe_allpatientlist_cxtj[8]).send_keys(Keys.ENTER)

            # # 时间空件的操作方法
            # jsa = "$('#select_more_dom>ul>li:nth-child(5)>input:nth-child(1)').removeAttr('readonly')"               # jQuery，移除属性,将只读置改为可写；删除readonly属性
            # jsb = "$('#select_more_dom>ul>li:nth-child(5)>input:nth-child(1)').attr('oldtime', ‘2014-01-01’)"
            # self.driver.execute_script(jsa)                                          # 执行脚本
            # self.driver.execute_script(jsb)
            # aaaa = self.find_element(*self.esz_iframe_allpatientlist_cxtj[9])
            # aaaa.send_keys(quezhenStartTime)           # 输入确诊开始时间

            # jsb = "$('input[class=Wdate]').eq(1).removeAttr('readonly')"               # jQuery，移除属性,将只读置改为可写；删除readonly属性
            # self.driver.execute_script(jsb)                                          # 执行脚本
            # self.find_element(*self.esz_iframe_allpatientlist_cxtj[10]).send_keys(quezhenEndTime)              # 输入确诊结束时间
            #
            # # self.find_element(*self.esz_iframe_allpatientlist_cxtj[11]).send_keys(outhospitalEnd)              # 输入出院次数
            #
            # jsc = "$('input[class=Wdate]').eq(2).removeAttr('readonly')"
            # self.driver.execute_script(jsc)
            # self.find_element(*self.esz_iframe_allpatientlist_cxtj[12]).send_keys(outhospitalStart)              # 输入出院时间开始
            #
            # jsd = "$('input[class=Wdate]').eq(3).removeAttr('readonly')"
            # self.driver.execute_script(jsd)
            # self.find_element(*self.esz_iframe_allpatientlist_cxtj[13]).send_keys(outhospitalEnd)              # 输入出院时间结束

            self.find_element(*self.esz_iframe_allpatientlist_cxtj[14]).click()                            # 点击查询
        except NoSuchElementException:
            print(u"元素定位失败！")




if __name__ == "__main__":
    from selenium import webdriver
    driver = webdriver.Chrome()
    log = allpatientlist(driver)
    log.user_login()
    sleep(5)
    a = log.patientnum()[0]
    print(a)
    print(type(a))
    log.select_allpatientlist("10001", u"张三丰", "", "", "", "", "", u"鼻咽癌", "2000-10-01", "2016-12-16", "1990-01-01", "2016-12-16" )

