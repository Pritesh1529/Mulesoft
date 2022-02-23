from msilib.schema import Directory
from platform import release
import sqlite3
class demo:
        db = sqlite3.Connection("Movies.db")
        db.execute("create table if not exists movie(id int primary key,name varchar(50), actor vaechar(50), actress varchar(50), director varchar(50), release_year int)")
        print("table successfull created")

    def insert(self):
        id = int (input("Enter Id:"))
        name = input("Enter movie name:")
        actor_name = input("Enter Actor name:")
        actress_name = input("Enter Actress name:")
        Directory_name = input("Enter Director name:")
        release_year = int (input("enter release date:"))


        self.db.execute("insert into movie(id,name,actor,actress,director,release_year)values(?,?,?,?,?,?)",(id,name,actor_name,actress_name,Directory_name,release_year))
        self.db.commit()
        print("data insert successfully")

    def select(self):
        self.data = db.execute("select * from movie")
        for row in data:
            print("ID: {}, name: {},Actor: {},Actress: {},Director: {} Release year: {}".format(row[0],row[1],row[2],row[3],row[3],row[4],row[5]))

    def update(self):
        id = int (input("Enter Id:"))
        name = input("Enter movie name:")
        actor_name = input("Enter Actor name:")
        actress_name = input("Enter Actress name:")
        Directory_name = input("Enter Director name:")
        release_year = int (input("enter release date:"))

        self.db.execute("update movie set name = ?,actor=?,actress=?,director=?,release_year=? where id=?",(id,name,actor_name,actress_name,Directory_name,release_year))
        self.db.commit()
        print("data update successfully")

    def delete(self):
        print("Delete table")

        id = int(input("enter id:"))

        self.db.execute("delete from movie where id =?",(id))
        self.db.commit()
        print("record deleted")

con = demo()

while(True):
    print("1. Add data")
    print("2. view data")
    print("3. update data")

    var = int(input("choose from 1-3:"))

    if var == 1:
        con= demo()
        con.insert()
    elif var ==2:
        con.demo()
        con.display()
    elif var ==3:
        con.demo()
        con.update()
    elif var == 4:
        con.demo()
        con.delete()
    else:
        ("enter valid choice")


