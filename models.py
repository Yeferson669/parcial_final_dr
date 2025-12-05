from sqlalchemy import Column, Integer, String, Date, Float, Boolean, Enum as SqlEnum
from sqlalchemy.orm import validates
from .database import Base
from utils.positions import Position
from utils.states import States

class Jugador(Base):
    __tablename__ = "jugadores"

    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(150), nullable=False, index=True)
    numero_camiseta = Column(Integer, nullable=False, index=True)
    fecha_nacimiento = Column(Date, nullable=True)
    edad = Column(Integer, nullable=True, index=True)
    nacionalidad = Column(String(80), nullable=True, index=True)
    foto_url = Column(String(255), nullable=True)

    
    estado = Column(SqlEnum(States), nullable=False, default=States.ACTIVO)
    posicion = Column(SqlEnum(Position), nullable=False, default=Position.DEFENSA_C)

   
    eliminado = Column(Boolean, default=False, index=True)

   
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
