import sqlite3
import hashlib



with sqlite3.connect('search-base.db') as fut:
    searchs = fut.cursor()
    table = """
    CREATE TABLE IF NOT EXISTS search(
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
    searchs.execute("INSERT INTO search(name,time, gr) VALUES(?,?,?)", values)
    print("Cоздано")




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
