#coding=utf-8

from public.common import basepage
import time

class UserManagementPage(basepage.Page):

    def login(self):
        """登录系统"""
        self.dr.open("http://192.168.1.203:8080/ips/login.real.jsp")
        time.sleep(5)
        self.dr.clear_type('id->username', 'admin')
        self.dr.clear_type('id->password', '111111')
        self.dr.click('id->btnLogin')

    def into_user_management_page(self):
        """进入用户管理界面"""
        self.dr.click('xpath->html/body/div[10]/div[1]/a')
        self.dr.click('xpath->//div[@id="navMenu"]/ul/li[7]/a/img')
        self.dr.switch_to_frame('id->fNav')
        self.dr.click('id->spage.data.tree39')
        self.dr.switch_to_frame_out()
        self.dr.switch_to_frame('id->fMain')
        self.dr.switch_to_frame('name->fRight')

    def click_add_button(self):
        """点击添加用户按钮"""
        self.dr.click('name->btnCreateUser')

    def input_loginId(self, values):
        """输入账号"""
        self.dr.clear_type('id->loginId', values)

    def input_userName(self, values):
        """输入名称"""
        self.dr.clear_type('id->userName', values)

    def input_password_and_confirm(self, values1, values2):
        """输入密码和重复密码"""
        self.dr.clear_type('id->password', values1)
        self.dr.clear_type('id->confirm', values2)

    def input_email(self, values):
        """输入注册邮箱"""
        self.dr.clear_type('id->email', values)

    def input_phone(self, values):
        """输入手机号"""
        self.dr.clear_type('id->phone', values)

    def click_Confirm_add_button(self):
        """点击确认添加按钮"""
        self.dr.click('xpath->(//button[@type="button"])[9]')

    def pri(self, info):
        """该函数通过查询账号中有无刚添加的账号进行断言"""
        divs = self.dr.get_elements('tag_name->div')
        test = False
        for i in divs:
            if i.get_attribute("data-name") == "loginId":
                if i.text == info:
                    test = True
        return test

    def click_delect_button(self):
        """点击批量删除按钮"""
        self.dr.click('name->btnRemoveUser')

    def select_assert(self, info):
        """该函数通过查询账号中有无刚删除的账号进行断言"""
        divs = self.dr.get_elements('tag_name->div')
        test = True
        for i in divs:
            if i.get_attribute("data-name") == "loginId":
                if i.text in info:
                    test = False
        return test
