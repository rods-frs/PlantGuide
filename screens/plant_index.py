from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.scrollview import ScrollView
from widgets.plant_card import card_layout as CL
from kivymd.uix.label import MDLabel
from kivy.metrics import dp

class PlantIndex(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selected_plant=None
        self.md_bg_color = self.theme_cls.backgroundColor

        view=ScrollView()
        main_layout=MDBoxLayout(orientation="vertical")
        top_bar = self.build_title_bar()

        card_layout=CL(self, None)

        view.add_widget(card_layout)
        main_layout.add_widget(top_bar)   # fixed at the top
        main_layout.add_widget(view)      # scrolls below it
        self.add_widget(main_layout)      # only one child on the screen now

    def build_title_bar(self, text="Coracao de Trevo"):
        bar = MDBoxLayout(
            orientation="horizontal",
            adaptive_height=True,
            size_hint_x=1,
            padding=[dp(16), dp(16), dp(16), dp(8)],
        )
        bar.add_widget(MDLabel(
            text=str(text),
            font_style="Headline",
            role="small",
            halign="center",
            adaptive_height=True,
            pos_hint={"center_y": 0.5},
        ))
        return bar