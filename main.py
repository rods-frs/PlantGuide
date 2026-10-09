from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDButton, MDButtonText, MDButtonIcon
from kivymd.uix.label import MDLabel
from kivymd.uix.fitimage import FitImage
from kivymd.uix.widget import MDWidget
from kivymd.uix.button import MDIconButton

class MainScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.md_bg_color = self.theme_cls.backgroundColor

        layout1 = MDBoxLayout(
            FitImage(
                source=r"C:\Users\rodrigo.fsilva61\Downloads\cu.jpg",
                size_hint=(None, None),
                size=("200dp", "200dp"),
                fit_mode="scale-down",
                pos_hint={"center_x":0.5}),
            MDLabel(text="Bem-Vindo", font_style="Display", role="large", halign="center"),
            MDIconButton(icon="arrow-right", style="standard", pos_hint={"x": 0.5}),
            MDWidget(),
            orientation="vertical"
            )
        self.add_widget(layout1)

    def go_next(self, *args):   # *args: Kivy passes the button in, Textual didn't
        self.manager.current = "second"                 # your push_screen

class SecondScreen(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.md_bg_color = self.theme_cls.backgroundColor
        layout = MDBoxLayout(
            MDLabel(text="Test screen", font_style="Display", role="large", halign="center", adaptive_height=True),
            FitImage(
                source=r"C:\Users\rodrigo.fsilva61\Downloads\cu.jpg",
                size_hint=(None, None),
                size=("200dp", "200dp"),
                height="200dp",          # give it a height or it takes an equal share
                fit_mode="scale-down",        # cover | contain | fill | scale-down
                radius=("12dp", "12dp", 2, 2),   # rounded top corners
                pos_hint={"center_x":0.5},
            ),
            MDBoxLayout(
                MDButton(MDButtonText(text="Botão teste 1")),
                MDButton(MDButtonText(text="Bye")),
                orientation="horizontal",
                adaptive_size=False,                                 # 2: shrink to fit the buttons
                pos_hint={"center_x": 0.5},                         # 2: center_x, not right
            ),
            orientation="vertical"
        )
        self.add_widget(layout)

    def go_back(self, *args):
        self.manager.current = "main"

class JosehApp(MDApp):
    def build(self):                                    # replaces on_mount + push_screen
        sm = MDScreenManager()
        sm.add_widget(MainScreen(name="main"))
        sm.add_widget(SecondScreen(name="second"))
        return sm

JosehApp().run()