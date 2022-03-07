from dataclasses import dataclass


@dataclass
class Property:
    id: int
    address: str
    city: str
    price: int
    description: str
    year: int
