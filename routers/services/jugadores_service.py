from sqlalchemy.orm import Session
from typing import List, Optional
from ..models import Jugador
from ..schemas import JugadorCreate, JugadorUpdate
from ..repositories.jugadores_repo import JugadoresRepo

class JugadoresService:
    def __init__(self):
        self.repo = JugadoresRepo()

    def crear(self, db: Session, data: JugadorCreate) -> Jugador:
        jugador = Jugador(**data.model_dump())
        return self.repo.crear(db, jugador)

    def obtener(self, db: Session, id_: int) -> Optional[Jugador]:
        return self.repo.obtener(db, id_)

    def listar(self, db: Session, incluir_eliminados: bool = False) -> List[Jugador]:
        return self.repo.listar(db, incluir_eliminados)

    def actualizar(self, db: Session, id_: int, data: JugadorUpdate) -> Optional[Jugador]:
        jugador = self.repo.obtener(db, id_)
        if not jugador or jugador.eliminado:
            return None
        for k, v in data.model_dump(exclude_unset=True).items():
            setattr(jugador, k, v)
        return self.repo.actualizar(db, jugador)

    def eliminar(self, db: Session, id_: int) -> Optional[Jugador]:
        jugador = self.repo.obtener(db, id_)
        if not jugador or jugador.eliminado:
            return None
        return self.repo.soft_delete(db, jugador)

    def restaurar(self, db: Session, id_: int) -> Optional[Jugador]:
        jugador = self.repo.obtener(db, id_)
        if not jugador or not jugador.eliminado:
            return None
        return self.repo.restaurar(db, jugador)

    
    def buscar(self, db: Session, **filtros) -> List[Jugador]:
        from sqlalchemy import select, and_
        stmt = select(Jugador).where(Jugador.eliminado == False)
        conds = []

        
        if (nombre := filtros.get("nombre")):
            from sqlalchemy import func
            conds.append(func.lower(Jugador.nombre).like(f"%{nombre.lower()}%"))
        if (id_ := filtros.get("id")) is not None:
            conds.append(Jugador.id == id_)
        if (estado := filtros.get("estado")):
            conds.append(Jugador.estado == estado.lower())
        if (nacionalidad := filtros.get("nacionalidad")):
            conds.append(Jugador.nacionalidad == nacionalidad)
        if (edad := filtros.get("edad")) is not None:
            conds.append(Jugador.edad == edad)
        if (peso := filtros.get("peso_kg")) is not None:
            conds.append(Jugador.peso_kg == peso)
        if (altura := filtros.get("altura_cm")) is not None:
            conds.append(Jugador.altura_cm == altura)

       
        if (pj := filtros.get("partidos_jugados")) is not None:
            conds.append(Jugador.partidos_jugados == pj)
        if (ga := filtros.get("goles_anotados")) is not None:
            conds.append(Jugador.goles_anotados == ga)
        if (gr := filtros.get("goles_recibidos")) is not None:
            conds.append(Jugador.goles_recibidos == gr)
        if (ta := filtros.get("tarjetas_amarillas")) is not None:
            conds.append(Jugador.tarjetas_amarillas == ta)
        if (tr := filtros.get("tarjetas_rojas")) is not None:
            conds.append(Jugador.tarjetas_rojas == tr)

       
        if conds:
            stmt = stmt.where(and_(*conds))
        return db.scalars(stmt).all()

