import reflex as rx
from advent_py.styles.styles import Size, TextColor
import advent_py.styles.styles as styles
import advent_py.constants as constants


def header() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Calendario de aDEViento 2023",
            size="lg",
            padding_bottom=Size.STANDARD.value
        ),
        rx.flex(
            rx.image(
                src="mouredev.png",
                alt="Imagen pixel art de MoureDev con estilo navideño",
                width="16em",
                height="16em",
                margin_right=Size.BIG.value
            ),
            rx.vstack(
                rx.box(
                    rx.text("24 días. 24 retos."),
                    rx.text("Del 1 al 24 de diciembre."),
                    class_name="nes-balloon from-left is-dark",
                ),
                rx.span(
                    "Por tercer año consecutivo, MoureDev presenta el calendario de aDEViento. Un calendario de adviento para ",
                    rx.span(
                        "desarrolladores python",
                        color=TextColor.ACCENT.value,
                        weight="bold",
                        font_size=Size.STANDARD.value,
                    ),
                ),
                rx.span(
                    "Su finalidad es ayudar a compartir conocimiento y a aprender de forma divertida.",
                ),
                rx.span(
                    "Cada día se publicará un nuevo reto en el ",
                    rx.link(
                        "repositorio de GitHub",
                        href=constants.PROJECT_URL,
                        is_external=True,
                    ),
                ),
                align_items="start"
            ),
            flex_direction=["column", "column", "column", "row", "row"],
        ),
        padding_top=Size.BIG.value,
        style=styles.max_width_style,
    )