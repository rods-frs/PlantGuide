from kivy.metrics import dp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.fitimage import FitImage
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton
from kivymd.app import MDApp
from path_resolver import RESOURCES_PATH


class WelcomeScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.md_bg_color = (0.22, 0.36, 0.25, 1)  # medium green background
        self.app = MDApp.get_running_app()

        # Main vertical container centred on screen
        main_layout = MDBoxLayout(
            orientation="vertical",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            size_hint=(None, None),
            width=dp(320),
            spacing=dp(24),
            adaptive_height=True,

        )

        # Card wrapper
        card = MDBoxLayout(
            orientation="vertical",
            padding=dp(16),
            spacing=dp(14),
            radius=[dp(16)],
            adaptive_height=True,
            size_hint_x=1,
            md_bg_color=(0.90, 0.95, 0.88, 1),  # light green card
        )

        # Welcome image
        image_widget = FitImage(
            source=str(RESOURCES_PATH / "welcome.jpg"),
            size_hint=(None, None),
            size=(dp(160), dp(160)),
            fit_mode="cover",
            pos_hint={"center_x": 0.5},
            radius=[dp(16)],
        )

        # Welcome title
        welcome_message = MDLabel(
            text="Bem-vindo",
            font_style="Display",
            role="small",
            halign="center",
            adaptive_height=True,
            theme_text_color="Custom",
            text_color=(0, 0, 0, 1),
        )

        # Subtitle
        subtitle = MDLabel(
            text="Descubra o melhor cuidado para as suas plantas.",
            font_style="Body",
            role="medium",
            halign="center",
            adaptive_height=True,
            theme_text_color="Custom",
            text_color=(0, 0, 0, 1),
        )

        card.add_widget(image_widget)
        card.add_widget(welcome_message)
        card.add_widget(subtitle)
        main_layout.add_widget(card)

        # Next button
        next_button = MDIconButton(
            icon="arrow-right",
            on_release=self.pass_screen,
            pos_hint={"center_x": 0.5},
            size_hint=(None, None),
            height=dp(56),
            width=dp(56),
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
        )
        button_box = MDBoxLayout(
            adaptive_height=True,
            size_hint_x=1,
            pos_hint={"center_x": 0.5},
        )
        button_box.add_widget(next_button)
        main_layout.add_widget(button_box)

        self.add_widget(main_layout)

    def pass_screen(self, instance):
        self.app.sm.current="plantindex"