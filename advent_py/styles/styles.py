from enum import Enum

import reflex as rx
from .fonts import Font
from .colors import TextColor, Color


MAX_WIDTH = "1000px"

STYLESHEETS = [
    "https://unpkg.com/nes.css@latest/css/nes.min.css",
    "https://fonts.googleapis.com/css?family=Press+Start+2P&display=swap"
]

class Size(Enum):
    STANDARD = "1em"
    MEDIUM = "0.8em"
    SMALL = "0.5em"
    BIG = "2em"


BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "color": TextColor.PRIMARY.value,
    "background": Color.PRIMARY.value,
    rx.Link: {
        "text_decoration": "none",
        "_hover": {
            "text_decoration": "none",
            "color": TextColor.ACCENT.value,
        }
    },
    rx.Heading: {
        "color": TextColor.ACCENT.value,
        "font_family": Font.DEFAULT.value,
    },
    rx.Span: {
        "font_size": Size.MEDIUM.value,
    },
}

max_width_style = dict(
    align_items = "start",
    padding_x = Size.BIG.value,
    width = "100%",
    max_width = MAX_WIDTH,
)
