from abc import ABC, abstractmethod

from core.domain.property.model.Property import Property


class PropertyGateway(ABC):

    @abstractmethod
    def find_properties(self, year: int = None, city: str = None, state: str = None) -> list[Property]:
        pass
