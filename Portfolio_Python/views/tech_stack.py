import reflex as rx
from Portfolio_Python.components.heading import heading
from Portfolio_Python.styles.styles import Size


def tech_stack() -> rx.Component:
    return rx.vstack(
        heading("Tecnologías"),
        rx.flex(
            *[
                rx.badge(
                    rx.icon("code"),
                    rx.text(f"Stack{index}"),
                    size="2"
                )
                for index in range(0, 10)
            ],
            wrap="wrap",
            spacing=Size.SMALL.value
        ),
        spacing=Size.DEFAULT.value
    )