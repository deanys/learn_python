import sys
from PyQt5.QtWidgets import QWidget

out = sys.stdout
sys.stdout = open(r"api.txt", "w")
help(QWidget)
s = lambda x: x + 2
print(s(3))
sys.stdout.close()
sys.out = out

