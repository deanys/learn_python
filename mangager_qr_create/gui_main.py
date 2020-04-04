import random
import pyqrcode

__auther__ = "dean"
auth_explan = """
1.生成六位数字随机数，可重复，模拟短信验证
2.九位数字产品代号，后六位随机
3.25位随机数
4.数据分析防伪标准
"""
main_gui = '''
*******************************************
            企业编码生成系统
*******************************************
*       1.生成6位数字防伪编码(213563)      *
*       2.生成9位数字防伪编码(879-335493)  *
*       3.生成25位数字防伪编码             *
*       4.生成含数据分析功能的方位码        *
*       5.条形码批量生成                   *
*       6.二维码批量输出                   *
*       7.企业粉丝防伪码抽奖               *
*       8.退出系统                         *
'''


def display():
    print("{}".format(main_gui))


def number_code_create(num=1):
    letter = "0123456789"
    for j in range(num):
        rand_number = ""
        for i in range(6):
            rand_number = rand_number + random.choice(letter)
        print(rand_number)


display()
number_code_create(300)
