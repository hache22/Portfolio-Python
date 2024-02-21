from Portfolio_Python.components.media import media
from Portfolio_Python.styles.styles import Size
import reflex as rx
from Portfolio_Python.components.heading import heading 

def header() -> rx.Component:
    return rx.hstack(
        rx.avatar(size=Size.BIG.value),
        rx.vstack(
            heading("Nombre" , True),
            heading("Habilidad principal"),
            rx.text(
                rx.icon("locate-fixed"),
                "Localizacion",
                display="inherit"
                ),
                media(),
                spacing=Size.SMALL.value,
        ),
        spacing=Size.DEFAULT.value,
    )