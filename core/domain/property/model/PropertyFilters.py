from dataclasses import dataclass

from core.shared.UseCaseRequest import UseCaseRequest


@dataclass
class PropertyFilters(UseCaseRequest):
    year: int
    city: str
    state: str
