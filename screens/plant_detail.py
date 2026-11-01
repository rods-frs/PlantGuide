from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.fitimage import FitImage
from kivymd.uix.button import MDIconButton
from kivymd.uix.card import MDCard
from database.database_func import detail_query
from path_resolver import RESOURCES_PATH


class PlantDetail(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.md_bg_color = self.theme_cls.backgroundColor

        root = MDBoxLayout(orientation="vertical")

        # Top bar: back arrow
        top_bar = MDBoxLayout(
            orientation="horizontal",
            adaptive_height=True,
            padding=[dp(8), dp(8), dp(8), 0],
        )
        go_back_button = MDIconButton(
            icon="arrow-left",
            on_release=self.go_back,
        )
        top_bar.add_widget(go_back_button)

        # Image: rounded, full width, same radius as the water cards
        self.image_widget = FitImage(
            size_hint=(1, None),
            height=dp(200),
            fit_mode="scale-down",
            radius=[dp(16)],
        )

        # Cards (same attribute names as before)
        self.plant_name_widget = self.make_detail_card("sprout")
        self.plant_type_widget = self.make_detail_card("shape-outline")
        self.plant_water_widget = self.make_detail_card("water", chevron=True)
        self.plant_water_widget.bind(on_release=self.water_screen_change)
        self.plant_size_widget = self.make_detail_card("ruler")

        # Scrollable column, full width, same padding/spacing as the water card
        content = MDBoxLayout(
            orientation="vertical",
            adaptive_height=True,
            padding=dp(16),
            spacing=dp(14),
        )
        content.add_widget(self.image_widget)
        content.add_widget(self.plant_name_widget)
        content.add_widget(self.plant_type_widget)
        content.add_widget(self.plant_water_widget)
        content.add_widget(self.plant_size_widget)

        scroll = MDScrollView(do_scroll_x=False)
        scroll.add_widget(content)

        root.add_widget(top_bar)
        root.add_widget(scroll)
        self.add_widget(root)

    def on_pre_enter(self, *args):
        self.selected_plant = self.get_selected_plant()
        data = detail_query(self.selected_plant)
        data = data[0]

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

    def water_screen_change(self, instance):
        self.app = MDApp.get_running_app()
        self.app.sm.current = "water_detail"

    def make_detail_card(self, icon="information-outline", chevron=False):
        # Same look as the water card: surfaceContainerLow, radius 16, padding 16
        card = MDCard(
            style="filled",
            theme_bg_color="Custom",
            md_bg_color=MDApp.get_running_app().theme_cls.surfaceContainerLowColor,
            orientation="horizontal",
            radius=[dp(16)],
            padding=dp(16),
            spacing=dp(14),
            size_hint=(1, None),
            height=dp(75),  # non-zero start size: MDCard builds a ripple FBO at init
        )

        card.add_widget(MDIcon(icon=icon, pos_hint={"center_y": 0.5}))

        label = MDLabel(
            text="",
            font_style="Title",
            role="small",
            adaptive_height=True,
            pos_hint={"center_y": 0.5},
        )
        card.add_widget(label)

        if chevron:
            card.add_widget(MDIcon(icon="chevron-right",
                                   pos_hint={"center_y": 0.5}))

        # Grow with the content only after construction (replaces adaptive_height)
        card.bind(minimum_height=card.setter("height"))

        card.label = label
        return card