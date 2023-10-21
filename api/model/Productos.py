from database.Conexiondb import connection
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_200_OK
import cx_Oracle


class Productos():
    def __init__(self) -> None:
        pass

        # CONSTRUCTOR PRODUCTOS AGREGAR, ELIMINAR, ACTUALIZAR
    def ConstructorProductos(self, id, idCategoria,categoria, nombreProducto, descripcion, nombreImagen, precioCosto, precioVenta, idRebajas, cantidad, fecha_creacion, idsabor, idrelleno):
        self.id = id
        self.idCategoria = idCategoria
        self.nombreProducto = nombreProducto
        self.descripcion = descripcion
        self.nombreImagen = nombreImagen
        self.precioCosto = precioCosto
        self.precioVenta = precioVenta
        self.idRebajas = idRebajas
        self.cantidad = cantidad
        self.fecha_creacion = fecha_creacion
        self.idsabor = idsabor
        self.idrelleno = idrelleno

    def verSabor(self):
        cn = connection.cursor()
        query = "SELECT * FROM SABORES"
        r = cn.execute(query).fetchall()
        item = []
        for row in r:
            dicti = {}
            dicti["id"] = row[0]
            dicti["nombre_sabor"] = row[1]
            item.append(dicti)
        return item

    def verRellenos(self):
        cn = connection.cursor()
        query = "SELECT * FROM RELLENOS"
        r = cn.execute(query).fetchall()
        item = []
        for row in r:
            dicti = {}
            dicti["id"] = row[0]
            dicti["nombre_relleno"] = row[1]
            item.append(dicti)
        return item

    def verProductos(self):
        cn = connection.cursor()
        query = "SELECT P.IDPRODUCTO, P.ID_CATEGORIA, C.NOMBRE, P.PRODUCTO, P.DESCRIPCION, P.IMAGEN, P.PRECIO_COSTO, P.PRECIO_VENTA, P.IDCONFIGURAR_REBAJAS,R.DESCRIPCION,\
                R.PORCENTAJE, R.FECHA_INICIO_REBAJA, P.CANTIDAD, P.FECHA_CREACION, P.ID_SABOR, P.ID_RELLENO,S.NOMBRE_SABOR, R.NOMBRE_RELLENO FROM\
                PRODUCTOS P, CATEGORIAS C, CONFIGURAR_REBAJAS R, SABORES S, RELLENOS R\
                WHERE P.ID_CATEGORIA = C.IDCATEGORIA AND P.IDCONFIGURAR_REBAJAS = R.IDCONFIGURAR_REBAJAS AND P.ID_SABOR = S.ID_SABOR AND P.ID_RELLENO = R.ID_RELLENO"
        r = cn.execute(query)
        item = []
        for row in r:
            dicti = {}
            dicti["id"] = row[0]
            dicti["idCategoria"] = row[1]
            dicti["categoria"] = row[2]
            dicti["nombreProducto"] = row[3]
            dicti["descripcion"] = row[4]
            dicti["nombreImagen"] = str(row[5])
            dicti["precioCosto"] = row[6]
            dicti["precioVenta"] = (round(row[7], 2))
            dicti["idRebajas"] = row[8]
            dicti["nombre_rebaja"] = row[9]
            dicti["porcentaje_rebaja"] = row[10]
            dicti["fecha_inicio_rebaja"] = row[11]
            dicti["cantidad"] = row[12]
            dicti["fecha_creacion"] = row[13]
            dicti["id_sabor"] = row[14]
            dicti["id_relleno"] = row[15]
            dicti["sabor"] = row[16]
            dicti["relleno"] = row[17]

            item.append(dicti)
        return item

    def agregarProducto(self):
        try:
            cn = connection.cursor()
            query = "INSERT INTO PRODUCTOS(ID_CATEGORIA, PRODUCTO, DESCRIPCION, IMAGEN, PRECIO_COSTO, PRECIO_VENTA,IDCONFIGURAR_REBAJAS, CANTIDAD, FECHA_CREACION, ID_SABOR, ID_RELLENO )\
                VALUES(:1, :2,:3,:4, :5,:6,:7, :8, :9, :10, :11)"
            r = cn.execute(query, (
                self.idCategoria,
                self.nombreProducto,
                self.descripcion,
                self.nombreImagen,
                self.precioCosto,
                self.precioVenta,
                self.idRebajas,
                self.cantidad,
                self.fecha_creacion,
                self.idsabor,
                self.idrelleno
            ))
            connection.commit()
            return HTTP_201_CREATED
        except cx_Oracle.Error as error:
            print("ModificarProductos ", error)
            return HTTP_400_BAD_REQUEST

    def ActualizarProducto(self):
        try:
            cn = connection.cursor()
            query = "UPDATE PRODUCTOS SET ID_CATEGORIA = :1, PRODUCTO=:2, DESCRIPCION =:3, IMAGEN=:4,\
            PRECIO_COSTO =:5, PRECIO_VENTA =:6, IDCONFIGURAR_REBAJAS =:7, CANTIDAD=:8, ID_SABOR =:9, ID_RELLENO =:10 WHERE IDPRODUCTO = :11"
            r = cn.execute(query, (
                self.idCategoria,
                self.nombreProducto,
                self.descripcion,
                self.nombreImagen,
                self.precioCosto,
                self.precioVenta,
                self.idRebajas,
                self.cantidad,
                self.idsabor,
                self.idrelleno,
                self.id
            ))
            connection.commit()
            return HTTP_200_OK
        except cx_Oracle.Error as error:
            print("ModificarProductos ", error)
            return HTTP_400_BAD_REQUEST

    def EliminarProducto(self):
        try:
            cn = connection.cursor()
            query = "DELETE PRODUCTOS WHERE IDPRODUCTO=" + str(self.id)
            cn.execute(query)
            connection.commit()
            return HTTP_200_OK
        except cx_Oracle.Error as error:
            print("EliminarProductos ", error)
            return HTTP_400_BAD_REQUEST

    def vercategoria1(self, id):
        cn = connection.cursor()
        query = "SELECT IDPRODUCTO, PRODUCTO, DESCRIPCION, IMAGEN, PRECIO_COSTO FROM PRODUCTOS WHERE ID_CATEGORIA ="+str(id)
        resultado = cn.execute(query).fetchall()
        item = []
        for row in resultado:
            dicti ={}
            dicti["id"] = row[0]
            dicti["producto"] = row[1]
            dicti["descripcion"] = row[2]
            dicti["imagen"] = row[3]
            dicti["precio"] = str(row[4])
            item.append(dicti)
        return item