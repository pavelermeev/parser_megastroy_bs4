from dataclasses import dataclass


@dataclass
class Good:
    id: str
    name: str
    price: int
    link: str
