# -*- coding:utf-8 -*-

import os


# 截图函数
def insert_img(driver, file_name):
	# 获取当前文件所在的父级目录，其中__file__为当前文件的绝对路径
	base_dir = os.path.dirname(__file__)
	# 获取当前目录所在的父级目录
	base_dir = os.path.dirname(base_dir)
	# 将当前目录进行切片操作，其中[-1]是指列表的最后一个元素
	base = base_dir.split('/test_date')[0]
	# 将多个路径组合成截图存放路径
	file_path = base + '/test_date/report/image/' + file_name
	# 将截图保存到本地
	driver.save_screenshot(file_path)
