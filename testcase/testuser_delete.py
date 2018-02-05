import time
from public.common import mytest
from public.common import datainfo
from public.pages import MenHu_user_managementPage

class TestuserDelete(mytest.MyTest):
    '''管理信息门户测试'''



    def test_user_delete(self):
        testuseradd = MenHu_user_managementPage.UserManagementPage(self.dr)
        testuseradd.login()
        time.sleep(5)
        testuseradd.into_user_management_page()
        time.sleep(2)
        datas = datainfo.get_csv_to_lists("用户添加测试用例.csv")
        userId = []
        for info in datas:
            userId.append(info[0])
        row = self.dr.get_element('xpath->html/body/div[1]/div[2]/div/div/div[2]/table/tbody').find_elements_by_xpath('tr')
        rowNum = len(row)
        for i in range(rowNum):
            if self.dr.get_element('xpath->html/body/div[1]/div[2]/div/div/div[2]/table/tbody/tr[' + str(i+1) + ']/td[3]/div').text in userId:
                self.dr.click('xpath->html/body/div[1]/div[2]/div/div/div[2]/table/tbody/tr[' + str(i+1) + ']/td[1]/input')
        time.sleep(1)
        testuseradd.click_delect_button()
        self.dr.accept_alert()
        time.sleep(2)
        self.assertTrue(testuseradd.select_assert(userId), "批量删除失败")