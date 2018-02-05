import time
from public.common import mytest
from public.pages import MenHu_loginPage

class TestuserLogin(mytest.MyTest):
    '''管理信息门户测试'''

    def user_login(self, username = "", password = ""):
        '''登陆测试基本操作'''
        loginpage = MenHu_loginPage.MenhuLoginPage(self.dr)
        loginpage.into_login_page()
        loginpage.input_username(username)
        loginpage.input_password(password)
        loginpage.click_login_button()

    def test_user_login1(self):
        '''用户名，密码为空测试'''
        loginpage = MenHu_loginPage.MenhuLoginPage(self.dr)
        self.user_login()
        self.assertEqual("用户名称不能为空！", loginpage.get_caution())

    def test_user_login2(self):
        '''用户名正确，密码为空测试'''
        loginpage = MenHu_loginPage.MenhuLoginPage(self.dr)
        self.user_login("admin", "")
        self.assertEqual("密码不能为空！", loginpage.get_caution())

    def test_user_login3(self):
        '''用户名为空，密码正确测试'''
        loginpage = MenHu_loginPage.MenhuLoginPage(self.dr)
        self.user_login("", "111111")
        self.assertEqual("用户名称不能为空！", loginpage.get_caution())

    def test_user_login4(self):
        '''用户名,密码不匹配测试'''
        loginpage = MenHu_loginPage.MenhuLoginPage(self.dr)
        self.user_login("admin", "22222")
        time.sleep(1)
        self.assertEqual("用户不存在或密码错误，登陆失败！", loginpage.get_caution())

    def test_user_login5(self):
        '''用户名,密码正确测试'''
        loginpage = MenHu_loginPage.MenhuLoginPage(self.dr)
        self.user_login("admin", "111111")
        time.sleep(2)
        self.assertIn("管理员", loginpage.get_welcome_name())


