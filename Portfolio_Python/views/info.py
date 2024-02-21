import reflex as rx

from Portfolio_Python.components.heading import heading
from Portfolio_Python.components.info_detail import info_detail
from Portfolio_Python.styles.styles import Size


def info(title: str) -> rx.Component:
    return rx.vstack(
        heading(title),
        info_detail(),
        spacing=Size.DEFAULT.value,
        width="100%"
    )