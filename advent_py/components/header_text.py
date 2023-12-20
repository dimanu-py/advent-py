import reflex as rx
from advent_py.styles.styles import Size, TextColor


def header_text(icon: str, text: str, dark: bool=True) -> rx.Component:
    return rx.hstack(
        rx.box(
            class_name=f"nes-icon is-medium {icon}"
        ),
        rx.heading(
            text,
            size="md",
            color=TextColor.ACCENT.value if dark else TextColor.SECONDARY.value
        ),
        spacing=Size.STANDARD.value,
        padding_bottom=Size.BIG.value
    )