from database.Conexiondb import connection


class Clientes():
    def __init__(self) -> None:
        pass

    def ConstructorClientes(self, id, nombres, apellidos, nit, correo, fecha, tipocliente):
        self.id = id
        self.nombres = nombres
        self.apellidos = apellidos
        self.nit = nit
        self.correo = correo
        self.fecha = fecha
        self.tipocliente = tipocliente

    def CrearCliente(self):
        cn = connection.cursor()
        query = "INSERT INTO CLIENTES(NOMBRES, APELLIDOS, NIT, CORREO_E, FECHAINGRESO, TIPO_CLIENTE)\
                VALUES(:1, :2, :3,:4, :5, :6)"
        cn.execute(query, (
            self.nombres,
            self.apellidos,
            self.nit,
            self.correo,
            self.fecha,
            self.tipocliente
        ))
        connection.commit()
        return 1

    def verClientes(self):
        cn = connection.cursor()
        query = "SELECT * FROM CLIENTES"
        resultado = cn.execute(query).fetchall()
        item = []
        for row in resultado:
            dicti = {}
            dicti["idcliente"] = row[0]
            dicti["nombres"] = row[1]
            dicti["apellidos"] = row[2]
            dicti["nit"] = row[3]
            dicti["correo"] = row[4]
            dicti["fechaingreso"] = row[5]
            dicti["tipocliente"] = row[6]
            item.append(dicti)
        
        return item
    
    def verDocumento(self):
        cn = connection.cursor()
        query = "SELECT * FROM TIPOPEDIDO"
        resultado = cn.execute(query)
        item =[]
        for row in resultado:
            dicti={}
            dicti["id"] = row[0]
            dicti["documento"] = row[1]
            item.append(dicti)
        return item
    
    def verTipoPago(self):
        cn = connection.cursor()
        query = "SELECT * FROM TIPOPAGO"
        resultado = cn.execute(query)
        item =[]
        for row in resultado:
            dicti={}
            dicti["id"] = row[0]
            dicti["tipopago"] = row[1]
            item.append(dicti)
        return item
    
   