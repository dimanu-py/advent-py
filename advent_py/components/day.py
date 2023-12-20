import reflex as rx
from advent_py.styles.styles import Size, Color


def day(number: int, image: str="gift.png", url: str="") -> rx.Component:
    return rx.box(
        rx.cond(
            url != "",
            rx.link(
                rx.image(
                    src=image,
                    alt=f"Regalo asociado al día {number}"
                ),
                href=url,
                is_external=True,
                position="absolute"
            )
        ),
        rx.cond(
            url == "",
            rx.image(
                src=image,
                alt=f"Regalo asociado al día {number}",
                position="absolute",
                padding=Size.SMALL.value
            ),
        ),
        rx.text(
            number,
            padding=Size.STANDARD.value,
            position="absolute",
        ),
        bg=Color.ACCENT.value,
        width="100%",
        aspect_ratio="1",
        position="relative",
    )