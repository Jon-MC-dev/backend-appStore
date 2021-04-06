class Usuario:
    def __init__(self, conexion):
        self.conexion = conexion


    def insertar(self, id, usuario, contrasena, permisos):
        return self.conexion.insetar_actualizar_eliminar("INSERT INTO tbl_usuarios (id_persona, usuario, contrasena, permisos) VALUE('"+str(id)+"', '"+usuario+"', '"+contrasena+"', '"+permisos+"')")


    def actualizar(self, id, usuario, contrasena, permisos):
        return self.conexion.insetar_actualizar_eliminar("UPDATE tbl_usuarios SET usuario='"+usuario+"', contrasena='"+contrasena+"', permisos='"+permisos+"' WHERE id_persona = "+str(id))


    def eliminar(self, id):
        return self.conexion.insetar_actualizar_eliminar("DELETE FROM tbl_usuarios WHERE id_persona="+str(id))

    def getAll(self, id = 0):
        if id == 0:
            respuesta = self.conexion.traerRegistros("SELECT * FROM tbl_usuarios")
        else:
            respuesta = self.conexion.traerRegistros("SELECT * FROM tbl_usuarios WHERE id_persona="+str(id))
        arreglo = []
        for tupa_marca in respuesta:
            json ={'id_persona': tupa_marca[0], 'usuario': tupa_marca[1], 'contrasena': tupa_marca[2], 'permisos': tupa_marca[3] }
            arreglo.append(json)
        return arreglo
