import reflex as rx
import advent_py.constants as constants
from advent_py.styles.styles import Size, TextColor

def github() -> rx.Component:
    return rx.link(
        rx.vstack(
            rx.vstack(
                rx.span("GitHub"),
                rx.span("Project"),
                align_items="start",
                class_name="nes-balloon from-right is-dark",
                margin_bottom=Size.BIG.value
            ),
            rx.box(
                rx.span(
                    constants.VERSION,
                    class_name="is-error"
                ),
                class_name="nes-badge",
            ),
        ),
        rx.box(
            class_name="nes-octocat animate",
        ),
        href=constants.PROJECT_URL,
        is_external=True,
        align_items="end",
        display="flex",
        margin_top=0
    )