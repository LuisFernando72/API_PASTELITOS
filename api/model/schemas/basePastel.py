from pydantic import BaseModel


class BaseCrearProducto(BaseModel):
    id: int 
    idCategoria: int
    nombreProducto: str
    idMarca: int
    descripcion: str     
    nombreImagen: str
    precioCosto: float
    precioVenta: float
    idRebajas: int
    
    
class BaseConfigurarRebajas(BaseModel):
    id:int
    descripcion:str
    porcentaje:float
    tiempo: str
    
class BaseTipoProducto(BaseModel):
    id:int
    nombreCategoria:str
    estado:str
    fechaCreacion:str
    fechaActualizacion:str