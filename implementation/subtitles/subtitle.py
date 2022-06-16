from dataclasses import dataclass

EMPTY_SUBTITLE = ""


@dataclass
class Subtitle:
    content: str
    start: int
    end: int
