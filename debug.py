import sqlite3

conn = sqlite3.connect("vitivinicultura.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM PRODUCAO LIMIT 5")
for row in cursor.fetchall():
    print(row)

conn.close()
