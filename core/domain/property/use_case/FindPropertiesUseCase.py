from core.domain.property.model.Property import Property
from core.domain.property.model.PropertyFilters import PropertyFilters
from core.domain.property.gateway.PropertyGateway import PropertyGateway
from core.shared.UseCase import UseCase


class FindPropertiesUseCase(UseCase):

    def __init__(self, property_repository: PropertyGateway):
        self.property_repository = property_repository

    def execute(self, property_filters: PropertyFilters) -> list[Property]:
        properties = self.property_repository.find_properties(
            year=property_filters.year,
            city=property_filters.city,
            state=property_filters.state
        )
        return list(
            filter(lambda p: p.address and p.city and p.price != 0 and p.year, properties)
        )
