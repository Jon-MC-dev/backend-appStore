class Fotografia:
    def __init__(self, conexion):
        self.conexion = conexion


    def insertar(self, id_producto, fotografia, id_color):
        return self.conexion.insetar_actualizar_eliminar("INSERT INTO tbl_colores_fotografias (id_producto, fotografia, id_color) VALUE('"+str(id_producto)+"', '"+fotografia+"', '"+str(id_color)+"')")


    def actualizar(self, id, id_producto, fotografia, id_color):
        return self.conexion.insetar_actualizar_eliminar("UPDATE tbl_colores_fotografias SET id_producto='"+str(id_producto)+"', fotografia='"+fotografia+"', id_color='"+str(id_color)+"' WHERE id_foto = "+str(id))


    def eliminar(self, id):
        return self.conexion.insetar_actualizar_eliminar("DELETE FROM tbl_colores_fotografias WHERE id_foto="+str(id))

    def getAll(self, id = 0):
        if id == 0 or id == '0':
            respuesta = self.conexion.traerRegistros("SELECT * FROM tbl_colores_fotografias")
        else:
            respuesta = self.conexion.traerRegistros("SELECT * FROM tbl_colores_fotografias WHERE id_foto="+str(id))
        arreglo = []
        for tupa_marca in respuesta:
            json ={'id_foto': tupa_marca[0], 'id_producto': tupa_marca[1], 'fotografia': tupa_marca[2], 'id_color': tupa_marca[3]}
            arreglo.append(json)
        return arreglo
