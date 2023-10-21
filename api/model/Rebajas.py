from database.Conexiondb import connection
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
import cx_Oracle


class Rebajas():
    # CONSTRUCTOR REBAJAS AGREGAR, ELIMINAR, ACTUALIZAR
    def __init__(self) -> None:
        pass

    def constructorRebajas(self, id, descripcion, porcentaje, tiempo, fecha_inicio_rebaja):
        self.id = id
        self.descripcion = descripcion
        self.porcentaje = porcentaje
        self.tiempo = tiempo
        self.fecha_inicio_rebaja = fecha_inicio_rebaja

    def verRebajas(self):
        cn = connection.cursor()
        query = "SELECT * FROM CONFIGURAR_REBAJAS"
        r = cn.execute(query).fetchall()
        item = []
        for row in r:
            dicti = {}
            dicti["id"] = row[0]
            dicti["descripcion"] = row[1]
            dicti["porcentaje"] = str(row[2])
            dicti["tiempo"] = str(row[3])
            dicti["fecha_inicio"] = row[4]
            item.append(dicti)

        return item

    def AgregaRebajas(self):
        try:
            cn = connection.cursor()
            query = "INSERT INTO CONFIGURAR_REBAJAS(DESCRIPCION, PORCENTAJE, TIEMPO_DIAS, FECHA_INICIO_REBAJA)\
                VALUES(:1,:2,:3,:4)"
            cn.execute(query, (
                self.descripcion,
                self.porcentaje,
                self.tiempo,
                self.fecha_inicio_rebaja
            ))
            connection.commit()
            return HTTP_201_CREATED

        except cx_Oracle.Error as error:
            print("Agregar rebajas ", error)
            return HTTP_400_BAD_REQUEST
          
          
    def ActualizarRebajas(self):
        try:
            cn = connection.cursor()
            query = "UPDATE CONFIGURAR_REBAJAS SET DESCRIPCION  =:1, PORCENTAJE =:2, TIEMPO_DIAS=:3, FECHA_INICIO_REBAJA =:4\
                    WHERE IDCONFIGURAR_REBAJAS =:5"
            cn.execute(query, (
                self.descripcion,
                self.porcentaje,
                self.tiempo,
                self.fecha_inicio_rebaja,
                self.id
            ))
            connection.commit()
            return HTTP_200_OK
        except cx_Oracle.Error as error:
            print("Actualizar rebajas ", error)
            return HTTP_400_BAD_REQUEST
          
    def ActualizarRebajas(self):
        try:
            cn = connection.cursor()
            cn.execute("DELETE CONFIGURAR_REBAJAS WHERE IDCONFIGURAR_REBAJAS ="+ str(self.id))
            connection.commit()
            return HTTP_200_OK
        except cx_Oracle.Error as error:
            print("Eliminar rebajas ", error)
            return HTTP_400_BAD_REQUEST