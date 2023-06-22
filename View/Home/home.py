from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.chip import MDChip
from kivy.animation import Animation

Builder.load_file('Home/home.kv')

class Home(MDScreen):

    def build(self):
        pass

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def goLogin(self):
        
        self.manager.current = 'login'

    def goHome(self):

        self.manager.current = 'home'

    def goProfile(self):

        self.manager.current = 'perfil'

    def goConsulta(self):

        self.manager.current = 'consulta'

            

        
            












  
    