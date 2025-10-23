CATALOGO DE TRANSPORTE
-----------
Proyecto sencillo en FastAPI que modela dos entidades: Vehicle (Vehículo) y Destination (Destino).
Todos los transportes regresan siempre a Bogotá (asumido como punto de partida y llegada).


Características
---------------
- Endpoints CRUD (Create, Read, Update, Delete) para Vehículos, Destinos y Rutas.
- Endpoints para listar rutas por vehículo (incluye retorno a Bogotá).
- Archivo único ejecutable: main.py


La aplicación arrancará en http://127.0.0.1:8000
Docs interactivos: http://127.0.0.1:8000/docs


MAPA DE ENDPOINTS (resumen)
---------------------------
Vehículos
- GET /Vehiculo -> listar vehículos
- POST /vehiculo -> crear vehículo
- GET /vehiculo/{vehiculo_id} -> obtener vehículo por id
- PUT /vehiculo/{vehiculo_id} -> actualizar vehículo
- DELETE /vehiculo/{vehiculo_id} -> eliminar vehículo


Destinos
- GET /destino -> listar destinos
- POST /destino -> crear destino (asociado a un vehículo)
- GET /destino/{destino_id} -> obtener destino por id
- PUT /destino/{destino_id} -> actualizar destino
- DELETE /destino/{destino_id} -> eliminar destino


Rutas 
- GET/rutas -> Listar rutas
- POST/rutas -> Crear ruta
- GET/rutas -> obtener ruta
- PUT/rutas -> actualizar ruta
- DELETE/rutas-> eliminar ruta 


Diseño de modelos 
--------------------------------
Vehiculo:
- id: int (PK)
- plate: str (único)
- model: str
- capacity: int
- active: bool


Destino:
- id: int (PK)
- name: str (ciudad o parada)
- order: int (orden en la ruta)
- vehicle_id: int (FK -> vehicles.id)
- km_from_bogota: float (kilómetros aproximados desde Bogotá)

Rutas:
- id
- nombre: str
- fecha_salida: datetime 
- fecha_retorno: datetime 
- vehiculo_id





