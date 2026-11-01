from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from screens.plant_index import PlantIndex
from screens.welcome_screen import WelcomeScreen
from database.database_func import start_db
from screens.plant_detail import PlantDetail
from screens.water_sun_details import WaterDetail
from pathlib import Path

class JosehApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selected_plant = None

    def build(self): 
        app = MDApp.get_running_app()
        db_path = Path(app.user_data_dir) / "plants.db"
        start_db(db_path)                                
        self.sm = MDScreenManager()
        self.sm.add_widget(WelcomeScreen(name="welcome"))
        self.sm.add_widget(PlantIndex(name="plantindex"))
        self.sm.add_widget(PlantDetail(name="plantdetail"))
        self.sm.add_widget(WaterDetail(name="water_detail"))
        return self.sm

JosehApp().run()