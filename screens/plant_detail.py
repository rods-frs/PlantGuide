from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.fitimage import FitImage
from kivymd.uix.button import MDIconButton
from kivymd.uix.card import MDCard
from database.database_func import detail_query
from path_resolver import RESOURCES_PATH


class PlantDetail(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.md_bg_color = self.theme_cls.backgroundColor

        main_layout = MDFloatLayout()

        # Arrow: top left
        go_back_button = MDIconButton(
            icon="arrow-left",
            on_release=self.go_back,
            pos_hint={"x": 0.02, "top": 0.98},
        )

        # Cards: center left, stacked in a column that sizes itself to its children
        self.plant_name_widget = self.make_nature_card()
        self.plant_type_widget = self.make_nature_card()
        self.plant_water_widget = self.make_nature_card()
        self.plant_size_widget = self.make_nature_card()

        info_layout = MDBoxLayout(
            orientation="vertical",
            adaptive_size=True,
            spacing="12dp",
            pos_hint={"x": 0.03, "center_y": 0.5},
        )
        info_layout.add_widget(self.plant_name_widget)
        info_layout.add_widget(self.plant_type_widget)
        info_layout.add_widget(self.plant_water_widget)
        info_layout.add_widget(self.plant_size_widget)

        # Image: center right
        self.image_widget = FitImage(
            size_hint=(None, None),
            size=("160dp", "160dp"),
            fit_mode="cover",
            pos_hint={"right": 0.97, "center_y": 0.5},
        )

        main_layout.add_widget(go_back_button)
        main_layout.add_widget(info_layout)
        main_layout.add_widget(self.image_widget)
        self.add_widget(main_layout)

    def on_pre_enter(self, *args):
        self.selected_plant = self.get_selected_plant()
        data = detail_query(self.selected_plant)
        data = data[0]
        self.selected_plant = None

        self.image_widget.source=str(RESOURCES_PATH / "detail" / data['search_name']) + ".jpg"
        self.plant_name_widget.label.text = f"Plant name: {data['name']}"
        self.plant_type_widget.label.text = f"Type: {data['type']}"
        self.plant_water_widget.label.text = f"Water quantity per day: {data['water']}"
        self.plant_size_widget.label.text = f"Size: {data['size']}"

    def get_selected_plant(self):
        self.app = MDApp.get_running_app()
        self.selected_plant = self.app.selected_plant
        print(self.selected_plant)
        return self.selected_plant

    def go_back(self, instance):
        self.app = MDApp.get_running_app()
        self.app.sm.current = "plantindex"

    def make_nature_card(self):
        card = MDCard(
            style="outlined",
            theme_bg_color="Custom",
            md_bg_color="#DAE5C8",
            theme_line_color="Custom",
            line_color="#A3B18A",
            line_width=1.2,
            radius=[24, 24, 24, 24],
            size_hint=(None, None),
            size=("200dp", "75dp"),
            padding="12dp",
        )

        label = MDLabel(
            text="",
            halign="center",
            theme_text_color="Custom",
            text_color="#344E41",
        )

        card.add_widget(label)
        card.label = label
        return card