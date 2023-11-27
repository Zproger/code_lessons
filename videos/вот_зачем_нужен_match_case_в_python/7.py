
from enum import Enum, auto

class Command(Enum):
    DESTROY_SYSTEM = auto()
    SUBSCRIBE_TO_CHANNEL = auto()
    LIKE_AND_COMMENT = auto()

command = Command.LIKE_AND_COMMENT

match command:
    case Command.DESTROY_SYSTEM:
        print(f"{Command.DESTROY_SYSTEM.value=}")
    case other:
        print(f"{other=}")
