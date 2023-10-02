from fastapi import APIRouter, responses
from starlette.status import HTTP_201_CREATED
from api.model.schemas import basePastel

pastel = APIRouter()


@pastel.get("/")
def root():
    return {"Bienvenida": "Hola :))"}

@pastel.post("/api/configurarRebajas", status_code=HTTP_201_CREATED)
def ConfigurarRebajas(dataRebaja: basePastel.BaseConfigurarRebajas):
    pass