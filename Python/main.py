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
from kivymd.uix.list import OneLineListItem
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.list import ThreeLineListItem
from kivymd.uix.button import MDFlatButton
import webbrowser
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFloatingActionButton
from kivymd.uix.button import MDRaisedButton
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
from kivy.core.window import Window
from kivy.core.window import Window
import sqlite3
import hashlib
from kivy.uix.modalview import ModalView
from kivy.lang import Builder
from kivymd.uix.list import MDList
from kivymd import images_path
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivymd.toast import toast
from kivy.core.window import Window
from kivymd.utils.fitimage import FitImage
from kivy.uix.scrollview import ScrollView
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.theming import ThemeManager
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivymd.uix.bottomsheet import MDGridBottomSheet
from kivy.uix.anchorlayout import AnchorLayout
from kivy.lang.builder import Builder
from kivymd.uix.button import MDTextButton
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.snackbar import Snackbar
from kivy.factory import Factory
from kivymd.uix.button import MDIconButton
Window.size = (480,800)



class ContentNavigationDrawer(FloatLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


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
        fio TEXT,
        kvant TEXT,
        photo TEXT,
        op TEXT,
        pn1 TEXT,
        pn2 TEXT,
        vt1 TEXT,
        vt2 TEXT,
        cr1 TEXT,
        cr2 TEXT,
        cht1 TEXT,
        cht2 TEXT,
        pt1 TEXT,
        pt2 TEXT,
        cb1 TEXT,
        cb2 TEXT,
        ob TEXT
        
)
    """
    db.executescript(table)


class sDrawer(MDFloatLayout):
    pass



photo = None
ras = None
v = None
am = None
class КvantTask(MDApp):
    icon = "/Search-master/КвантИконка.jpg"

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_file("filekv.kv")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.events)
        self.manager_opens = False
        self.file_managers = MDFileManager(
            exit_manager=self.exit_managers,
            select_path=self.select_paths,
            preview=True,
        )


    def show_example_grid_bottom_sheet(self):
        bottom_sheet_menu = MDGridBottomSheet()
        data = {
            "Поиск по ФИО": "/Search-master/База/Uti.jpg",
            "Поиск по Квантомам": "/Search-master/Икон/КвантИконка.jpg",

        }
        for item in data.items():
            bottom_sheet_menu.add_item(
                item[0],
                lambda x, y=item[0]: self.searchs(y),
                icon_src=item[1],
            )
        bottom_sheet_menu.open()
    def file_image(self, b):
        global v
        global photo
        a = "/"
        d = "/Search-master/Икон/"

        if b == 1:
            self.file_managers.show(a)
            v = 1
        elif b == 0:
            self.file_managers.show(d)
            v = 0
        elif b == 2:
            self.file_managers.show(a)
            v = 2
        self.manager_opens = True


    def select_paths(self, path):
        global v
        global photo
        global ras
        '''It will be called when you click on the file name
        or the catalog selection button.

        :type path: str;
        :param path: path to the selected directory or file;
        '''
        db = sqlite3.connect("database.db")
        cursor = db.cursor()
        if v == 1:
            self.root.ids.sic.icon = f'{path}'
            photo = f"{path}"
        elif v == 0:
            self.root.ids.cin.icon = f'{path}'
            self.root.ids.sics.icon = f"{path}"
            self.root.ids.acc.icon = f'{path}'
        elif v == 2:
            ras = f"{path}"
        self.exit_managers()
        print(photo)
        cursor.close()
        db.close()



    def exit_managers(self, *args):
        '''Called when the user reaches the root of the directory tree.'''

        self.manager_opens = False
        self.file_managers.close()

    def events(self, instance, keyboard, keycode, text, modifiers):
        '''Called when buttons are pressed on the mobile device.'''

        if keyboard in (1001, 27):
            if self.manager_opens:
                self.file_managers.back()
        return True


    def registration(self):
        login = self.root.ids.log.text
        password = self.root.ids.pase.text
        name = self.root.ids.nameas.text
        age = self.root.ids.age.text
        otch = self.root.ids.otchims.text
        famal = self.root.ids.famalis.text

        fio = f"{age, otch, famal}"
        try:
            db = sqlite3.connect("database.db")
            cursor = db.cursor()

            db.create_function("md5", 1, md5sum)

            cursor.execute("SELECT login FROM users WHERE login = ?", [login])

            if cursor.fetchone() is None:
                values = [login, password, fio, age]
                cursor.execute("INSERT INTO users(login, password, name, age) VALUES(?,md5(?),?,?)", values)
                toast("Создали акаунт")
                self.root.ids.screen_manager.current = "Enter"
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
        global photo
        global ras
        name = self.root.ids.name.text
        famali = self.root.ids.famali.text
        otchim = self.root.ids.otchim.text
        fio = f"{famali} {name} {otchim}"
        kvant = self.root.ids.kvant.text
        op = self.root.ids.op.text
        pn1 = self.root.ids.pn1.text
        pn2 = self.root.ids.pn2.text
        vt1 = self.root.ids.vt1.text
        vt2 = self.root.ids.vt2.text
        cr1 = self.root.ids.cr1.text
        cr2 = self.root.ids.cr2.text
        cht1 = self.root.ids.cht1.text
        cht2 = self.root.ids.cht2.text
        pt1 = self.root.ids.pt1.text
        pt2 = self.root.ids.pt2.text
        cb1 = self.root.ids.cb1.text
        cb2 = self.root.ids.cb2.text
        ob = self.root.ids.ob.text
        try:
            fut = sqlite3.connect("search-base.db")
            searchs = fut.cursor()
            values = [fio, kvant, photo, op, pn1, pn2, vt1, vt2, cr1, cr2, cht1, cht2, pt1, pt2, cb1, cb2, ob]
            searchs.execute("INSERT INTO search(fio, kvant, photo, op, pn1, pn2, vt1, vt2, cr1, cr2, cht1, cht2, pt1, pt2, cb1, cb2, ob) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", values)
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
            searchs.execute(f'''DELETE FROM search WHERE fio = '{rut}';''')
            fut.commit()
            self.root.ids.screen_manager.current = "admin"
        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)

    def screen(self, sed):
        self.root.ids.screen_manager.current = sed

    def searchs(self, *args):
        fut = sqlite3.connect("search-base.db")
        searchs = fut.cursor()
        poisk = self.root.ids.poisks.text
        conten = sDrawer()
        if args[0] == "Поиск по ФИО":
            searchs.execute(f'''SELECT * FROM search WHERE fio LIKE '%{poisk}%';''')
            three_results = searchs.fetchall()
            if len(three_results) == 0:
                toast('Такого преподователя нет')
            elif poisk == "":
                toast('Ведите имя преподователя')
            else:
                fio = three_results[0][0]
                image = three_results[0][2]
                ob = three_results[0][16]
                op = three_results[0][3]
                kvan = three_results[0][1]
                pn1 = three_results[0][4]
                pn2 = three_results[0][5]
                vt1 = three_results[0][6]
                vt2 = three_results[0][7]
                cr1 = three_results[0][8]
                cr2 = three_results[0][9]
                cht1 = three_results[0][10]
                cht2 = three_results[0][11]
                pt1 = three_results[0][12]
                pt2 = three_results[0][13]
                cb1 = three_results[0][14]
                cb2 = three_results[0][15]
                self.root.ids.real.text = f"{fio}"
                self.root.ids.img.icon = f"{image}"
                # self.root.ids.ops.text = f'Основное направление:\n          {op}'
                # self.root.ids.obs.text = f'Образование: \n          {ob}'
                self.root.ids.screen_manager.current = "search-enter"
                data_tables = MDDataTable(
                    size_hint=(.9, .5),
                    pos_hint={"center_x": .5, "center_y": .5},
                    column_data=[
                        ("", dp(30)),
                        ("Гр.1", dp(25)),
                        ("Гр.2", dp(25)),
                    ],
                    row_data=[
                        # The number of elements must match the length
                        # of the `column_data` list.
                        (
                            "Понедельник",
                            f"{pn1}",
                            f"{pn2}",
                        ),
                        (
                            "Вторник",
                            f"{vt1}",
                            f"{vt2}",
                        ),
                        (
                            "Среда",
                            f"{cr1}",
                            f"{cr2}",
                        ),
                        (
                            "Четверг",
                            f"{cht1}",
                            f"{cht2}",
                        ),
                        (
                            "Пятница",
                            f"{pt1}",
                            f"{pt2}",
                        ),
                        (
                            "Суббота",
                            f"{cb1}",
                            f"{cb2}",
                        ),
                    ],
                )
                self.root.ids.md_list.add_widget(data_tables)
        elif args[0] == "Поиск по Квантомам":
            searchs.execute(f'''SELECT * FROM search WHERE kvant LIKE '%{poisk}';''')
            three_results = searchs.fetchall()
            print(three_results)
            if len(three_results) == 0:
                toast('Такого Квантома нет')
            elif poisk == "":
                toast('Ведите имя преподователя')
            else:
                fio = three_results[0][0]
                image = three_results[0][2]
                ob = three_results[0][16]
                op = three_results[0][3]
                kvan = three_results[0][1]
                pn1 = three_results[0][4]
                pn2 = three_results[0][5]
                vt1 = three_results[0][6]
                vt2 = three_results[0][7]
                cr1 = three_results[0][8]
                cr2 = three_results[0][9]
                cht1 = three_results[0][10]
                cht2 = three_results[0][11]
                pt1 = three_results[0][12]
                pt2 = three_results[0][13]
                cb1 = three_results[0][14]
                cb2 = three_results[0][15]
                fio = three_results[0][0]
                image = three_results[0][2]
                ob = three_results[0][16]
                op = three_results[0][3]
                kvan = three_results[0][1]
                pn1 = three_results[0][4]
                pn2 = three_results[0][5]
                vt1 = three_results[0][6]
                vt2 = three_results[0][7]
                cr1 = three_results[0][8]
                cr2 = three_results[0][9]
                cht1 = three_results[0][10]
                cht2 = three_results[0][11]
                pt1 = three_results[0][12]
                pt2 = three_results[0][13]
                cb1 = three_results[0][14]
                cb2 = three_results[0][15]
                self.root.ids.real.text = f"{fio}"
                self.root.ids.img.icon = f"{image}"
                # self.root.ids.ops.text = f'Основное направление:\n          {op}'
                # self.root.ids.obs.text = f'Образование: \n          {ob}'
                self.root.ids.screen_manager.current = "search-enter"
                data_tables = MDDataTable(
                    size_hint=(.9, .5),
                    pos_hint={"center_x": .5, "center_y": .5},
                    column_data=[
                        ("", dp(30)),
                        ("Гр.1", dp(25)),
                        ("Гр.2", dp(25)),
                    ],
                    row_data=[
                        # The number of elements must match the length
                        # of the `column_data` list.
                        (
                            "Понедельник",
                            f"{pn1}",
                            f"{pn2}",
                        ),
                        (
                            "Вторник",
                            f"{vt1}",
                            f"{vt2}",
                        ),
                        (
                            "Среда",
                            f"{cr1}",
                            f"{cr2}",
                        ),
                        (
                            "Четверг",
                            f"{cht1}",
                            f"{cht2}",
                        ),
                        (
                            "Пятница",
                            f"{pt1}",
                            f"{pt2}",
                        ),
                        (
                            "Суббота",
                            f"{cb1}",
                            f"{cb2}",
                        ),
                    ],
                )
                self.root.ids.real.text = f"{fio}"
                self.root.ids.img.icon = f"{image}"
                # self.root.ids.ops.text = f'Основное направление:\n          {op}'
                # self.root.ids.obs.text = f'Образование: \n          {ob}'
                self.root.ids.screen_manager.current = "search-enter"
                data_tables = MDDataTable(
                    size_hint=(.9, .5),
                    pos_hint={"center_x": .5, "center_y": .5},
                    column_data=[
                        ("", dp(30)),
                        ("Гр.1", dp(25)),
                        ("Гр.2", dp(25)),
                    ],
                    row_data=[
                        # The number of elements must match the length
                        # of the `column_data` list.
                        (
                            "Понедельник",
                            f"{pn1}",
                            f"{pn2}",
                        ),
                        (
                            "Вторник",
                            f"{vt1}",
                            f"{vt2}",
                        ),
                        (
                            "Среда",
                            f"{cr1}",
                            f"{cr2}",
                        ),
                        (
                            "Четверг",
                            f"{cht1}",
                            f"{cht2}",
                        ),
                        (
                            "Пятница",
                            f"{pt1}",
                            f"{pt2}",
                        ),
                        (
                            "Суббота",
                            f"{cb1}",
                            f"{cb2}",
                        ),
                    ],
                )
                self.root.ids.md_list.add_widget(data_tables)

    def account(self):
        db = sqlite3.connect("database.db")
        cursor = db.cursor()
        a = self.root.ids.login.text
        cursor.execute(f'''SELECT * FROM users WHERE login LIKE '%{a}%';''')
        three_results = cursor.fetchall()
        self.root.ids.nameac.text = f"{three_results[0][2]}"
        self.root.ids.ageac.text = f"Лет: {three_results[0][3]}"



КvantTask().run()
