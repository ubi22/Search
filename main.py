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
        password VARCHAR(20)
)
    """

    cursor.executescript(query)

class DemoPage(Screen):
    pass

class sDrawer(BoxLayout):
    pass


class ClickableTextFieldRound(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()

class Kniga(MDApp):
    theme_cls = ThemeManager()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data_tables = None

    def createButton(self, a, f, d):
        conten = sDrawer()
        conten.add_widget(ThreeLineListItem(text=f'{f}',secondary_text=f"{a}",tertiary_text=f"{d}"))
        self.root.ids.create.add_widget(conten)



    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_file("filekv.kv")

    def registration(self):
        login = self.root.ids.log.text
        password = self.root.ids.pase.text
        try:
            db = sqlite3.connect("database.db")
            cursor = db.cursor()

            db.create_function("md5", 1, md5sum)

            cursor.execute("SELECT login FROM users WHERE login = ?", [login])
            if cursor.fetchone() is None:
                values = [login, password]
                cursor.execute("INSERT INTO users(login, password) VALUES(?,md5(?))", values)
                toast("Создали акаунт")
                db.commit()
            else:
                toast("Tакой логин уже есть")

        except sqlite3.Error as e:
            print("Error", e)
        finally:
            cursor.close()
            db.close()

    def log_in(self):
        login = self.root.ids.log.text
        password = self.root.ids.pase.text
        self.create_data()
        if login == 'admin':
            if password == '1234':
                toast("Здраствуйте Admin")
                self.root.ids.screen_manager.current = "admin"
        else:
            try:
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


Kniga().run()