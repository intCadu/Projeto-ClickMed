from kivy.lang import Builder
from kivymd.uix.screen import MDScreen


Builder.load_file('Home/consulta.kv')

class Consulta(MDScreen):

    def build(self):
        pass

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def goHome(self):

        self.manager.current = 'home'

    def goDiag(self):

        self.manager.current = 'diagnostico'