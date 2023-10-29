from database.Conexiondb import connection
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
import cx_Oracle


class Compras():
    def __init__(self) -> None:
        pass

    def agregarcompra(self, id, nodocumento, serie, nombredocumento, fechapedido, estado, idcliente, tipodocumento, tipopago):
        try:
            cn = connection.cursor()
            query = "INSERT INTO PEDIDOS(NODOCUMENTO, SERIE, NOMBRE_DOCUMENTO, FECHAPEDIDO, ESTADOPEDIDO,IDCLIENTE,\
                    TIPODOCUMENTO, TIPOPAGO)VALUES(:1, :2,:3,:4,:5,:6,:7,:8)"
            cn.execute(query, (
                nodocumento,
                serie,
                nombredocumento,
                fechapedido,
                estado,
                idcliente,
                tipodocumento,
                tipopago
            ))
            connection.commit()
            return HTTP_201_CREATED
        except cx_Oracle.Error as error:
            print("ERROR EN COMPRA   ", error)
            return HTTP_400_BAD_REQUEST

    def agregarDetalleCompra(self, idpedido, idproducto, cantidad, preciounitario):
        try:
            cn = connection.cursor()
            query = "INSERT INTO PEDIDO_DETALLE(IDPEDIDO, IDPRODUCTO, CANTIDAD, PRECIO_UNITARIO)\
                    VALUES(:1, :2,:3,:4)"
            cn.execute(query, (
                idpedido,
                idproducto,
                cantidad,
                preciounitario
            ))
            connection.commit()
            return HTTP_201_CREATED
        except cx_Oracle.Error as error:
            print("ERROR EN LA COMPRA DEL DETALLE  ", error)
            return HTTP_400_BAD_REQUEST
    
    def SeleccionaNodocumento(self):
        cn = connection.cursor()
        query = "SELECT  max(NODOCUMENTO) FROM PEDIDOS "
        resultado = cn.execute(query).fetchone()
        dicti ={}
        dicti["id"] = resultado[0]
        dicti["no"] = resultado[0]
        return dicti
    
    def SeleccionaridPedido(self, fecha):
        cn = connection.cursor()
        query = "SELECT ID_PEDIDO FROM PEDIDOS WHERE FECHAPEDIDO ='"+fecha+"'"
        resultado = cn.execute(query).fetchone()
        dicti = {}
        dicti["id"] = resultado[0]
        return dicti