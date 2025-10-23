"""
-----------
Proyecto sencillo en FastAPI que modela dos entidades: Vehicle (Vehículo) y Destination (Destino).
Todos los transportes regresan siempre a Bogotá (asumido como punto de partida y llegada).


Características
---------------
- Modelos SQLAlchemy + esquemas Pydantic.
- Persistencia en SQLite (archivo: ./data/transport.db) y backups en CSV (./data/vehicles.csv y ./data/destinations.csv).
- Endpoints CRUD (Create, Read, Update, Delete) para Vehículos y Destinos.
- Endpoints para listar rutas por vehículo (incluye retorno a Bogotá).
- Archivo único ejecutable: main.py


La aplicación arrancará en http://127.0.0.1:8000
Docs interactivos: http://127.0.0.1:8000/docs


MAPA DE ENDPOINTS (resumen)
---------------------------
Vehículos
- GET /vehicles -> listar vehículos
- POST /vehicles -> crear vehículo
- GET /vehicles/{vehicle_id} -> obtener vehículo por id
- PUT /vehicles/{vehicle_id} -> actualizar vehículo
- DELETE /vehicles/{vehicle_id} -> eliminar vehículo


Destinos
- GET /destinations -> listar destinos
- POST /destinations -> crear destino (asociado a un vehículo)
- GET /destinations/{destination_id} -> obtener destino por id
- PUT /destinations/{destination_id} -> actualizar destino
- DELETE /destinations/{destination_id} -> eliminar destino


Rutas y utilidades
- GET /routes -> lista las rutas por vehículo (incluye retorno a Bogotá)
- GET /vehicles/{id}/route -> ruta para un vehículo específico


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



