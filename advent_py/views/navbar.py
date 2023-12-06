import reflex as rx
from advent_py.styles.styles import Size

def navbar() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.image(
                src="mouredev.png",
                alt="Imagen pixel art de MoureDev con estilo navideño",
                width=Size.STANDARD.value,
                height=Size.STANDARD.value
            ),
            rx.text("aDEViento", size=2),
            rx.spacer(),
            width="100%"
        )
    )