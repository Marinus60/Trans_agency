import os


def table_creator(title, rec):
    os.system('clear')
    for tit in title:
        t = (15 - len(tit))
        print("|" + " " * (t // 2) + tit + " " * (t // 2 + t % 2), end='')
    print('|')
    print(("|" + 15 * "-") * len(title) + "|")

    for row in rec:
        for el in row:
            t = (15 - len(str(el)))
            print("|" + " " * (t // 2) + str(el) + " " * (t // 2 + t % 2), end='')
        print('|')
        print(("|" + 15 * "-") * len(title) + "|")
