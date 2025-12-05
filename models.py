from sqlalchemy import Column, Integer, String, Date, Float, Boolean
from sqlalchemy.orm import validates
from .database import Base

class Jugador(Base):
    __tablename__ = "jugadores"


    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(150), nullable=False, index=True)
    numero_camiseta = Column(Integer, nullable=False, index=True)
    fecha_nacimiento = Column(Date, nullable=True)
    edad = Column(Integer, nullable=True, index=True)
    nacionalidad = Column(String(80), nullable=True, index=True)
    foto_url = Column(String(255), nullable=True)

    
    estado = Column(String(20), nullable=False, default="activo", index=True)  # activo/suspendido
    eliminado = Column(Boolean, default=False, index=True)  # soft delete

    
    peso_kg = Column(Float, nullable=True, index=True)
    altura_cm = Column(Float, nullable=True, index=True)

    
    partidos_jugados = Column(Integer, default=0, index=True)
    goles_anotados = Column(Integer, default=0, index=True)
    goles_recibidos = Column(Integer, default=0, index=True)
    tarjetas_amarillas = Column(Integer, default=0, index=True)
    tarjetas_rojas = Column(Integer, default=0, index=True)

    def promedio_goles_anotados(self) -> float:
        return 0 if self.partidos_jugados == 0 else self.goles_anotados / self.partidos_jugados

    def promedio_goles_recibidos(self) -> float:
        return 0 if self.partidos_jugados == 0 else self.goles_recibidos / self.partidos_jugados

  
    @validates("estado")
    def validate_estado(self, key, value):
        v = (value or "").lower()
        if v not in {"activo", "suspendido"}:
            raise ValueError("Estado inválido: debe ser 'activo' o 'suspendido'")
        return v
