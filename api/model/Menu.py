from database.Conexiondb import connection


class Menu:
    def __init__(self):
        pass

    def mostrar_menu(self, menu):
        self.menu = menu
        # self.submenu = submenu

    def menuBuscar(self, idrol):
        self.idrol = idrol

    def buscarUsuario(self, correo2):
        seleccionar = connection.cursor()
        resultado = seleccionar.execute(
            "SELECT * FROM USUARIOS WHERE CORREO_ELECCTRONICO ='" + correo2+"'")
        usuario = resultado.fetchone()
        idRol = usuario[6]

        dictPerfil = {}
        dictPerfil["iduser"] = usuario[0]
        dictPerfil["nombres"] = usuario[1]
        dictPerfil["apellidos"] = usuario[3]
        dictPerfil["correo"] = usuario[2]
        dictPerfil["idperfil"] = str(usuario[6])

        d = Menu()

        selectmenu = d.menuBuscar(idRol)
        dictPerfil["pintarMenu"] = selectmenu
        seleccionar.close()

        return dictPerfil

    def menuBuscar(self, id_rol):
        select_menu = connection.cursor()
        # select_menu2 = connection.cursor()
        query = "SELECT M.SUBMODULO, M.NOMBRE, M.ENLACE, M.ICONON, M.TIPO FROM MENUMASTER M, PERFILES P\
                WHERE P.ID_MENU = M.SUBMODULO AND P.ID_ROL =" + str(id_rol)
        resultado = select_menu.execute(query).fetchall()
        print("menuBuscar")
        print(resultado)
        result = []
        for row in resultado:
            item_dict = {}

            if row[4] == "Menu":
                item_dict["id"] = str(row[0])
                item_dict["nombre"] = str(row[1])
                item_dict["enlaze"] = str(row[2])
                item_dict["icono"] = str(row[3])
                item_dict["tipo"] = str(row[4])
                result.append(item_dict)

        r = Menu()

        r.mostrar_menu(result)
        html = r.pintar_menu()
        print(html)
        return html

    def pintar_menu(self):
        listaMenu = self.menu

        kk = ""

        for m in listaMenu:
            kk += "<a id=\""+m["nombre"]+"\"  href=\"" + \
                m["enlaze"]+"\">"+ m["icono"] + m["nombre"]+"</a>"
            # else:
            #     kk += "<a id=\"CerrarSesion\" href=\"" + \
            #         m["enlaze"]+"\">"+m["icono"] + m["nombre"]+"</a>"

        return kk

    def menu(self):
        return self.menu
