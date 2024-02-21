import reflex as rx
from Portfolio_Python.components.heading import heading


def about() -> rx.Component:
    return rx.vstack(
        heading("Sobre mí"),
        rx.text("Descripción")
    )