import requests
import warnings
from requests.exceptions import RequestException
import re


class superTools:
    def testUrl(self, Url="", password="", cmd="ls -al", timeoutvalue=2):
        """
        测试URL连接并验证密码。

        这个方法用于测试给定的URL连接是否有效，并验证密码是否正确。如果连接成功且密码正确，将保存该URL为模板。

        Args:
            Url (str, optional): 要测试的URL。默认为空字符串。
            password (str, optional): 验证密码。为空时将被要求输入密码。
            cmd (str, optional): 执行命令。默认为 "ls -al"。
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
        if cmd == "":
            warnings.warn("未提供命令，将继续执行但可能会导致不期望的结果", Warning)
        self.setSystemCmd(cmd)
        try:
            if password == '':
                self.password = input("请输入连接密码：")
        except:
            print("错误的输入！")
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
