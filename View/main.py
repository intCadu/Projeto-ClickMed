import os
os.environ['KIVY_GL_BACKEND']='angle_sdl2'
from kivy.core.window import Window
from kivy.core.window import WindowBase

# Importando as classes
from Login.login import Login
from Password.password import Password
from SignUp.signUP import SignUp
from Home.home import Home
from Home.consulta import Consulta

# Importando os componentes
from kivy.app import App
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.behaviors.focus_behavior import FocusBehavior
from kivymd.uix.screenmanager import ScreenManager

# Criando a aplicação

class MainApp(MDApp, App):

    Window.size = (800, 600)
    #WindowBase.fullscreen = 'auto'

    def build(self):

        sm = ScreenManager()
        sm.add_widget(Login(name = 'login'))
        sm.add_widget(SignUp(name = 'signUp'))
        sm.add_widget(Password(name = 'password'))
        sm.add_widget(Home(name = 'home'))
        sm.add_widget(Consulta(name = 'consulta'))
        self.title = 'Click Med'
        self.icon = 'Images/logo.png'
        self.theme_cls.primary_palette = 'LightBlue'
        self.theme_cls.accent_palette = 'Cyan'
        self.theme_cls.primary_hue = '700'
        self.theme_cls.theme_style = "Light"

        return sm
    
    
class ButtonFocus(MDRaisedButton,FocusBehavior):
    pass


if __name__ == "__main__":

    mainApp = MainApp()
    mainApp.run()