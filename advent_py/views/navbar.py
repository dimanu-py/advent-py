import reflex as rx
from advent_py.styles.styles import Size, Color
from advent_py.components.link_icon import link_icon
import advent_py.constants as constants


def navbar() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.image(
                src="dimanu-py.png",
                alt="Imagen pixel art de MoureDev con estilo navideño",
                width=Size.STANDARD.value,
                height=Size.STANDARD.value
            ),
            rx.text("aDEViento", size=2),
            rx.spacer(),
            link_icon(
                "github",
                constants.GITHUB_URL
            ),
            link_icon(
                "linkedin",
                constants.LINKEDIN_URL
            ),
            width="100%"
        ),
        position="sticky",
        bg=Color.PRIMARY.value,
        border_bottom=f"0.25em solid {Color.SECONDARY.value}",
        padding_x=Size.BIG.value,
        padding_y=Size.STANDARD.value,
        z_index="999",
        top="0",
        width="100%"
    )