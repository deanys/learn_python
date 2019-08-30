from bs4 import BeautifulSoup
from urllib.request import urlopen
html=urlopen("http://fund.eastmoney.com/001595.html?spm=haosou")
hs=BeautifulSoup(html.read())
print(hs)