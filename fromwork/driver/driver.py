# -*- coding:utf-8 -*-
# 这个手动设置连接的设备信息

from macaca import WebDriver  # 导入webdriver，必须大写


class Driver(object):
	# 启动浏览器
	def browser(self):
		desired_caps = {
			'platformName': 'desktop',
			'browserName': 'electron'  # Chrome, Electron
		}
		server_url = 'http://localhost:3456'
		driver = WebDriver(desired_caps, server_url)
		return driver

	# 启动IOS虚拟机
	def ios_phone_virtual(self):
		"""
		远程路径示例：'app': 'https://npmcdn.com/android-app-bootstrap@latest/android_app_bootstrap/build/outputs/apk/
		android_app_bootstrap-debug.apk',
		:return:
		"""
		apps_path = '/Users/xxx/test-macaca/apps/'  # 自己修改路径
		desired_caps = {
			'platformName': 'iOS',
			'deviceName': 'iPhone 88',  # 自己修改型号
			'app': apps_path + 'app-debug.app'  # 自己修改app路径，名称，同时也支持远程路径
		}
		driver = WebDriver(desired_caps)
		return driver

	# 启动Android虚拟机
	def android_phone_virtual(self):
		apps_path = '/Users/xxx/test-macaca/apps/'
		desired_caps = {
			'platformName': 'android',
			'deviceName': 'xiaomi 4',  # 自己修改型号
			'app': apps_path + 'app-debug.app'  # 自己修改app路径
		}
		driver = WebDriver(desired_caps)
		return driver

	# 启动Android真机
	def android_phone(self):
		desired_caps = {
			'platformName': 'android',
			'udid': 'WTKDU16712009604',  # 自己修改udid，这是荣耀8的
			'package': 'com.tencent.mm',  # 自己修改包名
		}
		driver = WebDriver(desired_caps)
		return driver

	# 启动IOS真机
	def ios_phone(self):
		desired_caps = {
			'platformName': 'android',
			'udid': 'XXXXXXXXXXXXXXXXXXXX',  # 自己修改udid
			'package': 'com.xxxx.Maps',  # 自己修改包名
		}
		driver = WebDriver(desired_caps)
		return driver