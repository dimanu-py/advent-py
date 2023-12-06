import reflex as rx
from advent_py.styles.styles import Size, TextColor
import advent_py.styles.styles as styles
import advent_py.constants as constants


def footer() -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.text(
                "Calendario de aDEViento 2023",
                font_size=Size.MEDIUM.value,
                margin_bottom=Size.SMALL.value,
            ),
            rx.link(
                "Creado siguiendo el tutorial de MoureDev ",
                rx.box(
                    class_name="nes-icon is-small heart"
                ),
                font_size=Size.MEDIUM.value,
                color=TextColor.TERTIARY.value,
                href=constants.ORIGINAL_PROJECT_URL,
                is_external=True
            ),
            align_items="start",
            spacing=Size.SMALL.value,
        ),
        rx.spacer(),
        rx.image(
            src="logo.png",
            alt="Logo de MourDev. Una letra \"eme\" entre dos corchetes",
            class_name="nes-avatar is-large"
        ),
        style=styles.max_width_style,
        padding_bottom=Size.BIG.value,
        align_items="center"
    )