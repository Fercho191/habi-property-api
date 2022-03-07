from jinjasql import JinjaSql

from core.domain.property.model.Property import Property
from core.domain.property.gateway.PropertyGateway import PropertyGateway
from infrastructure.configuration.MySQLConfig import connect


class MySQLPropertyRepository(PropertyGateway):
    def find_properties(self, year: int = None, city: str = None, state: str = None) -> list[Property]:
        j = JinjaSql()
        template = get_query_template()
        template_data = {
            "default_states": ["pre_venta", "en_venta", "vendido"],
            "year": year,
            "city": city,
            "state": state
        }
        query, bind_params = j.prepare_query(template, template_data)

        mydb = connect()
        cursor = mydb.cursor()
        cursor.execute(query, bind_params)
        result = cursor.fetchall()

        result_properties = []
        for (id, address, city, price, description, year) in result:
            result_properties.append(
                Property(
                    id=id,
                    address=address,
                    city=city,
                    price=price,
                    description=description,
                    year=year
                )
            )

        return result_properties


def get_query_template():
    return """
        SELECT p.*
        FROM property p 
        JOIN (
            SELECT MAX(sh.id) max_id, sh.property_id
            FROM status_history sh
            GROUP BY property_id
        ) sh_max ON sh_max.property_id = p.id
        JOIN status_history sh ON (sh.id = sh_max.max_id)
        JOIN status s ON (s.id = sh.status_id)
        {% if state %}
            WHERE s.name = {{ state }}
        {% else %}
            WHERE s.name in {{ default_states  | inclause }}
        {% endif %}
        {% if year %}
            AND p.year = {{ year }}
        {% endif %}
        {% if city %}
            AND p.city = {{ city }}
        {% endif %}
        ORDER BY p.id asc
    """
