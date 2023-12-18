import sqlite3

conn = sqlite3.connect("bd.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS stations(
    idstations INT PRIMARY KEY,
    stname TEXT,
    year TEXT,
    month TEXT,
    day TEXT,
    hour TEXT,
    dirwind TEXT,
    precipit REAL,
    temperature REAL,
    humidity REAL);""")
conn.commit()
