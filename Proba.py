import sqlite3
import hashlib



with sqlite3.connect('search-base.db') as db:
    cursor = db.cursor()
    query = """
    CREATE TABLE IF NOT EXISTS sirt(
        name TEXT,
        time TEXT,
        gr TEXT
)
    """
    cursor.executescript(query)

search = input('Действие: ')
fen = input('пон')
if search == 'Создать':
    db = sqlite3.connect("search-base.db")
    cursor = db.cursor()
    name = input('Ведите имя: ')
    time = input('Время ')
    gr = input('Какая группа: ')
    values = [name, time, gr]
    cursor.execute("INSERT INTO sirt(name,time, gr) VALUES(?,?,?)", values)
    print("Cоздано")



cursor.execute('SELECT * FROM  users')
three_results = cursor.fetchall()
print(three_results)
if search == 'Поиск':
    db = sqlite3.connect("search-base.db")
    cursor = db.cursor()
    search = input('Поиск')
    a = '''SELECT * FROM users WHERE name LIKE '%A%'''
    d = cursor.execute(f'''SELECT * FROM users WHERE name LIKE '%{fen}%';''')
    b = cursor.execute(f'''SELECT * FROM users WHERE gr LIKE '%{fen}%';''')
    s = cursor.execute(f'''SELECT * FROM users WHERE time LIKE '%{fen}%';''')


if search == 'Удалить':
    db = sqlite3.connect("search-base.db")
    cursor = db.cursor()
    rut = input('Что удалить: ')
    cursor.execute(f'''DELETE FROM users WHERE name = '{rut}';''')

db.commit()