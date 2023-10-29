from database.Conexiondb import connection


class Pedidos():

    def __init__(self) -> None:
        pass

    def verMispedidos(self, correo):
        cn = connection.cursor()
        query = "SELECT P.ID_PEDIDO, P.NODOCUMENTO, P.SERIE, P.NOMBRE_DOCUMENTO, P.FECHAPEDIDO, P.ESTADOPEDIDO,\
                R.PRODUCTO, R.PRECIO_COSTO,PD.CANTIDAD FROM PEDIDOS P, PEDIDO_DETALLE PD, PRODUCTOS R, CLIENTES C\
                WHERE P.ID_PEDIDO = PD.IDPEDIDO AND PD.IDPRODUCTO = R.IDPRODUCTO AND C.CORREO_E ='"+correo+"'"
        resultado = cn.execute(query).fetchall()

        item = []
        for row in resultado:
            dicti = {}
            dicti["id"] = row[0]
            dicti["nodocumento"] = str(row[1])
            dicti["serie"] = row[2]
            dicti["nombredocumento"] = row[3]
            dicti["fechapedidos"] = str(row[4])
            dicti["estadopedido"] = row[5]
            dicti["producto"] = row[6]
            dicti["preciocosto"] = str(row[7])
            dicti["cantidad"] = row[8]
            item.append(dicti)

        return item

    def verEntregas(self):
        cn = connection.cursor()
        query = "SELECT P.ID_PEDIDO, P.NODOCUMENTO, P.NOMBRE_DOCUMENTO, P.FECHAPEDIDO, P.ESTADOPEDIDO,C.NOMBRES, C.APELLIDOS\
                         FROM PEDIDOS P,   CLIENTES C WHERE P.IDCLIENTE = C.IDCLIENTE"
        resultado = cn.execute(query).fetchall()

        item = []
        for row in resultado:
            dicti = {}
            dicti["ID_PEDIDO"] = row[0]
            dicti["NODOCUMENTO"] = str(row[1])
            dicti["NOMBRE_DOCUMENTO"] = row[2]
            dicti["FECHAPEDIDO"] = row[3]
            dicti["ESTADOPEDIDO"] = str(row[4])
            dicti["NOMBRES"] = row[5]
            dicti["APELLIDOS"] = row[6]

            item.append(dicti)

        return item
