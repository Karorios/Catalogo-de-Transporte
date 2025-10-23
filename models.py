from typing import Optional
from sqlmodel import SQLModel, Field, Relationship

class Vehiculo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    placa: str = Field(index=True)
    modelo: str
    capacidad: int
    active: bool = Field(default=True)

    destinos: list["Destino"] = Relationship(back_populates="vehiculo")


class Destino(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    orden: int
    km_from_bogota: float

    vehiculo_id: Optional[int] = Field(default=None, foreign_key="vehiculo.id")
    vehiculo: Optional[Vehiculo] = Relationship(back_populates="destinos")
