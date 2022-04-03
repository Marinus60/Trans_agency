import sqlite3 as sq
import menu


def create_db():
    con = sq.connect("database.db")
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS branch")
    cur.execute("""CREATE TABLE IF NOT EXISTS branch (
                id_city INTEGER PRIMARY KEY AUTOINCREMENT,
                name_city TEXT,
                coord_city TEXT,
                category_city TEXT)""")
    cur.execute("DROP TABLE IF EXISTS transports")
    cur.execute("""CREATE TABLE IF NOT EXISTS transports (
                id_trans INTEGER PRIMARY KEY AUTOINCREMENT,
                name_trans TEXT,
                price INTEGER,
                speed INTEGER,
                category_city TEXT
                )""")
    cur.execute("DROP TABLE IF EXISTS orders")
    cur.execute("""CREATE TABLE IF NOT EXISTS orders (
                id_sender INTEGER,
                id_recipient INTEGER,
                id_trans INTEGER,
                weight INTEGER
                )""")

    con.close()

""""  def __init__(self,*args):
        self.id_city = id_city
        self.name_city = name_city
        self.coord_city = coord_city
        self.category_city = category_city
        """
class Branch():

    def add_branch(self):
        con = sq.connect("database.db")
        cur = con.cursor()
        name_city=input("Enter the name of the city: ")
        coord_city=input("Enter city coordinates: ")
        category_city=input("Enter city category: ")
        query = """INSERT INTO branch
                                      (name_city, coord_city, category_city)
                                      VALUES (?, ?, ?);"""
        data = (name_city,coord_city,category_city)
        cur.execute(query, data)
        con.commit()
        con.close()
        menu.main_menu()
    def del_branch(self):
        con = sq.connect("database.db")
        cur = con.cursor()
        name_city = input("Enter the name of the city: ")
        query="""DELETE FROM branch WHERE name_city = ?"""
        cur.execute(query,(name_city,))
        con.commit()

        con.close()
        menu.main_menu()
    def view_branch(self):
        con = sq.connect("database.db")
        cur = con.cursor()
        cur.execute("""SELECT * FROM branch""")
        rec = cur.fetchall()
        print(len(rec))
        for row in rec:
            print("ID_city:", row[0])
            print("Name_city:", row[1])
            print("Coord_city:", row[2])
            print("Category_city:", row[3], end="\n\n")
        con.close()
        input("Press any key!!!")
        menu.main_menu()


class Transport:
    def __init__(self):
        self.id_trans = id_trans
        self.name_trans = name_trans
        self.price = price
        self.speed = speed
        self.category = category

class Orders(Branch,Transport):
    def __init__(self):
        self.id_order=id_order
        self.weight=weight

#create_db()
agency=Branch()
m=menu.main_menu()
if m=='b1': agency.view_branch()
if m=='b2': agency.add_branch()
if m=='b3': agency.del_branch()


