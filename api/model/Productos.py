from database.Conexiondb import connection

class Productos():
    def __init__(self) -> None:
        pass
    
    #CONSTRUCTOR REBAJAS AGREGAR, ELIMINAR, ACTUALIZAR
    def ConfigurarRebajas(self, id, descripcion, porcentaje, tiempo):
        self.id = id
        self.descripcion = descripcion
        self.porcentaje = porcentaje
        self.tiempo = tiempo
        
        #CONSTRUCTOR TIPOPRODUCTO AGREGAR, ELIMINAR, ACTUALIZAR
    def TipoProducto(self, id, nombreCategoria, estado, fechaActualizacion):
        self.id = id
        self.nombreCategoria= nombreCategoria
        self.estado = estado
        self.fechaActualizacion = fechaActualizacion
        
        #CONSTRUCTOR PRODUCTOS AGREGAR, ELIMINAR, ACTUALIZAR
    def Productos(self, id, idCategoria, nombreProducto, idMarca, descripcion, nombreImagen, precioCosto, precioVenta, idRebajas):
        self.id = id
        self.idCategoria= idCategoria
        self.nombreProducto= nombreProducto
        self.idMarca = idMarca
        self.descripcion = descripcion    
        self.nombreImagen = nombreImagen
        self.precioCosto = precioCosto
        self.precioVenta = precioVenta
        self.idRebajas = idRebajas
    
    
    def AgregarRebajas(self):
        self.descripcion
        
    def EliminarRebajas(self):
        pass
    
    def ActualizarRebajas(self):
        pass
    
    #TIPO PRODUCTO
    
    def AgregarTipoProducto(self):
        self.descripcion
        
    def EliminarTipoProducto(self):
        pass
    
    def ActualizarTipoProducto(self):
        pass
    
    #PRODUCTOSSSSS
    def AgregarProductos(self):
        self.descripcion
        
    def EliminarProductos(self):
        pass
    
    def ActualizarProductos(self):
        pass