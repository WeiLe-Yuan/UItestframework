import time
from public.common import mytest
from public.common import datainfo
from public.pages import MenHu_user_managementPage


class TestuserAdd(mytest.MyTest):
    '''管理信息门户测试'''


    def user_add(self, info):
        '''用户添加测试'''
        testuseradd = MenHu_user_managementPage.UserManagementPage(self.dr)
        testuseradd.click_add_button()
        testuseradd.input_loginId(info[0])
        testuseradd.input_userName(info[1])
        testuseradd.input_password_and_confirm(info[2], info[3])
        testuseradd.input_email(info[4])
        testuseradd.input_phone(info[5])
        testuseradd.click_Confirm_add_button()
        time.sleep(2)
        self.assertTrue(testuseradd.pri(info[0]), "用户添加失败")

    def test_user_add(self):
        '''添加新用户的测试'''

        testuseradd = MenHu_user_managementPage.UserManagementPage(self.dr)
        testuseradd.login()
        time.sleep(5)
        testuseradd.into_user_management_page()
        time.sleep(2)
        datas = datainfo.get_csv_to_lists("用户添加测试用例.csv")
        for data in datas:
            self.user_add(data)

