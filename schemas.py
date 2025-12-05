from pydantic import BaseModel
from typing import Optional
from datetime import date
from utils.positions import Position
from utils.states import States

class JugadorBase(BaseModel):
    nombre: str
    numero_camiseta: int
    fecha_nacimiento: Optional[date] = None
    edad: Optional[int] = None
    nacionalidad: Optional[str] = None
    peso_kg: Optional[float] = None
    altura_cm: Optional[float] = None
    estado: States = States.ACTIVO   
    posicion: Position               
    foto_url: Optional[str] = None
    partidos_jugados: int = 0
    goles_anotados: int = 0
    goles_recibidos: int = 0
    tarjetas_amarillas: int = 0
    tarjetas_rojas: int = 0

class JugadorCreate(JugadorBase):
    pass

class JugadorUpdate(BaseModel):
    nombre: Optional[str] = None
    numero_camiseta: Optional[int] = None
    fecha_nacimiento: Optional[date] = None
    edad: Optional[int] = None
    nacionalidad: Optional[str] = None
    peso_kg: Optional[float] = None
    altura_cm: Optional[float] = None
    estado: Optional[States] = None   
    posicion: Optional[Position] = None
    foto_url: Optional[str] = None
    partidos_jugados: Optional[int] = None
    goles_anotados: Optional[int] = None
    goles_recibidos: Optional[int] = None
    tarjetas_amarillas: Optional[int] = None
    tarjetas_rojas: Optional[int] = None

class JugadorOut(JugadorBase):
    id: int
    eliminado: bool

    class Config:
        from_attributes = True
