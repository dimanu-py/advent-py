import reflex as rx

import advent_py.styles.styles as styles
from advent_py.styles.styles import Size
from advent_py.components.header_text import header_text
from advent_py.components.day import day


def calendar() -> rx.Component:
    return rx.vstack(
        header_text(
            icon="heart",
            text="DEVcember Calendar"
        ),
        rx.vstack(
            rx.hstack(
                rx.text("The event will start in: "),
                rx.text(id="countdown"),
                align_items="start"
                ),
            ),
            rx.responsive_grid(
                rx.foreach(
                    list(range(1, 25)), lambda day_number: day(day_number),
                ),
                columns=[3, 3, 4, 5, 6],
                width="100%",
                spacing=Size.STANDARD.value,
                padding_top=Size.BIG.value
            ),
            rx.script(
                src="/js/countdown.js"
        ),
        style=styles.max_width_style
    )