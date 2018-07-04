#  获取连接到电脑上的机器
#  Android ：利用 adb devices 获取连接上的所有安卓设备。
#  iOS：利用 instruments -s devices 获取连接上的所有iOS设备
#  只是代码搬运，没有试验过，来源：https://testerhome.com/topics/6810


class InitDevice:


	"""
	获取连接的设备的信息
	"""


	def __init__(self):
		self.GET_ANDROID = "adb devices"
		self.GET_IOS = "instruments -s devices"


	def get_device(self):
		value = os.popen(self.GET_ANDROID)

		device = []

		for v in value.readlines():
			android = {}
			s_value = str(v).replace("\n", "").replace("\t", "")
			if s_value.rfind('device') != -1 and (not s_value.startswith("List")) and s_value != "":
				android['platformName'] = 'Android'
				android['udid'] = s_value[:s_value.find('device')].strip()
				android['package'] = 'xxxx'
				android['activity'] = 'xxxxxx'
				device.append(android)

		value = os.popen(self.GET_IOS)

		for v in value.readlines():
			iOS = {}

			s_value = str(v).replace("\n", "").replace("\t", "").replace(" ", "")

			if v.rfind('Simulator') != -1:
				continue
			if v.rfind("(") == -1:
				continue

			iOS['platformName'] = 'iOS'
			iOS['platformVersion'] = re.compile(r'\((.*)\)').findall(s_value)[0]
			iOS['deviceName'] = re.compile(r'(.*)\(').findall(s_value)[0]
			iOS['udid'] = re.compile(r'\[(.*?)\]').findall(s_value)[0]
			iOS['bundleId'] = 'xxxx'

			device.append(iOS)

		return device


	#  2. 动态获取3456 端口后的空闲端口，获取的端口数根据上个方法中获取的设备数
	#  判断端口号是否被占用是去执行 netstat -an | grep port这条命令判断端口号是否被占用

	def is_using(port):
		"""
		判断端口号是否被占用
		:param port:
		:return:
		"""
		cmd = "netstat -an | grep %s" % port

		if os.popen(cmd).readlines():
			return True
		else:
			return False


	def get_port(count):
		"""
		获得3456端口后一系列free port
		:param count:
		:return:
		"""
		port = 3456
		port_list = []
		while True:
			if len(port_list) == count:
				break

			if not is_using(port) and (port not in port_list):
				port_list.append(port)
			else:
				port += 1

		return port_list


#  3. 开启macaca服务，为每一个service动态分布一个端口
#  start_server: 开启一个进程池，每一个device对应一个macaca server
#  run_server：运行macaca server
#  is_running：判断server是否有开启成功，判断的方法为：去访问每个server对应的http://127.0.0.1:port/wd/hub/status地址，看看返回的状态码是不是以2 开头。
#  run_test：运行脚本
class macacaServer():
	def __init__(self, devices):

		self.devices = devices
		self.count = len(devices)
		self.url = 'http://127.0.0.1:%s/wd/hub/status'

	def start_server(self):

		pool = Pool(processes=self.count)
		port_list = get_port(self.count)

		for i in range(self.count):
			pool.apply_async(self.run_server, args=(self.devices[i], port_list[i]))

		pool.close()
		pool.join()

	def run_server(self, device, port):

		r = RunServer(port)
		r.start()

		while not self.is_running(port):
			sleep(1)

		server_url = {
			'hostname': "ununtrium.local",
			'port': port,
		}
		driver = WebDriver(device, server_url)
		driver.init()

		DRIVER.set_driver(driver)
		DRIVER.set_OS(device.get("platformName"))

		self.run_test()

	def run_test(self):
		"""运行测试
		"""
		all_test = AllTests()
		all_test.run_case()

	def is_running(self, port):
		"""Determine whether server is running
		:return:True or False
		"""
		url = self.url % port
		response = None
		try:
			response = requests.get(url, timeout=0.01)

			if str(response.status_code).startswith('2'):
				# data = json.loads((response.content).decode("utf-8"))

				# if data.get("staus") == 0:
				return True

			return False
		except requests.exceptions.ConnectionError:
			return False
		except ReadTimeout:
			return False
		finally:
			if response:
				response.close()


class RunServer(threading.Thread):

	def __init__(self, port):
		threading.Thread.__init__(self)
		self.cmd = 'macaca server -p %s --verbose' % port

	def run(self):
		os.system(self.cmd)
