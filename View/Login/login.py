from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

Builder.load_file('Login\login.kv')

class Login(MDScreen):

    def build(self):
        pass

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def goRegister(self):

        self.manager.current = 'signUp'

    def newPassword(self):

        self.manager.current = 'password'

    def login(self):

        self.manager.current = 'home'