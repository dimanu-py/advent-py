import reflex as rx
import advent_py.styles.styles as styles
from advent_py.styles.styles import Size
from advent_py.views import navbar, header, footer, instructions, calendar
from advent_py.components import github



"""
Reflex funciona de forma que si quiero definir una página tengo que crear una función que devuelva un componente.

No vamos a crear backend, no hay estado, por lo que tendremos una página estática
"""
def index() -> rx.Component:
    return rx.box(
        rx.script(
            src="document.documentElement.lang = 'en'"
        ),
        rx.script(
            src="/js/snow.js"
        ),
        navbar.navbar(),
        rx.center(
            rx.vstack(
                header.header(),
                instructions.instructions(),
                calendar.calendar(),
                footer.footer(),
                github.github(),
                width="100%",
                spacing=Size.BIG.value
            )
        ),
    )


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)

app.add_page(
    index,
    title="Calendario de aDEViento 2023 | 24 días. 24 retos. 24 premios.",
    description="Un calendario de adviento para desarrolladores python"
)

app.compile()