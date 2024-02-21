from Portfolio_Python.components.media import media
from Portfolio_Python.styles.styles import Size
import reflex as rx


def footer() -> rx.Component:
    return rx.vstack(
        rx.divider(),
        rx.text("nombre"),
        media(),
        spacing=Size.SMALL.value
    )