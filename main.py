from fastapi import FastAPI, HTTPException, Depends
from sqlmodel import Session, select
from typing import List

from models import Vehiculo, Destino
from db import create_db_and_tables, get_session

app = FastAPI(title="Catalogo de Rutas de Transporte", version="1.0")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.post("/vehiculos/", response_model=Vehiculo)
def crear_vehiculo(vehiculo: Vehiculo, session: Session = Depends(get_session)):
    session.add(vehiculo)
    session.commit()
    session.refresh(vehiculo)
    return vehiculo

@app.get("/vehiculos/", response_model=List[Vehiculo])
def listar_vehiculos(session: Session = Depends(get_session)):
    vehiculos = session.exec(select(Vehiculo)).all()
    return vehiculos

@app.get("/vehiculos/{vehiculo_id}", response_model=Vehiculo)
def obtener_vehiculo(vehiculo_id: int, session: Session = Depends(get_session)):
    vehiculo = session.get(Vehiculo, vehiculo_id)
    if not vehiculo:
        raise HTTPException(status_code=404, detail="Vehículo no encontrado")
    return vehiculo

@app.delete("/vehiculos/{vehiculo_id}")
def eliminar_vehiculo(vehiculo_id: int, session: Session = Depends(get_session)):
    vehiculo = session.get(Vehiculo, vehiculo_id)
    if not vehiculo:
        raise HTTPException(status_code=404, detail="Vehículo no encontrado")
    session.delete(vehiculo)
    session.commit()
    return {"mensaje": "Vehículo eliminado correctamente"}

@app.post("/destinos/", response_model=Destino)
def crear_destino(destino: Destino, session: Session = Depends(get_session)):
    session.add(destino)
    session.commit()
    session.refresh(destino)
    return destino

@app.get("/destinos/", response_model=List[Destino])
def listar_destinos(session: Session = Depends(get_session)):
    destinos = session.exec(select(Destino)).all()
    return destinos

@app.get("/destinos/{destino_id}", response_model=Destino)
def obtener_destino(destino_id: int, session: Session = Depends(get_session)):
    destino = session.get(Destino, destino_id)
    if not destino:
        raise HTTPException(status_code=404, detail="Destino no encontrado")
    return destino

@app.delete("/destinos/{destino_id}")
def eliminar_destino(destino_id: int, session: Session = Depends(get_session)):
    destino = session.get(Destino, destino_id)
    if not destino:
        raise HTTPException(status_code=404, detail="Destino no encontrado")
    session.delete(destino)
    session.commit()
    return {"mensaje": "Destino eliminado correctamente"}

@app.get("/rutas/")
def listar_rutas(session: Session = Depends(get_session)):
    vehiculos = session.exec(select(Vehiculo)).all()
    destinos = session.exec(select(Destino)).all()

    rutas = []
    for v in vehiculos:
        for d in destinos:
            if d.vehiculo_id == v.id:
                rutas.append({
                    "vehiculo": v.placa,
                    "modelo": v.modelo,
                    "origen": "Bogotá",
                    "destino": d.nombre,
                    "distancia_km": d.km_from_bogota
                })
    return rutas
