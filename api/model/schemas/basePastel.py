from pydantic import BaseModel


class BaseCrearProducto(BaseModel):
    id: int 
    idCategoria: int
    categoria: str
    nombreProducto: str
    descripcion: str     
    nombreImagen: str
    precioCosto: float
    precioVenta: float
    idRebajas: int
    nombre_rebaja:str
    porcentaje_rebaja:str
    fecha_inicio_rebaja: str
    cantidad: int
    fecha_creacion:str
    id_sabor:int
    id_relleno: int
    sabor: str
    relleno:str
    
    
class BaseConfigurarRebajas(BaseModel):
    id:int
    descripcion:str
    porcentaje:str
    tiempo: str
    fecha_inicio:str
    
class BaseCategorias(BaseModel):
    id:int
    nombreCategoria:str
    descripcion:str

class BaseSabores(BaseModel):
    id: int 
    nombre_sabor:str

class BaseRellenos(BaseModel):
    id:int
    nombre_relleno:str
    
class Basevistproducto(BaseModel):
    id: int
    producto:str
    descripcion:str
    imagen:str
    precio:str