class Categoria:
    def __init__(self, conexion):
        self.conexion = conexion


    def insertar(self, nombre):
        return self.conexion.insetar_actualizar_eliminar("INSERT INTO tbl_categorias (nombre) VALUE('"+nombre+"')")


    def actualizar(self, nombre, id):
        return self.conexion.insetar_actualizar_eliminar("UPDATE tbl_categorias SET nombre='"+nombre+"' WHERE id_categoria = "+str(id))


    def eliminar(self, id):
        return self.conexion.insetar_actualizar_eliminar("DELETE FROM tbl_categorias WHERE id_categoria="+str(id))

    def getAll(self, id = 0):
        if id == 0:
            respuesta = self.conexion.traerRegistros("SELECT * FROM tbl_categorias")
        else:
            respuesta = self.conexion.traerRegistros("SELECT * FROM tbl_categorias WHERE id_categoria="+str(id))
        arreglo = []
        for tupa_marca in respuesta:
            json ={'id_categoria': tupa_marca[0], 'categoria': tupa_marca[1]}
            arreglo.append(json)
        return arreglo
