from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.fitimage import FitImage
from kivymd.uix.button import MDIconButton

class WelcomeScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.md_bg_color = self.theme_cls.backgroundColor

        self.app = MDApp.get_running_app()

        layout=MDBoxLayout(orientation="vertical")
        welcome_message=MDLabel(text="Welcome", halign="center")
        next_button=MDIconButton(icon="arrow-right", on_release=self.pass_screen, halign="center", pos_hint={"center_x": 0.5})

        layout.add_widget(welcome_message)
        layout.add_widget(next_button)
        self.add_widget(layout)

    def pass_screen(self, instance):
        self.app.sm.current="plantindex"
