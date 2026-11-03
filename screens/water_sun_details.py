"""Water and sun details screen — shows watering and sunlight info cards for a plant."""

from database.database_func import water_query, sun_query
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
from widgets.water_card import build_water_card
from widgets.sun_card import build_sun_card
from kivymd.uix.scrollview import ScrollView


class WaterDetail(MDScreen):
    """Displays water and sun care cards for the selected plant."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.md_bg_color = (0.22, 0.36, 0.25, 1)  # medium green background
        self.main_layout = MDBoxLayout(orientation="vertical")

    def on_pre_enter(self, *args):
        """Called before the screen becomes visible — queries and displays water/sun data."""
        self.main_layout.clear_widgets()
        self.remove_widget(self.main_layout)
        # Back button to return to plant detail screen
        self.main_layout.add_widget(MDIconButton(icon="arrow-left",on_release=self.go_back,pos_hint={"x": 0.02, "top": 0.98},theme_text_color="Custom",text_color=(1, 1, 1, 1)))
        self.selected_plant = self.get_selected_plant()\

        # Query water data and build the water card
        data = water_query(self.selected_plant)
        data = data[0]
        water_days = data["water_every_days"]
        water_winter_days = data["water_every_days_winter"]
        water_method = data["water_method"]
        water_amount = data["water_amount"]
        water_card = build_water_card(water_days, water_winter_days, water_method, water_amount)

        # Query sun data and build the sun card
        data = sun_query(self.selected_plant)
        data = data[0]
        light_level = data["light_level"]
        best_sun_time = data["best_sun_time"]
        direct_sun_hours = data["direct_sun_hours"]
        sun_notes = data["sun_notes"]
        sun_card = build_sun_card(light_level, direct_sun_hours, best_sun_time, sun_notes)

        # Wrap both cards in a scrollable layout
        view = ScrollView()
        data_layout = MDBoxLayout(orientation="vertical", size_hint_y=None, adaptive_height=True)
        data_layout.add_widget(water_card)
        data_layout.add_widget(sun_card)
        view.add_widget(data_layout)
        self.main_layout.add_widget((view))
        self.add_widget(self.main_layout)

    def get_selected_plant(self):
        """Retrieve the currently selected plant from the app state."""
        self.app = MDApp.get_running_app()
        self.selected_plant = self.app.selected_plant
        print(self.selected_plant)
        return self.selected_plant

    def go_back(self, instance):
        """Navigate back to the plant detail screen."""
        self.app = MDApp.get_running_app()
        self.app.sm.current = "plantdetail"

