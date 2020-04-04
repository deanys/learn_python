import sys
import os
from mysql_connect import Mysql


def display():
    print("**********************学生管理系统***************************")
    print("*=====================功能目录==============================*")
    print("*                     1.录入学生信息                        *")
    print("*                     2.查找学生信息                        *")
    print("*                     3.删除学生信息                        *")
    print("*                     4.修改学生信息                        *")
    print("*                     5.排序                                *")
    print("*                     6.统计学生总人数                      *")
    print("*                     7.显示所有学生信息                    *")
    print("*                     0. 退出系统                           *")
    print("*************************************************************")


def sacn_input_student():
    ins_sql = Mysql()
    while True:
        input_student = input("请按姓名，性别，数学，英语，语文方式输入").split(",")
        print(input_student)
        ins_sql.insert_date_to_sql(input_student)
        if str(input("请确定是否接着输入，Y确认")).upper() != "Y":
            break


def search_student():
    ins_sql = Mysql()
    res = ins_sql.fetch_one_data(input("请输入姓名"))
    print(res[0])


def del_student():
    ins_sql = Mysql()
    ins_sql.del_date(input("请输入姓名"))


def delete_student():
    ins_sql = Mysql()
    ins_sql.del_date(input("请输入姓名"))


def change_student():
    Mysql().update_to_mysql(input("更改姓名"), input("科目"), input("分数"))


def all_info():
    res = Mysql().fetch_all_data()
    for result in res:
        print(result)


def choice_menu():
    input_test = int(input("请输入数字选择功能"))
    if input_test == 0:
        sys.exit()
    elif input_test == 1:
        sacn_input_student()
    elif input_test == 2:
        search_student()
    elif input_test == 3:
        delete_student()
    elif input_test == 4:
        change_student()
    elif input_test == 5:
        pass
    elif input_test == 6:
        pass
    elif input_test == 7:
        all_info()
    else:
        raise ValueError


if __name__ == '__main__':
    display()
    choice_menu()
    display()
    choice_menu()
