import os
os.environ['KIVY_GL_BACKEND']='angle_sdl2'

from kivy.lang import Builder
from kivymd.app import MDApp


from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window

Window.size = (350, 580)



class MeuApp(MDApp):
    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file('teste.kv'))
        self.title='Dashboard'
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Red"
        return screen_manager

MeuApp().run()