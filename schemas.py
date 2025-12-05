from pydantic import BaseModel, field_validator
from typing import Optional
from datetime import date

class JugadorBase(BaseModel):
    nombre: str
    numero_camiseta: int
    fecha_nacimiento: Optional[date] = None
    edad: Optional[int] = None
    nacionalidad: Optional[str] = None
    peso_kg: Optional[float] = None
    altura_cm: Optional[float] = None
    estado: str = "activo"
    foto_url: Optional[str] = None
    partidos_jugados: int = 0
    goles_anotados: int = 0
    goles_recibidos: int = 0
    tarjetas_amarillas: int = 0
    tarjetas_rojas: int = 0

    @field_validator("estado")
    @classmethod
    def estado_valido(cls, v):
        if v.lower() not in {"activo", "suspendido"}:
            raise ValueError("Estado debe ser 'activo' o 'suspendido'")
        return v.lower()

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
    estado: Optional[str] = None
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
