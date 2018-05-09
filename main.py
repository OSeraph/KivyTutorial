import kivy

kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.widget import Widget


class PongGame(Widget):
    pass


class MyApp(App):

    def build(self):
        return PongGame()


if __name__ == '__main__':
    MyApp().run()
