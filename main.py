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
from screens.plant_index import PlantIndex
from screens.welcome_screen import WelcomeScreen
from database.database_func import start_db
from screens.plant_detail import PlantDetail
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
        return self.sm

JosehApp().run()