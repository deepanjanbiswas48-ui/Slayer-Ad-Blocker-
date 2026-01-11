from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class SlayerAdBlocker(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        title = Label(
            text='Slayer Ad Blocker',
            font_size='28sp'
        )

        status = Label(
            text='Status: Blocking Ads (Simulation)',
            font_size='18sp'
        )

        btn = Button(
            text='Stop Blocker',
            size_hint=(None, None),
            size=(200, 80),
            pos_hint={'center_x': 0.5}
        )

        layout.add_widget(title)
        layout.add_widget(status)
        layout.add_widget(btn)

        return layout

if __name__ == '__main__':
    SlayerAdBlocker().run()
