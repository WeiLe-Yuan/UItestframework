import time
from public.common import mytest
from public.common import datainfo
from public.pages import MenHu_user_managementPage
from public.common.publicfunction import get_img

class TestuserEdit(mytest.MyTest):
    '''管理信息门户测试'''

    def test_user_edit(self):
        '''用户信息编辑功能测试'''

        testuseredit = MenHu_user_managementPage.UserManagementPage(self.dr)
        testuseredit.login()
        time.sleep(5)
        testuseredit.into_user_management_page()
        time.sleep(2)

        self.dr.click('xpath->html/body/div[1]/div[2]/div/div/div[2]/table/tbody/tr[6]/td[7]/div/a[2]/img')
        time.sleep(2)
        self.dr.clear_type('id->loginId', 'xiaohong')
        self.dr.click('xpath->html/body/div[5]/div[3]/div/button[2]')

        result = self.dr.alert_is_present()
        time.sleep(2)
        if result==False:
            get_img(self.dr, "出现重复账号名.jpg")
        self.assertTrue(result, "不应该出现重复的账户名")

