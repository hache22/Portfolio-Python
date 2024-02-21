import reflex as rx

#from Portfolio_Python.styles.styles import Size
# texto por defecto vacio 
def icon_button(icon: str,url: str , text="", solid=False) -> rx.Component:
    return rx.link(
        rx.button(
            rx.icon(icon),
            text,
            variant= "solid" if solid else "soft"
        ),
        href=url,
        is_external = True,
    )