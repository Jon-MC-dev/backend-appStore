class Persona:
    def __init__(self, conexion):
        self.conexion = conexion


    def insertar(self, nombre, apellido_paterno, apellido_materno, edad, sexo):
        return self.conexion.insetar_actualizar_eliminar("INSERT INTO tbl_personas (nombre, apellido_paterno, apellido_materno, edad, sexo) VALUE('"+nombre+"', '"+apellido_paterno+"', '"+apellido_materno+"', '"+str(edad)+"', '"+sexo+"')")


    def actualizar(self, id, nombre, apellido_paterno, apellido_materno, edad, sexo):
        return self.conexion.insetar_actualizar_eliminar("UPDATE tbl_personas SET nombre='"+nombre+"', apellido_paterno='"+apellido_paterno+"', apellido_materno='"+apellido_materno+"', edad='"+str(edad)+"', sexo='"+sexo+"' WHERE id_persona = "+str(id))


    def eliminar(self, id):
        return self.conexion.insetar_actualizar_eliminar("DELETE FROM tbl_personas WHERE id_persona="+str(id))

    def getAll(self, id = 0):
        if id == 0:
            respuesta = self.conexion.traerRegistros("SELECT * FROM tbl_personas")
        else:
            respuesta = self.conexion.traerRegistros("SELECT * FROM tbl_personas WHERE id_persona="+str(id))
        arreglo = []
        for tupa_marca in respuesta:
            json ={'id': tupa_marca[0], 'nombre': tupa_marca[1], 'apellido_paterno': tupa_marca[2], 'apellido_materno': tupa_marca[3], 'edad': tupa_marca[4], 'sexo': tupa_marca[5]}
            arreglo.append(json)
        return arreglo
