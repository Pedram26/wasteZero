from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
from kivy.lang import Builder

import os

Builder.load_string("""
<MyWidget>:
    id: my_widget
    Button
        text: "open"
        on_release: my_widget.open(filechooser.path, filechooser.selection)
    FileChooserListView:
        id: filechooser
        on_selection: my_widget.selected(filechooser.selection)
""")


class MyWidget(BoxLayout):
    def open(self, path, filename):
        with open(os.path.join(path, filename[0]), 'r+') as f:
            print(f.read())

    def selected(self, filename):
        print("selected: %s" % filename[0])


class RootWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.add_widget(Button(text='Upload an Image'))
        cb = CustomBtn()
        cb.bind(pressed=self.btn_pressed)
        self.add_widget(cb)

    def btn_pressed(self, instance, pos):
        print ('pos: printed from root widget: {pos}'.format(pos=pos))


class CustomBtn(Widget):
    pressed = ListProperty([0, 0])

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.pressed = touch.pos
            return True
        return super(CustomBtn, self).on_touch_down(touch)

    def on_pressed(self, instance, pos):
        print ('pressed at {pos}'.format(pos=pos))


class TestApp(App):

    def build(self):
        return MyWidget()


if __name__ == '__main__':
    TestApp().run()
