class Color:
    def __init__(self, conexion):
        self.conexion = conexion


    def insertar(self, color, codigo):
        return self.conexion.insetar_actualizar_eliminar("INSERT INTO tbl_catalogo_colores (color, codigo) VALUE('"+color+"', '"+codigo+"')")


    def actualizar(self, color, id, codigo):
        return self.conexion.insetar_actualizar_eliminar("UPDATE tbl_catalogo_colores SET color='"+color+"', codigo='"+codigo+"' WHERE id_color = "+str(id))


    def eliminar(self, id):
        return self.conexion.insetar_actualizar_eliminar("DELETE FROM tbl_catalogo_colores WHERE id_color="+str(id))

    def getAll(self, id = 0):
        if id == 0:
            respuesta = self.conexion.traerRegistros("SELECT * FROM tbl_catalogo_colores")
        else:
            respuesta = self.conexion.traerRegistros("SELECT * FROM tbl_catalogo_colores WHERE id_color="+str(id))
        arreglo = []
        for tupa_marca in respuesta:
            json ={'id_color': tupa_marca[0], 'color': tupa_marca[1], 'codigo':tupa_marca[2]}
            arreglo.append(json)
        return arreglo
