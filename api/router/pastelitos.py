from fastapi import APIRouter, responses, Response
from starlette.status import HTTP_201_CREATED
from api.model.schemas import basePastel
from api.model.Productos import Productos
from api.model.Rebajas import Rebajas
from api.model.Categorias import Categorias
from typing import List
from datetime import datetime
from api.model.Clientes import Clientes
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK
from typing import List
from datetime import datetime

pastel = APIRouter()


@pastel.get("/")
def root():
    return {"Bienvenida": "Hola :))"}

@pastel.get("/api/verproductos", response_model=List[basePastel.BaseProductos])
def VerProductos():
    pr = Productos()
    retorno = pr.verProductos()
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

@pastel.get("/api/Buscarporidproducto/<id>", response_model=List[basePastel.Basevistproducto])
def BuscarPoridProducto(id: str):
    p = Productos()
    retorno = p.BuscaridProducto(id)
    return retorno

@pastel.post("/api/CrearUsuario")
def CrearUsuario(listau: basePastel.BaseUsuarios):
    u = Usuarios()
    c = Clientes()
    tiempo = datetime.now()
    horaActual = tiempo.strftime('%d/%m/%Y %H:%M:%S')
    contra = generate_password_hash(listau.password, "pbkdf2:sha256:30", 30)
    
    u.ConstructorUsuario(0, listau.nombres, listau.correo,
                         listau.apellidos, contra, horaActual, 2)
    
    c.ConstructorClientes(0, listau.nombres, listau.apellidos,"0", listau.correo, horaActual, "Credito")
    
    verificar = u.verificarSiexiste()
    if verificar != HTTP_200_OK:
        retorno = u.CrearUsuario()
        retorno2 = c.CrearCliente()
    else:
        retorno = HTTP_400_BAD_REQUEST
    
    return Response(status_code=retorno)

@pastel.get("/api/log/<correol><pasw>", response_model= basePastel.BasePerfil)
def usuario(correol: str, pasw: str):
    u = Usuarios()
    u.ConstructorUsuario(0,"", correol,"", pasw, "", 0)
    
    retorno1 = u.autenticar()
    if retorno1 != HTTP_400_BAD_REQUEST:
        usuarioMenu = Menu()
        retorno = usuarioMenu.buscarUsuario(correol)
        return retorno
    else:
        return Response(status_code=retorno1)

#INICIO CLIENTE 

@pastel.get("/api/ListarClientes", response_model= List[basePastel.BaseCliente])
def ListarClientes():
    c = Clientes()
    retorno = c.verClientes()
    return retorno

@pastel.get("/api/Listartipodocumento", response_model=List[basePastel.TipoDocumento])
def ListarDocumentos():
    c = Clientes()
    retorno = c.verDocumento()
    return retorno

@pastel.get("/api/Listartipopago", response_model=List[basePastel.Tipopago])
def ListartipoPago():
    c = Clientes()
    retorno = c.verTipoPago()
    return retorno
    