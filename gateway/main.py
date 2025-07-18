from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from modulos.comentarios.logica.comentario_service import router as comentarios_router

app = FastAPI(title="API Gateway")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(comentarios_router, prefix="/comentarios")