from kivy.metrics import dp
from kivy.properties import NumericProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

from widgets.water_card import _title_row  # reuse the same title row


# ---------- helpers ----------

LIGHT_LEVEL_LABELS = {
    "sol_pleno": "Sol pleno",
    "luz_indireta": "Luz indireta",
    "meia_sombra": "Meia-sombra",
    "sombra": "Sombra",
}

LIGHT_LEVEL_ICONS = {
    "sol_pleno": "white-balance-sunny",
    "luz_indireta": "weather-partly-cloudy",
    "meia_sombra": "weather-cloudy",
    "sombra": "weather-night",
}

BEST_SUN_TIME_LABELS = {
    "manha": "Sol da manhã",
    "tarde": "Sol da tarde",
    "dia_todo": "O dia todo",
    "nenhum": "Não precisa de sol direto",
}


def hours_to_sun_level(hours):
    # 0-1 hours -> 1 (little sun), 8+ hours -> 10 (full sun)
    level = round(hours * 10 / 8)
    return max(1, min(10, level))


class SunBar(MDBoxLayout):
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
        filled = (0.20, 0.60, 0.35, 1)    # green
        empty = (0.5, 0.5, 0.5, 0.25)
        for i, block in enumerate(self._blocks):
            block.md_bg_color = filled if i < int(value) else empty


def _sun_bar_section(icon, title, hours_text, level):
    section = MDBoxLayout(orientation="vertical", spacing=dp(6),
                          adaptive_height=True)
    section.add_widget(_title_row(icon, title))
    section.add_widget(SunBar(level=level))
    section.add_widget(MDLabel(text=f"{hours_text}  •  {level}/10",
                               adaptive_height=True,
                               theme_text_color="Custom", text_color=(0, 0, 0, 1)))
    return section


def _text_section(icon, title, text):
    box = MDBoxLayout(orientation="vertical", spacing=dp(4),
                      adaptive_height=True)
    box.add_widget(_title_row(icon, title))
    box.add_widget(MDLabel(text=text, adaptive_height=True,
                            theme_text_color="Custom", text_color=(0, 0, 0, 1)))
    return box


# ---------- the function ----------

def build_sun_card(light_level, direct_sun_hours, best_sun_time, sun_notes):
    """
    Arguments:
        light_level       (str)       "sol_pleno" | "luz_indireta" | "meia_sombra" | "sombra"
        direct_sun_hours  (int)       hours of direct sun per day
        best_sun_time     (str)       "manha" | "tarde" | "dia_todo" | "nenhum"
        sun_notes         (str|None)  free text; None or empty hides the section

    Returns:
        MDBoxLayout card, ready for add_widget(...)
    """
    card = MDBoxLayout(
        orientation="vertical",
        padding=dp(16),
        spacing=dp(14),
        radius=[dp(16)],
        adaptive_height=True,
        size_hint_x=1,
        md_bg_color=(0.90, 0.95, 0.88, 1),  # light green card
    )

    # Header
    card.add_widget(_title_row("white-balance-sunny", "Detalhes de sol"))

    # Light level
    card.add_widget(_text_section(
        LIGHT_LEVEL_ICONS.get(light_level, "white-balance-sunny"),
        "Tipo de luz",
        LIGHT_LEVEL_LABELS.get(light_level, str(light_level)),
    ))

    # Hours of direct sun (bar)
    card.add_widget(_sun_bar_section(
        "clock-outline", "Sol direto por dia",
        f"{direct_sun_hours} horas",
        hours_to_sun_level(direct_sun_hours),
    ))

    # Best time
    card.add_widget(_text_section(
        "weather-sunset", "Melhor horário",
        BEST_SUN_TIME_LABELS.get(best_sun_time, str(best_sun_time)),
    ))

    # Notes (only if there is something to show)
    if sun_notes:
        card.add_widget(_text_section("note-text-outline", "Observações", sun_notes))

    return card