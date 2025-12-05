from fastapi import FastAPI
from .routers.jugadores import router as jugadores_router
from .database import Base, engine

def create_app():
    app = FastAPI(title="SigmotoaFC")
    app.include_router(jugadores_router)

    @app.get("/health")
    def health():
        return {"status": "ok"}

    return app

app = create_app()


Base.metadata.create_all(bind=engine)




