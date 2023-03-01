import sqlite3
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.metrics import dp
from kivymd.uix.tab import MDTabsBase
from kivymd.app import MDApp
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.icon_definitions import md_icons
from kivy.properties import StringProperty
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList
from kivymd.uix.button import MDRaisedButton
from kivymd.font_definitions import fonts
from kivymd.icon_definitions import md_icons
from kivymd.uix.card import MDCardSwipe
import datetime
from kivymd.uix.screen import MDScreen
from kivymd.uix.chip import MDChip
from kivy.animation import Animation
from kivy.factory import Factory
from kivymd.uix.menu import MDDropdownMenu
from kivy.clock import Clock
from kivymd.uix.dialog import MDDialog
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.list import ThreeLineListItem
from kivymd.uix.button import MDFlatButton
import webbrowser
from kivymd.uix.button import MDRaisedButton
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
from kivy.core.window import Window
from kivy.core.window import Window
import sqlite3
import hashlib
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.toast import toast
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.theming import ThemeManager
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.lang.builder import Builder
Window.size = (480,800)




def md5sum(value):
    return hashlib.md5(value.encode()).hexdigest()

with sqlite3.connect('database.db') as db:
    cursor = db.cursor()
    query = """
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        login VARCHAR(15),
        password VARCHAR(20),
        name TEXT,
        age TEXT
        
)
    """

    cursor.executescript(query)

with sqlite3.connect('search-base.db') as fut:
    db = fut.cursor()
    table = """
    CREATE TABLE IF NOT EXISTS search(
        name TEXT,
        time TEXT,
        gr TEXT
)
    """
    db.executescript(table)


class sDrawer(BoxLayout):
    pass

class ClickableTextFieldRound(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()

class Schedule(MDApp):
    icon = "/Search-master/КвантИконка.jpg"
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_file("filekv.kv")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            preview=True,
        )


    def file_manager_open(self):
        self.file_manager.show('/Search-master/Икон/')  # output manager to the screen
        self.manager_open = True

    def select_path(self, path):
        '''It will be called when you click on the file name
        or the catalog selection button.

        :type path: str;
        :param path: path to the selected directory or file;
        '''

        self.exit_manager()
        self.root.ids.cin.icon = f'{path}'
        self.root.ids.acc.icon = f'{path}'

    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''

        self.manager_open = False
        self.file_manager.close()

    def events(self, instance, keyboard, keycode, text, modifiers):
        '''Called when buttons are pressed on the mobile device.'''

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True

    def registration(self):
        login = self.root.ids.log.text
        password = self.root.ids.pase.text
        name = self.root.ids.names.text
        age = self.root.ids.age.text
        try:
            db = sqlite3.connect("database.db")
            cursor = db.cursor()

            db.create_function("md5", 1, md5sum)

            cursor.execute("SELECT login FROM users WHERE login = ?", [login])




            if cursor.fetchone() is None:
                values = [login, password, name, age]
                cursor.execute("INSERT INTO users(login, password, name, age) VALUES(?,md5(?),?,?)", values)
                toast("Создали акаунт")
                self.root.ids.screen_manager.current = "search"
                db.commit()
            else:
                toast("Tакой логин уже есть")

        except sqlite3.Error as e:
            print("Error", e)
        finally:
            cursor.close()
            db.close()

    def log_in(self):
        login = self.root.ids.login.text
        password = self.root.ids.password.text
        if login == 'admin':
            if password == '1234':
                toast("Здраствуйте Admin")
                self.root.ids.screen_manager.current = "admin"
        else:
            try:
                db = sqlite3.connect("database.db")
                cursor = db.cursor()
                db.create_function("md5", 1, md5sum)
                cursor.execute("SELECT login FROM users WHERE login = ?", [login])
                if cursor.fetchone() is None:
                    toast("Такого логина не существует")
                else:
                    cursor.execute("SELECT login FROM users WHERE login = ? AND password = md5(?)", [login, password])
                    if cursor.fetchone() is None:
                        toast("Пороль не верный")
                    else:
                        toast("Вы вошли")
                        self.root.ids.screen_manager.current = "search"
            except sqlite3.Error as e:
                print('Error, e')
            finally:
                cursor.close()
                db.close()

    def createbase(self):
        name = self.root.ids.name.text
        time = self.root.ids.time.text
        gr = self.root.ids.gr.text
        try:
            fut = sqlite3.connect("search-base.db")
            searchs = fut.cursor()
            values = [name, time, gr]
            searchs.execute("INSERT INTO search(name,time, gr) VALUES(?,?,?)", values)
            print(values)
            fut.commit()
            self.root.ids.screen_manager.current = "admin"
        except sqlite3.Error as e:
            print("Error", e)

    def delbase(self):
        try:
            fut = sqlite3.connect("search-base.db")
            searchs = fut.cursor()
            rut = self.root.ids.delete.text
            searchs.execute(f'''DELETE FROM search WHERE name = '{rut}';''')
            fut.commit()
            self.root.ids.screen_manager.current = "admin"
        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)

    def screen(self, sed):
        self.root.ids.screen_manager.current = sed

    def searchs(self):
        fut = sqlite3.connect("search-base.db")
        searchs = fut.cursor()
        poisk = self.root.ids.poisks.text
        searchs.execute(f'''SELECT * FROM search WHERE name LIKE '%{poisk}%';''')
        three_results = searchs.fetchall()
        conten = sDrawer()
        if len(three_results) == 0:
            print('Ведите имя')
        else:

            for a, b, c in three_results:

                conten.add_widget(ThreeLineListItem(text=f'ФИО: {a}', secondary_text=f"Время: {b}", tertiary_text=f"Группа: {c}"))
                self.root.ids.md_list.add_widget(conten)


    def account(self):
        db = sqlite3.connect("database.db")
        cursor = db.cursor()
        a = self.root.ids.login.text
        cursor.execute(f'''SELECT * FROM users WHERE login LIKE '%{a}%';''')
        three_results = cursor.fetchall()
        self.root.ids.nameac.text = f"ФИО: {three_results[0][3]}"
        self.root.ids.ageac.text = f"Лет: {three_results[0][4]}"

Schedule().run()
