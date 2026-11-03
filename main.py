"""Main entry point for the PlantGuide app."""

from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from screens.plant_index import PlantIndex
from screens.welcome_screen import WelcomeScreen
from database.database_func import start_db
from screens.plant_detail import PlantDetail
from screens.water_sun_details import WaterDetail
from screens.recipes import Recipes
from pathlib import Path

class JosehApp(MDApp):
    """Main application class that sets up screens and the database."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Tracks which plant the user selected, shared across screens
        self.selected_plant = None

    def build(self):
        # Initialize the SQLite database in the app's data directory
        app = MDApp.get_running_app()
        db_path = Path(app.user_data_dir) / "plants.db"
        start_db(db_path)

        # Create the screen manager and register all screens
        self.sm = MDScreenManager()
        self.sm.add_widget(WelcomeScreen(name="welcome"))
        self.sm.add_widget(PlantIndex(name="plantindex"))
        self.sm.add_widget(PlantDetail(name="plantdetail"))
        self.sm.add_widget(WaterDetail(name="water_detail"))
        self.sm.add_widget(Recipes(name="recipes"))
        return self.sm

# Launch the app
JosehApp().run()