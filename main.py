from fastapi import FastAPI, HTTPException, Depends
from sqlmodel import Session, select
from typing import List

from models import Vehiculo, Destino, Ruta
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

@app.put("/vehiculos/{vehiculo_id}", response_model=Vehiculo)
def actualizar_vehiculo(vehiculo_id: int, vehiculo_actualizado: Vehiculo, session: Session = Depends(get_session)):
    vehiculo = session.get(Vehiculo, vehiculo_id)
    if not vehiculo:
        raise HTTPException(status_code=404, detail="Vehículo no encontrado")
    vehiculo.placa = vehiculo_actualizado.placa
    vehiculo.modelo = vehiculo_actualizado.modelo
    vehiculo.capacidad = vehiculo_actualizado.capacidad
    vehiculo.active = vehiculo_actualizado.active
    session.commit()
    session.refresh(vehiculo)
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

@app.put("/destinos/{destino_id}", response_model=Destino)
def actualizar_destino(destino_id: int, destino_actualizado: Destino, session: Session = Depends(get_session)):
    destino = session.get(Destino, destino_id)
    if not destino:
        raise HTTPException(status_code=404, detail="Destino no encontrado")
    destino.nombre = destino_actualizado.nombre
    destino.orden = destino_actualizado.orden
    destino.km_from_bogota = destino_actualizado.km_from_bogota
    destino.vehiculo_id = destino_actualizado.vehiculo_id
    session.commit()
    session.refresh(destino)
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


@app.post("/rutas/", response_model=Ruta)
def crear_ruta(ruta: Ruta, session: Session = Depends(get_session)):
    session.add(ruta)
    session.commit()
    session.refresh(ruta)
    return ruta

@app.get("/rutas/", response_model=List[Ruta])
def listar_rutas(session: Session = Depends(get_session)):
    return session.exec(select(Ruta)).all()

@app.get("/rutas/{ruta_id}", response_model=Ruta)
def obtener_ruta(ruta_id: int, session: Session = Depends(get_session)):
    ruta = session.get(Ruta, ruta_id)
    if not ruta:
        raise HTTPException(status_code=404, detail="Ruta no encontrada")
    return ruta

@app.put("/rutas/{ruta_id}", response_model=Ruta)
def actualizar_ruta(ruta_id: int, ruta_actualizada: Ruta, session: Session = Depends(get_session)):
    ruta = session.get(Ruta, ruta_id)
    if not ruta:
        raise HTTPException(status_code=404, detail="Ruta no encontrada")
    ruta.nombre = ruta_actualizada.nombre
    ruta.fecha_salida = ruta_actualizada.fecha_salida
    ruta.fecha_retorno = ruta_actualizada.fecha_retorno
    ruta.vehiculo_id = ruta_actualizada.vehiculo_id
    session.commit()
    session.refresh(ruta)
    return ruta

@app.delete("/rutas/{ruta_id}")
def eliminar_ruta(ruta_id: int, session: Session = Depends(get_session)):
    ruta = session.get(Ruta, ruta_id)
    if not ruta:
        raise HTTPException(status_code=404, detail="Ruta no encontrada")
    session.delete(ruta)
    session.commit()
    return {"mensaje": "Ruta eliminada correctamente"}
