# coding:utf-8

import os
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from public.common.log import Log
from config import globalparam

# 邮件正文以及测试报告的路径
mailbodyPath = globalparam.mail_path
reportPath = globalparam.report_path
logger = Log()
# 配置收件人和抄送人
recvaddress = ['wlyuan1996@163.com']
ccaddress = ['yuanweile@businessmatrix.com.cn']
# 发件人的用户名和密码
sendaddr_name = '982578641@qq.com'
sendaddr_pswd = 'iljanuxrdqngbdce'


class SendMail:
    def __init__(self, recver=None):
        """接收邮件的人：list or tuple"""
        if recver is None:
            self.sendTo = recvaddress
        else:
            self.sendTo = recver

    def __get_report(self):
        """获取最新测试报告"""
        dirs = os.listdir(reportPath)
        dirs.sort()
        newreportname = dirs[-1]
        print('The new report name: {0}'.format(newreportname))
        return newreportname

    def __take_messages(self):
        """生成邮件的内容，和html报告附件"""
        newreport = self.__get_report()
        self.msg = MIMEMultipart()
        self.msg['Subject'] = '测试报告主题'
        self.msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')

        # 读取邮件正文的文件
        with open(os.path.join(mailbodyPath, "邮件版本1.txt"), 'rb') as d:
            mailbody = d.read()

        # 读取邮件附件的文件
        with open(os.path.join(reportPath, newreport), 'rb') as f:
            accessory = f.read()

        html = MIMEText(mailbody, _subtype='html', _charset='utf-8')
        self.msg.attach(html)

        # html附件
        att1 = MIMEText(accessory, 'base64', 'gb2312')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename="TestReport.html"'  # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        self.msg.attach(att1)

    def send(self):
        """发送邮件"""
        self.__take_messages()
        self.msg['to'] = ','.join(recvaddress)
        self.msg['Cc'] = ','.join(ccaddress)
        self.msg['from'] = sendaddr_name
        try:
            smtp = smtplib.SMTP_SSL('smtp.qq.com')
            smtp.login(sendaddr_name, sendaddr_pswd)
            smtp.sendmail(self.msg['from'], self.sendTo + ccaddress, self.msg.as_string())
            smtp.close()
            logger.info("发送邮件成功")
        except Exception:
            logger.error('发送邮件失败')
            raise


if __name__ == '__main__':
    sendMail = SendMail()
    sendMail.send()
