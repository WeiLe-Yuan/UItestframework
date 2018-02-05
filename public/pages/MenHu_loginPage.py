#coding=utf-8

from public.common import basepage

class MenhuLoginPage(basepage.Page):

    def into_login_page(self):
        '''打开门户登录页面'''
        self.dr.open("http://192.168.1.203:8080/ips/login.real.jsp")

    def input_username(self, values):
        '''输入用户名'''
        self.dr.clear_type('id->username', values)

    def input_password(self, values):
        '''输入密码'''
        self.dr.clear_type('id->password', values)

    def click_login_button(self):
        '''点击登录按钮'''
        self.dr.click('id->btnLogin')

    def get_caution(self):
        '''获取登录框的警示语'''
        return self.dr.get_text('id->msg')

    def get_welcome_name(self):
        '''获取登录后的欢迎显示'''
        return self.dr.get_text('xpath->html/body/div[2]/div/div[2]/div[2]/span')
