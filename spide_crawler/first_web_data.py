from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen(
    "https://temai.taobao.com/cheap.htm?spm=a231o.7076277%2Fb.19985674835.1.50aa46089wWDYM&prepvid=200_11.15.192.192_465_1567171979704&extra=&pid=mm_26632323_6762370_25910879&clk1=&unid=&source_id=&app_pvid=200_11.15.192.192_465_1567171979704")
# f = open("web-code.txt", "w")
# f.write(str(html.read()))
# f.close()
# s=f.read()
# print(s)
hs = BeautifulSoup(html.read())
print(hs.title)
