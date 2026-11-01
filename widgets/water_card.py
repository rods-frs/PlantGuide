from kivy.metrics import dp
from kivy.properties import NumericProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon


# ---------- helpers ----------

WATER_METHOD_LABELS = {
    "por_cima": "Por cima da terra",
    "por_baixo": "Por baixo (no pratinho)",
    "encharcar_secar": "Encharcar e deixar secar",
}


def days_to_water_level(days):
    # 1 day between waterings -> 10 (thirsty), 14+ days -> 1 (very little water)
    level = round(10 - (days - 1) * 9 / 13)
    return max(1, min(10, level))


class WaterBar(MDBoxLayout):
    """10 blocks; the first `level` blocks are filled."""
    level = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "horizontal"
        self.spacing = dp(4)
        self.size_hint_y = None
        self.height = dp(14)
        self._blocks = []
        for _ in range(10):
            block = MDBoxLayout(radius=[dp(4)])
            self._blocks.append(block)
            self.add_widget(block)
        self.on_level(self, self.level)

    def on_level(self, instance, value):
        if not hasattr(self, "_blocks"):  # fires once during super().__init__
            return
        filled = (0.13, 0.59, 0.95, 1)
        empty = (0.5, 0.5, 0.5, 0.25)
        for i, block in enumerate(self._blocks):
            block.md_bg_color = filled if i < int(value) else empty


def _title_row(icon, text):
    row = MDBoxLayout(orientation="horizontal", spacing=dp(8),
                      adaptive_height=True)
    row.add_widget(MDIcon(icon=icon, pos_hint={"center_y": 0.5}))
    row.add_widget(MDLabel(text=text, font_style="Title", role="small",
                           adaptive_height=True, pos_hint={"center_y": 0.5}))
    return row


def _bar_section(icon, title, days_text, level):
    section = MDBoxLayout(orientation="vertical", spacing=dp(6),
                          adaptive_height=True)
    section.add_widget(_title_row(icon, title))
    section.add_widget(WaterBar(level=level))
    section.add_widget(MDLabel(text=f"{days_text}  •  {level}/10",
                               adaptive_height=True))
    return section


# ---------- the function you asked for ----------

def build_water_card(water_every_days, water_every_days_winter,
                     water_method, water_amount):
    card = MDBoxLayout(
        orientation="vertical",
        padding=dp(16),
        spacing=dp(14),
        radius=[dp(16)],
        adaptive_height=True,
        size_hint_x=1,
        md_bg_color=MDApp.get_running_app().theme_cls.surfaceContainerLowColor,
    )

    # Header
    card.add_widget(_title_row("water", "Detalhes de rega"))

    # Normal season
    card.add_widget(_bar_section(
        "weather-sunny", "Época normal",
        f"A cada {water_every_days} dias",
        days_to_water_level(water_every_days),
    ))

    # Winter (None -> same as normal)
    if water_every_days_winter is None:
        winter_days, winter_text = water_every_days, "Igual à época normal"
    else:
        winter_days = water_every_days_winter
        winter_text = f"A cada {water_every_days_winter} dias"
    card.add_widget(_bar_section(
        "snowflake", "Inverno", winter_text, days_to_water_level(winter_days),
    ))

    # Method
    method_box = MDBoxLayout(orientation="vertical", spacing=dp(4),
                             adaptive_height=True)
    method_box.add_widget(_title_row("watering-can", "Como regar"))
    method_box.add_widget(MDLabel(
        text=WATER_METHOD_LABELS.get(water_method, str(water_method)),
        adaptive_height=True))
    card.add_widget(method_box)

    # Amount
    amount_box = MDBoxLayout(orientation="vertical", spacing=dp(4),
                             adaptive_height=True)
    amount_box.add_widget(_title_row("cup-water", "Quantidade"))
    amount_box.add_widget(MDLabel(text=water_amount, adaptive_height=True))
    card.add_widget(amount_box)

    return card