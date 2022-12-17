from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivymd.uix.widget import MDWidget
from kivy.core.text import LabelBase
from kivymd.uix.datatables import MDDataTable
from kivy.properties import StringProperty
from kivy.config import Config
from kivy.metrics import dp
from kivy.uix.button import Button
import pymongo
from pymongo import MongoClient
from kivy.animation import Animation

CLIENT = MongoClient("mongodb://localhost:27017")
Config.set("kivy", "keyboard_mode", "systemanddock")
Window.size = (310, 500)


class Main(MDScreen):
    pass


class Men(MDScreen):
    pass


class MyLayout(MDWidget):
    def spinner_clicked(self, value):
        self.ids.click_label.text = f"You select {value}"


class Admin(MDScreen):
    pass

class Table(MDScreen):
    screen= MDScreen()
    table=MDDataTable
    screen.add_widget(table)
    

class Adminhelp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(1, 20):
            size = dp(100)
            b = Button(text=f"{i}", size_hint=(None, None), size=(size, size))
            self.add_widget(b)


class Login(MDScreen):
    invalid_message = StringProperty("")

    def login(self):
        email = self.ids.email_data.text
        password = self.ids.password_data.text
        user = CLIENT["aviskar"]["users_data"].find_one(
            {"email": email, "password": password}
        )
        if user == None:
            self.invalid_message = "Invalid username or password."
            print("Invalid username or password.")
        else:
            self.invalid_message = ""
            print(user)


class Signup(MDScreen):
    already_exist_message = StringProperty("")

    def sign_up(self):
        data = {
            "username": self.ids.user_name_data.text,
            "email": self.ids.email_data.text,
            "password": self.ids.password_data.text,
            "privilege": "user",
        }
        if (
            CLIENT["aviskar"]["users_data"].find_one({"username": data["username"]})
            != None
        ):
            print("User of this name already exists.")
            self.already_exist_message = "User of this name already exists."
        else:
            CLIENT["aviskar"]["users_data"].insert_one(data)
            self.already_exist_message = ""
            print(data)


class ScreenManage(MDScreenManager):
    pass


class MainApp(MDApp):
    pass


if __name__ == "__main__":
    LabelBase.register(name="Lato", fn_regular="Lato/Lato-Regular.ttf")
    LabelBase.register(name="Lato", fn_regular="Lato/Lato-Bold.ttf")

    MainApp().run()
