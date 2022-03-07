from core.domain.property.gateway.PropertyGateway import PropertyGateway
from core.domain.property.model.Property import Property
from core.domain.property.model.PropertyFilters import PropertyFilters
from core.domain.property.use_case.FindPropertiesUseCase import FindPropertiesUseCase


def test_find_properties_use_case():
    find_properties_uc = FindPropertiesUseCase(MockedPropertyGateway())
    filters = PropertyFilters(year=2000, city="bogotá", state="en_venta")
    result = find_properties_uc.execute(filters)
    assert result[0].year == 2000
    assert result[0].city == "bogotá"
    assert result[0].description == "description"
    assert len(result) == 1


class MockedPropertyGateway(PropertyGateway):
    def find_properties(self, year: int = None, city: str = None, state: str = None) -> list[Property]:
        return [
            Property(id=1, address="address", city=city, price=10, description="description", year=year),
            Property(id=1, address="", city=city, price=10, description="description", year=year),
            Property(id=1, address="address", city=city, price=0, description="description", year=year)
        ]
