from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import List, Optional
from ..models import Jugador

class JugadoresRepo:
    def crear(self, db: Session, jugador: Jugador) -> Jugador:
        db.add(jugador)
        db.commit()
        db.refresh(jugador)
        return jugador

    def obtener(self, db: Session, id_: int) -> Optional[Jugador]:
        return db.get(Jugador, id_)

    def listar(self, db: Session, incluir_eliminados: bool = False) -> List[Jugador]:
        stmt = select(Jugador)
        if not incluir_eliminados:
            stmt = stmt.where(Jugador.eliminado == False)
        return db.scalars(stmt).all()

    def actualizar(self, db: Session, jugador: Jugador) -> Jugador:
        db.add(jugador)
        db.commit()
        db.refresh(jugador)
        return jugador

    def soft_delete(self, db: Session, jugador: Jugador) -> Jugador:
        jugador.eliminado = True
        db.commit()
        db.refresh(jugador)
        return jugador

    def restaurar(self, db: Session, jugador: Jugador) -> Jugador:
        jugador.eliminado = False
        db.commit()
        db.refresh(jugador)
        return jugador
