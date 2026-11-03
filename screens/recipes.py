"""Recipes screen — shows a recipe card for the selected plant."""

from database.database_func import recipe_query
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.scrollview import ScrollView
from widgets.recipe_card import build_recipe_card

class Recipes(MDScreen):
    """Displays the recipe card for the selected plant."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.md_bg_color = (0.22, 0.36, 0.25, 1)  # medium green background
        self.main_layout = MDBoxLayout(orientation="vertical")

    def on_pre_enter(self, *args):
        """Called before the screen becomes visible — queries and displays recipe data."""
        self.main_layout.clear_widgets()
        self.remove_widget(self.main_layout)
        # Back button to return to plant detail screen
        self.main_layout.add_widget(MDIconButton(icon="arrow-left",on_release=self.go_back,pos_hint={"x": 0.02, "top": 0.98},theme_text_color="Custom",text_color=(1, 1, 1, 1)))
        self.selected_plant = self.get_selected_plant()

        # Query recipe data and build the recipe card
        data = recipe_query(self.selected_plant)
        data = data[0]
        search_name = data["search_name"]
        recipe_name = data["recipe_name"]
        main_ingredient = data["main_ingredient"]
        prep_time = data["prep_time"]
        step1 = data["step_1"]
        step2 = data["step_2"]
        step3 = data["step_3"]
        main_card = build_recipe_card(search_name, recipe_name, main_ingredient, prep_time, step1, step2, step3)

        # Wrap the card in a scrollable layout
        view = ScrollView()
        data_layout = MDBoxLayout(orientation="vertical", size_hint_y=None, adaptive_height=True)
        data_layout.add_widget(main_card)
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
