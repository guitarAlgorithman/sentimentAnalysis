from fastapi import FastAPI
from reader import getSentimiento

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/{busqueda}")
async def root(busqueda):
    salida=getSentimiento(busqueda)
    return salida
