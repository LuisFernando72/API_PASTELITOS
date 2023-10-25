from database.Conexiondb import connection
from starlette.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_400_BAD_REQUEST
from werkzeug.security import generate_password_hash, check_password_hash


class Usuarios():
    def __init__(self) -> None:
        pass

    def ConstructorUsuario(self, id, nombres, correo, apellidos, password, fecha, idrol):
        self.id = id
        self.nombres = nombres
        self.correo = correo
        self.apellidos = apellidos
        self.password = password
        self.fecha = fecha
        self.idrol = idrol

    def CrearUsuario(self):
        cn = connection.cursor()
        query = "INSERT INTO USUARIOS(NOMBRE, CORREO_ELECCTRONICO, APELLIDOS, CONTRASENIA, FECHA_CREACION, ROLES_ID_ROL)\
                VALUES(:1,:2,:3,:4,:5,:6)"
        cn.execute(query, (
            self.nombres,
            self.correo,
            self.apellidos,
            self.password,
            self.fecha,
            self.idrol
        ))
        connection.commit()
        return HTTP_201_CREATED

    def autenticar(self):
        retorno = ""
        seleccionar = connection.cursor()
        resultado = seleccionar.execute(
            "SELECT * FROM USUARIOS WHERE CORREO_ELECCTRONICO = '" + self.correo+"'")
        usuario = resultado.fetchone()
        if usuario is not None:
            contra = usuario[4]
            check_pass = check_password_hash(contra, self.password)
            if check_pass:
                retorno = HTTP_200_OK
            else:
                retorno = HTTP_400_BAD_REQUEST

        else:
            retorno = HTTP_400_BAD_REQUEST
        return retorno

    def verificarSiexiste(self):
        retorno = ""
        seleccionar = connection.cursor()
        resultado = seleccionar.execute(
            "SELECT * FROM USUARIOS WHERE CORREO_ELECCTRONICO = '" + self.correo+"'")
        usuario = resultado.fetchone()
        if usuario is not None:
            retorno = HTTP_200_OK
        else:
            retorno = HTTP_400_BAD_REQUEST
        return retorno
