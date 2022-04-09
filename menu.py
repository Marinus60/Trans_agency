import os
import sqlite3 as sq



def main_menu():
    con = sq.connect("database.db")
    cur = con.cursor()
    cur.execute("""SELECT * FROM language""")
    lang=cur.fetchone()
    global l
    l=int(lang[0])
    global a
    a=[]
    f=open('translate.txt','r')
    for line in f:
        string=line.rstrip('\n').split(',')
        a.append([string[0],string[1]])
    os.system('clear')

    print("1 "+a[0][l])
    print("2 "+a[1][l])
    print("3 "+a[2][l])
    print("4 "+a[3][l])

    print("0 "+a[4][l], end='\n\n')
    n = input(a[-1][l]+':')
    if n == '0': return '0'
    if n == '1': return branches_menu()
    if n == '2': return transport_menu()
    if n == '3': return orders_menu()
    if n == '4': return language_menu()


def language_menu():
    os.system('clear')
    print("1 " + a[13][l])
    print("2 " + a[14][l])
    print("0 " + a[-2][l], end='\n\n')
    n = input(a[-1][l] + ':')
    if n == '0':
        return main_menu()
    else:
        con = sq.connect("database.db")
        cur = con.cursor()
        if n=='1':
            cur.execute("""UPDATE language SET lang=0""")
        elif n=='2':
            cur.execute("""UPDATE language SET lang=1""")

        con.commit()
        con.close()

def branches_menu():
    os.system('clear')
    print("1 "+a[5][l])
    print("2 "+a[6][l])
    print("3 "+a[7][l])
    print("0 "+a[-2][l], end='\n\n')
    n = input(a[-1][l]+':')
    if n == '0':
        return main_menu()
    else:
        return 'b'+n

def transport_menu():
    os.system('clear')
    print("1 "+a[8][l])
    print("2 "+a[9][l])
    print("3 "+a[10][l])
    print("0 "+a[-2][l], end='\n\n')
    n = input(a[-1][l]+':')
    if n == '0':
        return main_menu()
    else:
        return 't'+n

def orders_menu():
    os.system('clear')
    print("1 "+a[11][l])
    print("2 "+a[12][l])
    print("0 " + a[-2][l], end='\n\n')
    n = input(a[-1][l] + ':')
    if n == '0':
        return main_menu()
    else:
        return 'o'+n

