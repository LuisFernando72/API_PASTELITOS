from database.Conexiondb import connection


class Categorias():
    def __init__(self) -> None:
        pass
    
    def constructorCategorias(self,idcategoria, nombreCategoria, descripcion ):
        self.idcategoria = idcategoria
        self.nombreCategoria = nombreCategoria
        self.descripcion = descripcion
        
    
    def verCategorias(self):
        cn = connection.cursor()
        query = "SELECT * FROM CATEGORIAS"
        r = cn.execute(query).fetchall()
        item = []
        for row in r :
            dicti ={}
            dicti["id"] = row[0]
            dicti["nombreCategoria"] = row[1]
            dicti["descripcion"] = row[2]
            item.append(dicti)
        return item