import reflex as rx


"""
Reflex funciona de forma que si quiero definir una página tengo que crear una función que devuelva un componente.

No vamos a crear backend, no hay estado, por lo que tendremos una página estática
"""
def index() -> rx.Component:
    return rx.box(

    )


app = rx.App(

)

app.add_page(
    index,
    title="Calendario de aDEViento 2023 | 24 días. 24 retos. 24 premios.",
    description="Un calendario de adviento para desarrolladores python"
)

app.compile()