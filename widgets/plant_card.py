from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.fitimage import FitImage
from kivymd.uix.card import MDCard
from database.database_func import card_query
from path_resolver import RESOURCES_PATH


def card_layout(self, instance):
    self.plants = card_query()

    card_layout = MDBoxLayout(orientation="vertical", size_hint_y=None, adaptive_height=True,
                              padding=dp(16), spacing=dp(14))
    for plant in self.plants:
        card1 = card_constructor(self, plant["name"], plant["search_name"], None)
        card_layout.add_widget(card1)

    return card_layout


def _info_row(icon, text):
    # Icon + Title/small label, same pattern as the water card's title rows
    row = MDBoxLayout(orientation="horizontal", spacing=dp(8), adaptive_height=True)
    row.add_widget(MDIcon(icon=icon, pos_hint={"center_y": 0.5}))
    row.add_widget(MDLabel(text=text, font_style="Title", role="small",
                           adaptive_height=True, pos_hint={"center_y": 0.5}))
    return row


def card_constructor(self, plant, search_name, instance):
    card = MDCard(
        orientation="horizontal",
        size_hint=(1, None),
        height=dp(132),
        on_release=lambda instance: change_to_details_screen(self, plant_search_name, instance),
        style="filled",
        padding=dp(16),
        spacing=dp(14),
        radius=[dp(16)],
        theme_bg_color="Custom",
        md_bg_color=MDApp.get_running_app().theme_cls.surfaceContainerLowColor,

    )

    text_layout = MDBoxLayout(orientation="vertical", spacing=dp(8),
                              adaptive_height=True, pos_hint={"center_y": 0.5})

    image_widget = FitImage(
        source=str(RESOURCES_PATH / "card" / f"{search_name}.jpg"),
        size_hint=(None, None),
        size=(dp(100), dp(100)),
        fit_mode="cover",
        radius=[dp(12)],
        pos_hint={"center_y": 0.5}
    )

    for dic_plant in self.plants:
        if dic_plant["search_name"] == search_name:
            found_plant = dic_plant

    plant_name = found_plant["name"]
    plant_search_name = found_plant["search_name"]

    text_layout.add_widget(_info_row("sprout", f"Plant name: {found_plant["name"]}"))
    text_layout.add_widget(_info_row("shape-outline", f"Plant type: {found_plant["type"]}"))
    card.add_widget(image_widget)
    card.add_widget(text_layout)
    card.add_widget(MDIcon(icon="chevron-right", pos_hint={"center_y": 0.5}))
    return card


def change_to_details_screen(self, plant_name, instance):
    self.app = MDApp.get_running_app()
    self.app.selected_plant = plant_name
    print(self.app.selected_plant)
    self.app.sm.current = "plantdetail"