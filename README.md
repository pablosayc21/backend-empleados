# backend-empleados
Código fuente del backend para aplicación de gestión de empleados.

![Python]
![Flask]
![Sqlite]
![Conda]

## Guia de instalación

* Crear un ambiente de desarrollo de python con los requerimientos encontrados [Acá](https://github.com/pablosayc21/backend-empleados/blob/main/requirements.txt).
  * [Recurso](https://datumorphism.leima.is/til/programming/python/python-anaconda-install-requirements/) para este paso usando Conda.
* Clonar [este](https://github.com/pablosayc21/backend-empleados.git) repositorio.
* Colocarse en la rama main.
* Si el archivo [empleados_departamentos.db](https://github.com/pablosayc21/backend-empleados/blob/main/empleados_departamentos.db) no se encuentra o pierde, ejecute el archivo [creacion_bd.py](https://github.com/pablosayc21/backend-empleados/blob/main/creacion_bd.py) para crear un nuevo archivo con las tablas necesarias para el funcionamiento de la aplicación.

## Guia de ejecución 

* python [app.py](https://github.com/pablosayc21/backend-empleados/blob/main/app.py) para ejecutar la aplicación.
* Puede conectarse al API con el puerto 5000.

## Endpoints

### Departamentos

<details>
  <summary><code>GET</code> <code><b>/api/departamentos</b></code> <code>(obtiene todos los departamentos)</code></summary>

##### Parameters

> None

##### Responses

> | http code     | content-type                      | response                                                            |
> |---------------|-----------------------------------|---------------------------------------------------------------------|
> | `200`         | `application/json`                | Lista de departamentos en formato JSON                              |
> | `400`         | `application/json`                | `{"message": "Error interno del servidor: <detalle del error>"}`     |

##### Example cURL

> ```bash
>  curl -X GET http://localhost:5000/api/departamentos
> ```

</details>

<details>
  <summary><code>POST</code> <code><b>/api/departamentos</b></code> <code>(agrega un nuevo departamento)</code></summary>

##### Parameters

> | name          |  type      | data type      | description                                    |
> |---------------|------------|----------------|------------------------------------------------|
> | `nombre`      |  required  | string         | El nombre del nuevo departamento               |

##### Responses

> | http code     | content-type                      | response                                                            |
> |---------------|-----------------------------------|---------------------------------------------------------------------|
> | `201`         | `application/json`                | `{"message": "Departamento agregado"}`                              |
> | `400`         | `application/json`                | `{"message": "El contenido del request no es JSON"}`                |
> | `400`         | `application/json`                | `{"message": "Todos los campos son obligatorios: nombre de departamento"}` |
> | `400`         | `application/json`                | `{"message": "Error interno del servidor: <detalle del error>"}`     |

##### Example cURL

> ```bash
>  curl -X POST -H "Content-Type: application/json" -d '{"nombre": "Finanzas"}' http://localhost:5000/api/departamentos
> ```

</details>

### Empleados

<details>
  <summary><code>GET</code> <code><b>/api/empleados</b></code> <code>(obtiene todos los empleados)</code></summary>

##### Parameters

> None

##### Responses

> | http code     | content-type                      | response                                                            |
> |---------------|-----------------------------------|---------------------------------------------------------------------|
> | `200`         | `application/json`                | Lista de empleados en formato JSON                                  |
> | `400`         | `application/json`                | `{"message": "Error interno del servidor: <detalle del error>"}`     |

##### Example cURL

> ```bash
>  curl -X GET http://localhost:5000/api/empleados
> ```

</details>

<details>
  <summary><code>POST</code> <code><b>/api/empleados</b></code> <code>(agrega un nuevo empleado)</code></summary>

##### Parameters

> | name                  |  type      | data type      | description                                    |
> |-----------------------|------------|----------------|------------------------------------------------|
> | `nombre`              |  required  | string         | El nombre del empleado                         |
> | `apellido`            |  required  | string         | El apellido del empleado                       |
> | `departamento_id`     |  required  | int            | El ID del departamento al que pertenece el empleado |
> | `fecha_contratacion`  |  required  | string         | La fecha de contratación del empleado (yyyy-mm-dd) |
> | `cargo`               |  required  | string         | El cargo del empleado                          |

##### Responses

> | http code     | content-type                      | response                                                            |
> |---------------|-----------------------------------|---------------------------------------------------------------------|
> | `201`         | `application/json`                | `{"message": "Empleado agregado"}`                                  |
> | `400`         | `application/json`                | `{"message": "El contenido del request no es JSON"}`                |
> | `400`         | `application/json`                | `{"message": "Todos los campos son obligatorios: nombre, apellido, departamento_id, fecha_contratacion, cargo"}` |
> | `404`         | `application/json`                | `{"message": "El departamento_id especificado no existe."}`          |
> | `400`         | `application/json`                | `{"message": "Error interno del servidor: <detalle del error>"}`     |

##### Example cURL

> ```bash
>  curl -X POST -H "Content-Type: application/json" -d '{"nombre": "Juan", "apellido": "Pérez", "departamento_id": 1, "fecha_contratacion": "2023-09-25", "cargo": "Analista"}' http://localhost:5000/api/empleados
> ```

</details>

<details>
  <summary><code>PUT</code> <code><b>/api/empleados/<id></b></code> <code>(actualiza la información de un empleado)</code></summary>

##### Parameters

> | name                  |  type      | data type      | description                                    |
> |-----------------------|------------|----------------|------------------------------------------------|
> | `id`                  |  required  | int            | El ID del empleado a actualizar                |
> | `nombre`              |  required  | string         | El nuevo nombre del empleado                   |
> | `apellido`            |  required  | string         | El nuevo apellido del empleado                 |
> | `departamento_id`     |  required  | int            | El nuevo ID del departamento                   |
> | `fecha_contratacion`  |  required  | string         | La nueva fecha de contratación del empleado    |
> | `cargo`               |  required  | string         | El nuevo cargo del empleado                    |

##### Responses

> | http code     | content-type                      | response                                                            |
> |---------------|-----------------------------------|---------------------------------------------------------------------|
> | `200`         | `application/json`                | `{"message": "Empleado actualizado"}`                               |
> | `400`         | `application/json`                | `{"message": "El contenido del request no es JSON"}`                |
> | `400`         | `application/json`                | `{"message": "Todos los campos son obligatorios: nombre, apellido, departamento_id, fecha_contratacion, cargo"}` |
> | `404`         | `application/json`                | `{"message": "Empleado no encontrado."}`                            |
> | `404`         | `application/json`                | `{"message": "El departamento_id especificado no existe."}`          |
> | `400`         | `application/json`                | `{"message": "Error interno del servidor: <detalle del error>"}`     |

##### Example cURL

> ```bash
>  curl -X PUT -H "Content-Type: application/json" -d '{"nombre": "Juan", "apellido": "Pérez", "departamento_id": 2, "fecha_contratacion": "2023-09-25", "cargo": "Gerente"}' http://localhost:5000/api/empleados/1
> ```

</details>

<details>
  <summary><code>DELETE</code> <code><b>/api/empleados/<id></b></code> <code>(elimina un empleado)</code></summary>

##### Parameters

> | name   |  type      | data type      | description                                          |
> |--------|------------|----------------|------------------------------------------------------|
> | `id`   |  required  | int            | El ID del empleado a eliminar                        |

##### Responses

> | http code     | content-type                      | response                                                            |
> |---------------|-----------------------------------|---------------------------------------------------------------------|
> | `200`         | `application/json`                | `{"message": "Empleado eliminado."}`                                |
> | `404`         | `application/json`                | `{"message": "Empleado no encontrado."}`                            |
> | `400`         | `application/json`                | `{"message": "Error interno del servidor: <detalle del error>"}`     |

##### Example cURL

> ```bash
>  curl -X DELETE http://localhost:5000/api/empleados/1
> ```

</details>

## Autores
* [Pablo Say](https://github.com/pablosayc21)
* [Pablo Say - cuenta universitaria](https://github.com/pablosay)

## Contacto

[Instagram](https://www.instagram.com/pablosc_21/) 

[LinkedIn](https://www.linkedin.com/in/PabloSay21/)

## Reconocimientos: 

L Ma (2019). 'Installing requirements.txt in Conda Environments', Datumorphism, 03 April. Available at: https://datumorphism.leima.is/til/programming/python/python-anaconda-install-requirements/.

[Python]:https://img.shields.io/badge/Python-gray?logo=python
[Flask]:https://img.shields.io/badge/flask-gray?logo=flask
[Sqlite]:https://img.shields.io/badge/sqlite-gray?logo=sqlite
[Conda]:https://img.shields.io/badge/anaconda-gray?logo=anaconda

