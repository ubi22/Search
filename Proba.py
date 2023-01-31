import sqlite3
import hashlib

db = sqlite3.connect("search-base.db")
cur = db.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS users(
    name TEXT
    );            
''')

search = input('Действие: ')
fen = input('пон')
if search == 'Создать':
    name = input('Ведите имя: ')
    values = [name]
    cur.execute("INSERT INTO users(name) VALUES(?)", values)
    print("Cоздано")

g = cur.execute(f'''SELECT * FROM users
WHERE name LIKE '%{fen}%';''')

cur.execute('SELECT * FROM  users')
three_results = cur.fetchall()
print(three_results)
if search == 'Поиск':
    search = input('Поиск')
    a = '''SELECT * FROM users WHERE artist LIKE '%Audiosl%'''
    if search == three_results:
        print(search)
    else:
        print('Поястояное')

if search == 'Удалить':
    rut = input('Что удалить: ')
    cur.execute(f'''DELETE FROM users WHERE name = '{rut}';''')

db.commit()