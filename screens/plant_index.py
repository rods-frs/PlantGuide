from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDButton, MDButtonText, MDButtonIcon
from kivymd.uix.label import MDLabel
from kivymd.uix.fitimage import FitImage
from kivymd.uix.widget import MDWidget
from kivymd.uix.button import MDIconButton
from kivymd.uix.card import MDCard
from kivymd.uix.scrollview import ScrollView
from widgets.plant_card import card_layout as CL

class PlantIndex(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selected_plant=None
        self.md_bg_color = self.theme_cls.backgroundColor

        view=ScrollView()
        main_layout=MDBoxLayout(orientation="vertical")

        card_layout=CL(self, None)

        view.add_widget(card_layout)
        self.add_widget(main_layout)
        self.add_widget(view)
