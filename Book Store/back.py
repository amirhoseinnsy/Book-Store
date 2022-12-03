import sqlite3

def Connect():
    conn = sqlite3.connect("./Books")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, title VARCHAR , year INTEGER , "
                "author VARCHAR , ISBN "
                " INTEGER)")
    conn.commit()
    conn.close()

def View_All():
    conn = sqlite3.connect("./Books")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    row = cur.fetchall()
    conn.commit()
    conn.close()
    return row

def Add(title, year, author, ISBN):
    conn = sqlite3.connect("./Books")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL , ?, ?, ?, ?)", (title, year, author, ISBN))
    conn.commit()
    conn.close()

def Search(title, year, author, ISBN):
    conn = sqlite3.connect("./Books")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE  title=? OR year=? OR author=? OR ISBN=?", (title, year, author, ISBN))
    row = cur.fetchall()
    conn.commit()
    conn.close()
    return row

def Update(id, title, year, author, ISBN):
    conn = sqlite3.connect("./Books")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?, year=? , author=? , ISBN=? WHERE id=?", (title, year, author, ISBN, id))
    conn.commit()
    conn.close()

def Delete(id):
    conn = sqlite3.connect("./Books")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id, ))
    conn.commit()
    conn.close()

Connect()
Update(7, "harrypotter",2014,"JK",  201447954)