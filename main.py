import sqlite3

con = sqlite3.connect("bank.db")
cursor = con.cursor()

cursor.execute("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT
        name VARCHAR(20) NOT NULL,
        surname VARGCHAR(30) UNIQUE NOT NULL,
        phone_number VARCHAR(12) UNIQUE NOT NULL,
    )""")

cursor.execute("""CREATE TABLE transactions(
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        amount DECIMAL(10, 2)
                                        from_uid INTEGER NOT NULL,
                                        to_uid INTEGER NOT NULL,
               
                                        FORGEIN KEY (from_uid) REFERENCES users(id)
                        
               
               
               
               )""")
