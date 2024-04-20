from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout

class TelaPrincipal(FloatLayout):
    pass
        
class TelaGarcom(FloatLayout):
    pass


class RestauranteApp(App):
    def build(self):
        return TelaPrincipal()
    
if __name__ == "__main__":
    RestauranteApp().run()