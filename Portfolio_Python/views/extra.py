import reflex as rx
from Portfolio_Python.components.card_detail import card_detail
from Portfolio_Python.components.heading import heading
from Portfolio_Python.styles.styles import Size


def extra() -> rx.Component:
    return rx.vstack(
        heading("Extra"),
        rx.hstack(
            *[
                card_detail()
                for _ in range(0, 3)
            ],
            spacing=Size.DEFAULT.value,
            width="100%"
        ),
        spacing=Size.DEFAULT.value,
        width="100%"
    )