import sqlite3
import hashlib



<<<<<<< HEAD
with sqlite3.connect('search-base.db') as db:
    cursor = db.cursor()
    query = """
    CREATE TABLE IF NOT EXISTS sirt(
=======
with sqlite3.connect('search-base.db') as fut:
    searchs = fut.cursor()
    table = """
    CREATE TABLE IF NOT EXISTS search(
>>>>>>> origin/master
        name TEXT,
        time TEXT,
        gr TEXT
)
    """
    searchs.executescript(table)

search = input('Действие: ')
poisk = input('Поиск: ')
if search == 'Создать':
    fut = sqlite3.connect("search-base.db")
    searchs = fut.cursor()
    name = input('Ведите имя: ')
    time = input('Время ')
    gr = input('Какая группа: ')
    values = [name, time, gr]
<<<<<<< HEAD
    cursor.execute("INSERT INTO sirt(name,time, gr) VALUES(?,?,?)", values)
=======
    searchs.execute("INSERT INTO search(name,time, gr) VALUES(?,?,?)", values)
>>>>>>> origin/master
    print("Cоздано")



<<<<<<< HEAD
cursor.execute('SELECT * FROM  users')
three_results = cursor.fetchall()
print(three_results)
=======

>>>>>>> origin/master
if search == 'Поиск':
    fut = sqlite3.connect("search-base.db")
    searchs = fut.cursor()
    searchs.execute(f'''SELECT * FROM search WHERE name LIKE '%{poisk}%';''')
    three_results = searchs.fetchall()
    print(three_results)


if search == 'Удалить':
    fut = sqlite3.connect("search-base.db")
    searchs = fut.cursor()
    rut = input('Что удалить: ')
    searchs.execute(f'''DELETE FROM search WHERE name = '{rut}';''')

fut.commit()
fut.close()
