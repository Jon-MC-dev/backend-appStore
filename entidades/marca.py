class Marca:
    def __init__(self, conexion):
        self.conexion = conexion


    def insertar(self, nombre):
        return self.conexion.insetar_actualizar_eliminar("INSERT INTO tbl_marcas (nombre) VALUE('"+nombre+"')")


    def actualizar(self, nombre, id):
        return self.conexion.insetar_actualizar_eliminar("UPDATE tbl_marcas SET nombre='"+nombre+"' WHERE id_marca = "+str(id))


    def eliminar(self, id):
        return self.conexion.insetar_actualizar_eliminar("DELETE FROM tbl_marcas WHERE id_marca="+str(id))

    def getAll(self, id = 0):
        if id == 0:
            respuesta = self.conexion.traerRegistros("SELECT * FROM tbl_marcas")
        else:
            respuesta = self.conexion.traerRegistros("SELECT * FROM tbl_marcas WHERE id_marca="+str(id))
        arreglo = []
        for tupa_marca in respuesta:
            json ={'id_marca': tupa_marca[0], 'marca': tupa_marca[1]}
            arreglo.append(json)
        return arreglo
