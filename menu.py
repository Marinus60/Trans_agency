import os
import sqlite3 as sq



def main_menu():
    con = sq.connect("database.db")
    cur = con.cursor()
    cur.execute("""SELECT * FROM language""")
    lang=cur.fetchone()
    l=int(lang[0])
    a=[]
    f=open('translate.txt','r')
    for line in f:
        string=line.rstrip('\n').split(',')
        a.append([string[0],string[1]])
    os.system('clear')

    print("1 "+a[0][l])
    print("2 "+a[1][l])
    print("3 Orders (Заказы)")
    print("4 Choose language (Выбрать язык)")

    print("0 Exit (Выход)", end='\n\n')
    n = input("Select (Выберите): ")
    if n == '0': return '0'
    if n == '1': return branches_menu()
    if n == '2': return transport_menu()
    if n == '3': return orders_menu()
    if n == '4': return language_menu()


def language_menu():
    lang=0

def branches_menu():
    os.system('clear')
    print("1 View branches (Просмотр филиалов)")
    print("2 Add branches (Добавить филиал)")
    print("3 Delete branches (Удалить филиал)")
    print("0 Back (Назад)", end='\n\n')
    n = input("Select (Выберите): ")
    if n == '0':
        return main_menu()
    else:
        return 'b'+n

def transport_menu():
    os.system('clear')
    print("1 View transport (Просмотр транспорта)")
    print("2 Add transport (Добавить транспорт")
    print("3 Delete transport (Удалить транспорт")
    print("0 Back (Назад)", end='\n\n')
    n = input("Select (Выберите): ")
    if n == '0':
        return main_menu()
    else:
        return 't'+n

def orders_menu():
    os.system('clear')
    print("1 View orders (Просмотр заказов)")
    print("2 Add branches (Новый заказ)")
    print("0 Back (Назад)", end='\n\n')
    n = input("Select (Выберите): ")
    if n == '0':
        return main_menu()
    else:
        return 'o'+n

