from kivymd.uix.screen import MDScreen
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.fitimage import FitImage
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton
from kivymd.app import MDApp
from path_resolver import RESOURCES_PATH


class WelcomeScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.md_bg_color = self.theme_cls.backgroundColor
        self.app = MDApp.get_running_app()

        layout=MDFloatLayout()

        image_widget=FitImage(
            source=str(RESOURCES_PATH / "welcome.jpg"),
            size_hint=(None, None),
            size=("160dp", "160dp"),
            fit_mode="cover",
            pos_hint={"center_x": 0.5, "top":0.6}
        )        
        welcome_message=MDLabel(
            text="Welcome", 
            pos_hint={"center_x": 0.5, "top":0.95}, 
            size_hint=(None, None),
            font_style="Display",
            role="small",
            text_size=(None, None),
            adaptive_size=True
            )

        next_button=MDIconButton(icon="arrow-right", on_release=self.pass_screen, pos_hint={"center_x": 0.5, "top": 0.10})

        layout.add_widget(welcome_message)
        layout.add_widget(image_widget)
        layout.add_widget(next_button)
        self.add_widget(layout)

    def pass_screen(self, instance):
        self.app.sm.current="plantindex"