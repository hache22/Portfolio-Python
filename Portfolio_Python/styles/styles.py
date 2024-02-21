from enum import Enum

# enumerado del tipo de tamaños que se van a ir trabajando

MAX_WIDTH = "900px"
IMAGE_HEIGHT = "200px"

class EmSize(Enum):
    DEFAULT = "1em" #16px
    MEDIUM = "2em" #32px
    BIG = "4em" #64px


class Size(Enum):
    ZERO = "0"
    SMALL = "2" #8px
    DEFAULT = "4" #16px
    MEDIUM = "6" #32px
    BIG = "8" #48px
