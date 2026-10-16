from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDButton, MDButtonText, MDButtonIcon
from kivymd.uix.label import MDLabel
from kivymd.uix.fitimage import FitImage
from kivymd.uix.widget import MDWidget
from kivymd.uix.button import MDIconButton
from kivymd.uix.card import MDCard

def card_layout(self, instance):

    self.plants = [
    {"name": "Basil",     "type": "Herb"},
    {"name": "Tomato",    "type": "Vegetable"},
    {"name": "Lavender",  "type": "Flower"},
    {"name": "Aloe Vera", "type": "Succulent"},
    ]

    card_layout=MDBoxLayout(orientation="vertical")
    for plant in self.plants:
        card1 = card_constructor(self, plant["name"],None)
        card_layout.add_widget(card1)

    return card_layout

def card_constructor(self, plant, instance):
        card=MDCard(orientation="vertical", size_hint=(None, None), size=("400px", "200px"))
        first_line_card=MDBoxLayout(orientation="horizontal")
        second_line_card=MDBoxLayout(orientation="horizontal")

        for dic_plant in self.plants:
             if dic_plant["name"] == plant:
                  found_plant = dic_plant

        first_line_card.add_widget(MDLabel(text=found_plant["name"]))
        second_line_card.add_widget(MDLabel(text=found_plant["type"]))
        card.add_widget(first_line_card)
        card.add_widget(second_line_card)
        return card