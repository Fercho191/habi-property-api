from flask import request, Blueprint, jsonify

from core.domain.property.model.PropertyFilters import PropertyFilters
from core.domain.property.use_case.FindPropertiesUseCase import FindPropertiesUseCase
from infrastructure.delivery.web.model.PropertyDTO import PropertyDTO
from infrastructure.gateway.persistence.MySQLPropertyRepository import MySQLPropertyRepository

property_bp = Blueprint('property', __name__)


@property_bp.route('/property', methods=['GET'])
def get_properties():
    # Extract Url Params
    args = request.args
    property_filters = PropertyFilters(
        year=args.get('year', None, int),
        city=args.get('city', None, str),
        state=args.get('state', None, str),
    )

    # Use Case Initialization
    find_properties_uc = FindPropertiesUseCase(MySQLPropertyRepository())

    # Use Case Execution
    result_properties = find_properties_uc.execute(property_filters)

    # Converting to DTO model (Presenter)
    properties = []
    for p in result_properties:
        properties.append(
            PropertyDTO(
                address=p.address,
                city=p.city,
                price=p.price,
                description=p.description,
                year=p.year
            )
        )

    return jsonify(properties)
