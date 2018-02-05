#coding=utf-8

import os,time
from public.common.readconfig import ReadConfig

# 读取配置文件
config_file_path = os.path.split(os.path.realpath(__file__))[0]
read_config = ReadConfig(os.path.join(config_file_path,'config.ini'))
# 项目参数设置
prj_path = read_config.getValue('projectConfig','project_path')
# 日志路径
log_path = os.path.join(prj_path, 'report', 'log')
# 截图文件路径
img_path = os.path.join(prj_path, 'report', 'image')
# 测试报告路径
today = time.strftime("%Y-%m-%d")
report_path = os.path.join(prj_path, 'report', 'testreport',today)
if not os.path.exists(report_path):
    os.makedirs(report_path)
# 默认浏览器
browser = 'firefox'

# 测试数据路径
data_path = os.path.join(prj_path, 'data', 'testdata')

# 邮件正文路径
mail_path = os.path.join(prj_path, 'data', 'mailbody')
