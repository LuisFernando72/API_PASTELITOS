from fastapi import APIRouter, responses, Response
from starlette.status import HTTP_201_CREATED
from api.model.schemas import basePastel
from api.model.Productos import Productos
from api.model.Rebajas import Rebajas
from api.model.Categorias import Categorias
from typing import List
from datetime import datetime
pastel = APIRouter()


@pastel.get("/")
def root():
    return {"Bienvenida": "Hola :))"}


@pastel.post("/api/configurarRebajas", status_code=HTTP_201_CREATED)
def ConfigurarRebajas(dataRebaja: basePastel.BaseConfigurarRebajas):
    pass


@pastel.get("/api/verproductos", response_model=List[basePastel.BaseProductos])
def VerProductos():
    pr = Productos()
    retorno = pr.verProductos()
    return retorno

@pastel.get("/api/verRebajas", response_model= List[basePastel.BaseConfigurarRebajas])
def verRebajas():
    r = Rebajas()
    retorno = r.verRebajas()
    return retorno

@pastel.get("/api/verCategorias", response_model=List[basePastel.BaseCategorias])
def VerCategorias():
    c = Categorias()
    retorno = c.verCategorias()
    return retorno

@pastel.get("/api/verSabores", response_model=List[basePastel.BaseSabores])
def verSabores():
    s = Productos()
    retorno = s.verSabor()
    return retorno

@pastel.get("/api/verRellenos", response_model=List[basePastel.BaseRellenos])
def verRellenos():
    s = Productos()
    retorno = s.verRellenos()
    return retorno

@pastel.post("/api/crearProducto")
def CrearProducto(datap : basePastel.BaseProductos):
    p = Productos()
    nuevadesc = datap.categoria + ", "+datap.nombreProducto + ", sabor a "+ datap.sabor + ", con relleno de "+ datap.relleno
    pventa = (datap.precioCosto+(datap.precioCosto*1)/150)
    tiempo = datetime.now()
    horaActual = tiempo.strftime('%d/%m/%Y %H:%M:%S')
    p.ConstructorProductos(0, datap.idCategoria, "",  datap.nombreProducto,nuevadesc, datap.nombreImagen, datap.precioCosto, pventa,datap.idRebajas, datap.cantidad, horaActual, datap.id_sabor, datap.id_relleno)
    retorno = p.agregarProducto()
    return Response(status_code = retorno)

@pastel.put("/api/actualizarProducto")
def ActualizarProducto(datap : basePastel.BaseProductos):
    p = Productos()
    nuevadesc = datap.categoria + ", "+datap.nombreProducto + ", sabor a "+ datap.sabor + ", con relleno de "+ datap.relleno
    pventa = (datap.precioCosto+(datap.precioCosto*1)/150)
    tiempo = datetime.now()
    horaActual = tiempo.strftime('%d/%m/%Y %H:%M:%S')
    p.ConstructorProductos(datap.id, datap.idCategoria, "",  datap.nombreProducto,nuevadesc, datap.nombreImagen, datap.precioCosto, pventa,datap.idRebajas, datap.cantidad, horaActual, datap.id_sabor, datap.id_relleno)
    retorno = p.ActualizarProducto()
    return Response(status_code=retorno)

@pastel.delete("/api/EliminarProducto")
def EliminarProducto(datap : basePastel.BaseProductos):
    p = Productos()
    nuevadesc = datap.categoria + ", "+datap.nombreProducto + ", sabor a "+ datap.sabor + ", con relleno de "+ datap.relleno
    pventa = (datap.precioCosto+(datap.precioCosto*1)/150)
    tiempo = datetime.now()
    horaActual = tiempo.strftime('%d/%m/%Y %H:%M:%S')
    p.ConstructorProductos(datap.id, datap.idCategoria, "",  datap.nombreProducto,nuevadesc, datap.nombreImagen, datap.precioCosto, pventa,datap.idRebajas, datap.cantidad, horaActual, datap.id_sabor, datap.id_relleno)
    retorno = p.EliminarProducto()
    return Response(status_code=retorno)

@pastel.get("/api/Buscarporcategoria/<id>", response_model=List[basePastel.Basevistproducto])
def BuscarPorCategoria(id:str):
    p = Productos()
    retorno = p.vercategoria1(id)
    return retorno

@pastel.post("/api/CrearRebaja")
def CrearRebaja(datar: basePastel.BaseConfigurarRebajas):
    r = Rebajas()
    