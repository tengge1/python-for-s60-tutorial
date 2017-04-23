#作者：√ゞ絕配ぷ无恋℡
#解释绝大部分为tengge所加…
#socket.access_point可以设置一个接入点进行接入，先由它启动网络，就可以不询问用户接入点，而且可以断开网络，不必在软件应用过程中一直联网！

#本程序可显示各个接入点的IP地址
import socket
id = socket.select_access_point()
#选择接入点，返回一个整数，其实就是第几个接入点
apo = socket.access_point(id)
#由接入点返回一个ap对象
apo.start()
#启动网络连接
print apo.ip()
#打印IP地址

#断开网络链接
import socket,e32
api=socket.select_access_point()
apo=socket.access_point(api)
apo.start()
e32.ao_sleep(2)
#这里放需要联网的函数（此时不会让用户接入点）
apo.stop()
#断开网络连接
#注意，第二个程序让用户选择接入点不是联网的函数产生的，而是由socket.select_access_point产生的，如果上述程序去掉该句，再将api改成1（即默认选择第一个接入点），就不会让用户选择接入点…
