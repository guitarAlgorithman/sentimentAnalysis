from fastapi import FastAPI
from reader import getSentimiento

app = FastAPI()


@app.get("/{busqueda}")
async def root(busqueda):
    salida=getSentimiento(busqueda)
    return salida.json()
