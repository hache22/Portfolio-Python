
from Portfolio_Python.styles.styles import MAX_WIDTH, EmSize, Size
from Portfolio_Python.views.about import about
from Portfolio_Python.views.extra import extra
from Portfolio_Python.views.footer import footer
from Portfolio_Python.views.header import header
from Portfolio_Python.views.info import info
from Portfolio_Python.views.tech_stack import tech_stack
from rxconfig import config

import reflex as rx

def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            header(),
            about(),
            rx.divider(),
            tech_stack(),
            info("Experiencia"),
            info("Proyectos"),
            info("Formación"),
            extra(),
            rx.divider(),
            footer(),
            spacing = Size.MEDIUM.value,
            padding_y =EmSize.BIG.value,
            max_width=MAX_WIDTH # tamaño maximo de la pantalla
        )
    )


app = rx.App()
app.add_page(index)
