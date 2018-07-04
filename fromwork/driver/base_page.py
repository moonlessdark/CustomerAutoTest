# -*- coding:utf-8 -*-

from fromwork.function.log import Logger
import os

logger = Logger(logger="BasePage").getlog()


class Base(object):
	"""
	基本层
	"""

	def __init__(self, driver):
		self.driver = driver

	def open(self, url):
		"""
		在当前浏览器会话中加载Web页面
		:param url: 导航到的URL
		:return: WebDriver对象
		"""
		self.driver.set_window_size(1280, 800)
		self.driver.get(url)
		logger.info("日志：打开浏览器并跳转到网址:" + url)

	def quit_browser(self):
		"""
		关闭当前打开的浏览器
		:return: 关闭浏览器
		"""
		self.driver.quit()
		logger.info("日志：关闭浏览器")

	def forward(self):
		"""
		前进，需要先后退一页或多页
		:return: 前进一页
		"""
		self.driver.forward()
		logger.info("日志：浏览器向前一页")

	def back(self):
		"""
		后退一页
		:return:后退一页
		"""
		self.driver.back()
		logger.info("日志：浏览器后退一页")

	def refresh(self):
		"""
		刷新页面
		:return: 刷新当前页面
		"""
		self.driver.refresh()
		logger.info("日志：刷新当前页面")

	def source(self):
		"""
		获取当前页面的源代码
		:return: 页面的源代码
		"""
		logger.info("开始获取页面的源代码")
		return self.driver.source

	def id(self, _id):
		"""
		通过ID查找元素
		:param _id: 元素的ID
		:return: WebElement对象
		"""
		logger.info("开始通过ID"+_id+"来进行元素定位")
		return self.driver.element_by_id(_id)


	def xpath_or_none(self, xpath):
		"""
		通过XMLPath查找元素
		:param xpath: 元素的XMLPath
		:return: 如果元素存在，返回WebElement对象，否则返回None
		"""
		logger.info("开始通过ID" + xpath + "来进行元素定位")
		return self.driver.element_by_xpath_or_none(xpath)


	def css_selector_if_exists(self, css_selector):
		"""
		通过CSS选择器判断元素是否存在
		:param css_selector: 元素的CSS选择器
		:return: 如果元素存在，返回True，否则返回False
		"""
		logger.info("开始通过ID" + css_selector + "来判断元素是否存在")
		return self.driver.element_by_css_selector_if_exists(css_selector)
