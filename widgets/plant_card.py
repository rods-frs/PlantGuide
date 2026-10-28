from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDButton, MDButtonText, MDButtonIcon
from kivymd.uix.label import MDLabel
from kivymd.uix.fitimage import FitImage
from kivymd.uix.widget import MDWidget
from kivymd.uix.button import MDIconButton
from kivymd.uix.card import MDCard
from database.database_func import card_query
from path_resolver import RESOURCES_PATH

def card_layout(self, instance):

    self.plants = card_query()

    card_layout=MDBoxLayout(orientation="vertical", size_hint_y=None, adaptive_height=True)
    for plant in self.plants:
        card1 = card_constructor(self, plant["name"], plant["search_name"], None)
        card_layout.add_widget(card1)

    return card_layout

def card_constructor(self, plant, search_name, instance):
        card=MDCard(
             orientation="horizontal", 
             size_hint=(None, None), 
             size=("400dp", "200dp"), 
             on_release=lambda instance: change_to_details_screen(self, plant_name, instance),
             style="outlined",
             padding="12dp",
             radius=[24,24,24,24],
             theme_bg_color="Custom",
             md_bg_color="#F1F5E9",
             theme_line_color="Custom",
             line_color="#A3B18A"

             )
        
        text_layout=MDBoxLayout(orientation="vertical")
        first_line_card=MDBoxLayout(orientation="horizontal")
        second_line_card=MDBoxLayout(orientation="horizontal")

        image_widget=FitImage(
             source=str(RESOURCES_PATH / "card" / f"{search_name}.jpg"),
             size_hint=(None, None),
             size=("160dp", "160dp"),
             fit_mode="cover"
             )

        for dic_plant in self.plants:
             if dic_plant["name"] == plant:
                  found_plant = dic_plant

        plant_name = found_plant["name"]

        first_line_card.add_widget(MDLabel(text=f"Plant name: {found_plant["name"]}"))
        second_line_card.add_widget(MDLabel(text=f"Plant type: {found_plant["type"]}"))
        text_layout.add_widget(first_line_card)
        text_layout.add_widget(second_line_card)
        card.add_widget(image_widget)
        card.add_widget(text_layout)
        return card

def change_to_details_screen(self, plant_name, instance):
     self.app = MDApp.get_running_app()
     self.app.selected_plant=plant_name
     print(self.app.selected_plant)
     self.app.sm.current="plantdetail"
