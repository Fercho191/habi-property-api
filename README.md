# Servicio de consulta
## Tecnologias a Utilizar
- Flask: Se usará para levantar la API Rest de forma sencilla, además con el podemos apoyarnos en sus modulos y comenzar el proyecto con un lienzo en blanco, logrando así un mayor control de las dependencias a utilizar.
- Mysql-Connector: Con mysq-connector nos podremos conectar e interactuar con la Base de datos proporcionada

## Enfoque de arquirectura
Se trabajará en lo posible bajo Clean Architecture con el fin de:
- Procurar tener un codigo lo mas limpio posible
- Proponer un servicio escalable en el tiempo independientemente de las tecnologías que le rodeen (Bases de datos, Frameworks, etc)
- Hacer clases y metodos puros con el fin de testearlos de forma mas sencilla

## Dudas y respuestas:
¿Como puedo implementar el servicio sin utilizar un framework que no permita demostrar capacidades de desarrollo y buenas practicas de python?
- Al usar Clean Architecture, separamos las bondades que un framework pueda dar de la lógica de negocio. Esta logica de negocio se implementa en el "core" del servicio, utilizando python vanila. Todo detalle de interfaces REST y conecciones a BD, se hará en una capa superior llamada "infrastructure"

# Servicio de "Me Gusta"
Analizando la Base de Datos actual, es posible extender el modelo de forma sencilla con solo una tabla relacional que incluya ForeignKeys de la tabla Property y de AuthUser, agregando una columna de tipo dateTime para poder tener el detalle historico de los likes de un usuario


``` sql

CREATE TABLE `like` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `property_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `created_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `like_id_uindex` (`id`),
  KEY `like_property_id_fk` (`property_id`),
  KEY `like_user_id_fk` (`user_id`),
  CONSTRAINT `like_property_id_fk` FOREIGN KEY (`property_id`) REFERENCES `property` (`id`),
  CONSTRAINT `like_user_id_fk` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) 

```

Con esta tabla es posible consultar:
- Dato un usuario, sus likes sobre los inmuebles
- Dado un inmueble, sus likes de usuarios

Dependiendo de la necesidad de negocio, se pueden hacer cambios adicionales.
- Si es importante que un usuario pueda ver de forma sencilla todos los inmuebles a los que le dá like, este model es suficiente
- Si es importante hacer el ranking interno y las consultas sobre "cantidad de likes" en inmuebles son muchas, podriamos evitar hacer un "COUNT" sobre esta tabla por  cada consulta y apostar por una redundancia, agregando una columna a la tabla "property" llamada "like_count", donde por casa insert sobre la tabla like, este valor aumentaría en uno, con ello, la consulta sería inmediata.
