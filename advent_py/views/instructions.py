import reflex as rx
import advent_py.styles.styles as styles
from advent_py.components.button import button
import advent_py.constants as constants
from advent_py.styles.styles import TextColor


def instructions() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text(
                "Cómo funciona el calendario de aDEViento?",
                class_name="title",
                color=TextColor.ACCENT.value
            ),
            rx.span("Del 1 al 24 de diciembre se publicará cada día un nuevo ejercicio de Python."),
            rx.span("Si llegas tarde, puedes ver los ejercicios de los días que te has perdido, pero no podrás avanzar más rápido que el resto."),
            rx.span("Si quieres poner a prueba tu habilidad como desarrollador ánimate y participa."),
            button(
                text="Participa!",
                url=constants.WEB_URL
            ),
            class_name="nes-container is-dark with-title",
            align_items="start",
            width="100%"
        ),
        style=styles.max_width_style
    )