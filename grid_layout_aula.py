from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
class MaingridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MaingridLayout, self).__init__(**kwargs)

        self.cols = 2
        self.spacing = 10
        self.padding = 30