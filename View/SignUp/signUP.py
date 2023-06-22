from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

Builder.load_file('SignUp/signUp.kv')

class SignUp(MDScreen):

    def build(self):
        pass

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def goLogin(self):

        self.manager.current = 'login'

    def register(self):

        self.manager.current = 'login'