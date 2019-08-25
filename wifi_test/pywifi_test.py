import pywifi
from pywifi import const

wifi = pywifi.PyWiFi()
interface = wifi.interfaces()[0]
print(interface, type(interface))
# if interface in [const.IFACE_DISCONNECTED,
#               const.IFACE_INACTIVE]:
# print('已连接')
if interface.status() == const.IFACE_CONNECTED:
    print("wifi has been bbconnect")
else:
    print("wifi no connect")