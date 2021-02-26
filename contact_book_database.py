import sqlite3

conn = sqlite3.connect("c_book.db")
cursor = conn.cursor()

#cursor.execute("CREATE TABLE contacts (name TEXT, number INEGER)")  CREATES DB
#cursor.execute("INSERT INTO contacts VALUES ('John', 89991236745)")
#rows = cursor.execute("SELECT name, number FROM  contacts").fetchall()

#username = str(input("Type in your username: ")) 
#user_number = int(input("Type in your number: "))

username = cursor.execute("SELECT * FROM contacts WHERE name = ?", ('Scoop',)).fetchone()
user_number = cursor.execute("SELECT * FROM contacts WHERE number = ?", (11990044,))

#cursor.execute("INSERT INTO contacts VALUES (?, ?)", (username, user_number))

conn.commit()

rows = cursor.execute("SELECT name, number FROM  contacts").fetchall()

print(username)

numb = 987654321

#cursor.execute("UPDATE contacts SET number = ? WHERE name = ?", (numb, username))

conn.commit()

rows = cursor.execute("SELECT name, number FROM  contacts").fetchall()

print(rows)

conn.close()