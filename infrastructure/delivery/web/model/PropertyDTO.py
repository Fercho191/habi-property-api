from dataclasses import dataclass


@dataclass
class PropertyDTO:
    address: str
    city: str
    price: int
    description: str
    year: int
