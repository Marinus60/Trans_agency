import os


def main_menu():
    os.system('clear')
    print("1 Branches (Филиалы)")
    print("2 Transport (Транспорт)")
    print("3 Orders (Заказы)")
    print("0 Exit (Выход)", end='\n\n')
    n = input("Select (Выберите): ")
    if n == '0': pass
    if n == '1': return branches_menu()
    if n == '2': return transport_menu()
    if n == '3': return orders_menu()


def branches_menu():
    os.system('clear')
    print("1 View branches (Просмотр филиалов)")
    print("2 Add branches (Добавить филиал)")
    print("3 Delete branches (Удалить филиал)")
    print("0 Back (Назад)", end='\n\n')
    n = input("Select (Выберите): ")
    if n == '0':
        main_menu()
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
        main_menu()
    else:
        return 't'+n

def orders_menu():
    os.system('clear')
    print("1 View orders (Просмотр заказов)")
    print("2 Add branches (Новый заказ)")
    print("0 Back (Назад)", end='\n\n')
    n = input("Select (Выберите): ")
    if n == '0':
        main_menu()
    else:
        return 'o'+n

