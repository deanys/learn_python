import pywifi
from pywifi import const
import time


class WIFICON():
    inter = ""

    def __init__(self, wifi_name):
        wifi = pywifi.PyWiFi()
        self.inter = wifi.interfaces()[0]
        self.wifi_name = wifi_name

    def wifi_status_check(self):
        if self.inter.status() == const.IFACE_CONNECTED:
            # print("wifi has been connect")
            return True
        else:
            # print("wifi no connect")
            return False

    def wifi_connect(self, password):
        print("wifi name is [{}],password is [{}]".format(self.wifi_name, password.strip()))
        profile = pywifi.Profile()
        profile.ssid = self.wifi_name
        profile.key = password
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.auth = const.AUTH_ALG_OPEN
        profile.cipher = const.CIPHER_TYPE_CCMP
        self.inter.remove_all_network_profiles()
        temfile = self.inter.add_network_profile(profile)
        self.inter.connect(temfile)
        time.sleep(5)

    def read_password_note(self):
        with open("pass.txt", "r+") as f:
            return f.readlines()

    def wifi_test(self):
        if self.wifi_status_check():
            print("wifi has been conect ,no need connect")
        for password in self.read_password_note():
            self.wifi_connect(password.strip())
            if self.wifi_status_check():
                # print("good,wifi connect ,wifi name is [{}],password is [{}]".format(self.wifi_name, password.strip()))
                return
        print("wifi no connect,password use all,sorry!")


if __name__ == '__main__':
    wif = WIFICON("test")
    wif.wifi_test()
