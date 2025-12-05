from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from ..database import get_db
from ..services.jugadores_service import JugadoresService
from ..schemas import JugadorCreate, JugadorUpdate, JugadorOut

router = APIRouter(prefix="/jugadores", tags=["jugadores"])
service = JugadoresService()

@router.get("/", response_model=list[JugadorOut])
def listar_jugadores(db: Session = Depends(get_db)):
    return service.listar(db)

@router.get("/eliminados/", response_model=list[JugadorOut])
def listar_eliminados(db: Session = Depends(get_db)):
    return service.listar(db, incluir_eliminados=True)

@router.post("/crear/", response_model=JugadorOut, status_code=201)
def crear_jugador(payload: JugadorCreate, db: Session = Depends(get_db)):
    return service.crear(db, payload)

@router.patch("/editar/{id}", response_model=JugadorOut)
def editar_jugador(id: int, payload: JugadorUpdate, db: Session = Depends(get_db)):
    j = service.actualizar(db, id, payload)
    if not j:
        raise HTTPException(status_code=404, detail="Jugador no encontrado o eliminado")
    return j

@router.delete("/eliminar/{id}", response_model=JugadorOut)
def eliminar_jugador(id: int, db: Session = Depends(get_db)):
    j = service.eliminar(db, id)
    if not j:
        raise HTTPException(status_code=404, detail="Jugador no encontrado o ya eliminado")
    return j

@router.post("/restaurar/{id}", response_model=JugadorOut)
def restaurar_jugador(id: int, db: Session = Depends(get_db)):
    j = service.restaurar(db, id)
    if not j:
        raise HTTPException(status_code=404, detail="Jugador no encontrado o no está eliminado")
    return j

@router.get("/buscar/", response_model=list[JugadorOut])
def buscar_jugadores(
    nombre: str | None = Query(default=None),
    id: int | None = Query(default=None),
    estado: str | None = Query(default=None, description="activo/suspendido"),
    nacionalidad: str | None = Query(default=None),
    edad: int | None = Query(default=None),
    peso_kg: float | None = Query(default=None),
    altura_cm: float | None = Query(default=None),
    partidos_jugados: int | None = Query(default=None),
    goles_anotados: int | None = Query(default=None),
    goles_recibidos: int | None = Query(default=None),
    tarjetas_amarillas: int | None = Query(default=None),
    tarjetas_rojas: int | None = Query(default=None),
    db: Session = Depends(get_db),
):
    filtros = {
        "nombre": nombre, "id": id, "estado": estado, "nacionalidad": nacionalidad,
        "edad": edad, "peso_kg": peso_kg, "altura_cm": altura_cm,
        "partidos_jugados": partidos_jugados, "goles_anotados": goles_anotados,
        "goles_recibidos": goles_recibidos, "tarjetas_amarillas": tarjetas_amarillas,
        "tarjetas_rojas": tarjetas_rojas,
    }
    return service.buscar(db, **{k: v for k, v in filtros.items() if v is not None})
