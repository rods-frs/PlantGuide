from kivy.metrics import dp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.fitimage import FitImage
from path_resolver import RESOURCES_PATH
from widgets.water_card import _title_row  # reuse the same title row


# ---------- helpers ----------

def _format_prep_time(prep_time):
    # accepts an int (minutes) or a ready-made string ("1h 30min")
    if isinstance(prep_time, (int, float)):
        return f"{int(prep_time)} min"
    return str(prep_time)


def _text_section(icon, title, text):
    box = MDBoxLayout(orientation="vertical", spacing=dp(4),
                      adaptive_height=True)
    box.add_widget(_title_row(icon, title))
    box.add_widget(MDLabel(text=text, adaptive_height=True,
                            theme_text_color="Custom", text_color=(0, 0, 0, 1)))
    return box


def _step_row(number, text):
    theme = MDApp.get_running_app().theme_cls

    row = MDBoxLayout(orientation="horizontal", spacing=dp(12),
                      adaptive_height=True)

    # numbered circle badge
    badge = MDBoxLayout(
        size_hint=(None, None),
        size=(dp(26), dp(26)),
        radius=[dp(13)],
        md_bg_color=(0.20, 0.60, 0.35, 1),  # green
        pos_hint={"top": 1},
    )
    badge.add_widget(MDLabel(
        text=str(number),
        halign="center",
        valign="middle",
        bold=True,
        theme_text_color="Custom",
        text_color=(0, 0, 0, 1),  # black on green
    ))

    row.add_widget(badge)
    row.add_widget(MDLabel(text=text, adaptive_height=True, size_hint_x=1,
                            theme_text_color="Custom", text_color=(0, 0, 0, 1)))
    return row


def _steps_section(steps):
    section = MDBoxLayout(orientation="vertical", spacing=dp(10),
                          adaptive_height=True)
    section.add_widget(_title_row("format-list-numbered", "Modo de preparo"))
    for i, step in enumerate(steps, start=1):
        section.add_widget(_step_row(i, step))
    return section


# ---------- the function ----------

def build_recipe_card(search_name, recipe_name, main_ingredient, prep_time,
                      step1, step2, step3):
    """
    Arguments:
        recipe_name      (str)        recipe title
        main_ingredient  (str)        main ingredient (e.g. the plant part used)
        prep_time        (int|str)    minutes (int) or free text ("1h 30min")
        step1..step3     (str|None)   preparation steps; None/empty are skipped

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

    image_widget = FitImage(
        source=str(RESOURCES_PATH / "recipe" / f"{search_name}.jpg"),
        size_hint=(None, None),
        size=(dp(213), dp(213)),
        fit_mode="cover",
        pos_hint={"center_x": 0.5},
        radius = [dp(36), dp(36), dp(36), dp(36)]
    )

    #image
    card.add_widget(image_widget)

    # Header
    card.add_widget(_title_row("chef-hat", recipe_name))

    # Main ingredient
    card.add_widget(_text_section(
        "food-apple-outline", "Ingrediente principal", main_ingredient,
    ))

    # Prep time
    card.add_widget(_text_section(
        "clock-outline", "Tempo de preparo", _format_prep_time(prep_time),
    ))

    # Steps (only the ones that have text)
    steps = [s for s in (step1, step2, step3) if s]
    if steps:
        card.add_widget(_steps_section(steps))

    return card