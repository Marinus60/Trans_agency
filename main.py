import sqlite3 as sq
import menu
import table


def create_db():
    con = sq.connect("database.db")
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS language")

    cur.execute("""CREATE TABLE IF NOT EXISTS language (
                lang INTEGER)
                """)
    cur.execute("""INSERT INTO language (lang) VALUES (0)""")
    con.commit()
 #   cur.execute("DROP TABLE IF EXISTS branch")
    cur.execute("""CREATE TABLE IF NOT EXISTS branch (
                id_city INTEGER PRIMARY KEY AUTOINCREMENT,
                name_city TEXT,
                coord_city TEXT,
                category_city TEXT)""")
 #   cur.execute("DROP TABLE IF EXISTS transports")
    cur.execute("""CREATE TABLE IF NOT EXISTS transports (
                id_trans INTEGER PRIMARY KEY AUTOINCREMENT,
                name_trans TEXT,
                price INTEGER,
                speed INTEGER,
                category_city TEXT
                )""")
  #  cur.execute("DROP TABLE IF EXISTS orders")
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
class Branch:

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
        return menu.main_menu()
    def del_branch(self):
        con = sq.connect("database.db")
        cur = con.cursor()
        print()
        id_city = input("Enter ID of the city: ")
        query="""DELETE FROM branch WHERE id_city = ?"""
        cur.execute(query,(id_city,))
        con.commit()

        con.close()
        return menu.main_menu()
    def view_branch(self):
        con = sq.connect("database.db")
        cur = con.cursor()
        cur.execute("""SELECT * FROM branch""")
        rec = cur.fetchall()
        title = ("ID_city", "Name_city", "Coord_city", "Cat_city")

        table.table_creator(title,rec)
        con.close()
        input("Press any key!!!")

class Transport(Branch):

    def add_transport(self):
        con = sq.connect("database.db")
        cur = con.cursor()
        name_trans=input("Enter the name of the transport: ")
        price=input("Enter cost of delivery: ")
        speed=input("Enter delivery speed: ")
        category_city=input("Enter city category: ")

        query = """INSERT INTO transports
                (name_trans, price, speed, category_city)
                VALUES (?, ?, ?, ?);"""
        data = (name_trans, price, speed, category_city)
        cur.execute(query, data)
        con.commit()
        con.close()
        return menu.main_menu()
    def del_transport(self):
        con = sq.connect("database.db")
        cur = con.cursor()
        name_city = input("Enter ID of the transport: ")
        query="""DELETE FROM transports WHERE id_trans = ?"""
        cur.execute(query,(name_city,))
        con.commit()

        con.close()
        return menu.main_menu()
    def view_transport(self):
        con = sq.connect("database.db")
        cur = con.cursor()
        cur.execute("""SELECT * FROM transports""")
        rec = cur.fetchall()
        title = ("ID_trans", "Name_trans", "Price", "Speed", "Cat_city")


        table.table_creator(title,rec)
        con.close()
        input("Press any key!!!")

class Orders:
    def __init__(self):
        self.id_order=id_order
        self.weight=weight
m=''
#create_db()
agency=Transport()
while m!='0':
    m=menu.main_menu()
    if m=='b1': agency.view_branch()
    if m=='b2': agency.add_branch()
    if m=='b3': agency.del_branch()
    if m=='t1': agency.view_transport()
    if m=='t2': agency.add_transport()
    if m=='t3': agency.del_transport()




