class DetalleAdquisicion:
    def __init__(self, conexion):
        self.conexion = conexion


    def insertar(self, id_adquisicion, id_producto, precio_compra, cantidad):
        return self.conexion.insetar_actualizar_eliminar("INSERT INTO tbl_detalle_adquisicion (id_adquisicion, id_producto, precio_compra, cantidad) VALUE ('"+str(id_adquisicion)+"', '"+str(id_producto)+"', '"+str(precio_compra)+"', '"+str(cantidad)+"')")


    def actualizar(self, id, precio_compra, cantidad):
        return self.conexion.insetar_actualizar_eliminar("UPDATE tbl_detalle_adquisicion SET precio_compra='"+precio_compra+"', cantidad='"+cantidad+"' WHERE id_detalle = "+str(id))


    def eliminar(self, id):
        return self.conexion.insetar_actualizar_eliminar("DELETE FROM tbl_detalle_adquisicion WHERE id_detalle="+str(id))


    def getAll(self, id = 0):
        if id == 0:
            respuesta = self.conexion.traerRegistros("SELECT * FROM tbl_detalle_adquisicion")
        else:
            respuesta = self.conexion.traerRegistros("SELECT * FROM tbl_detalle_adquisicion WHERE id_adquisicion="+str(id))
        arreglo = []
        for tupa_marca in respuesta:
            json ={'id_detalle': tupa_marca[0], 'id_adquisicion': tupa_marca[1], 'id_producto': tupa_marca[2], 'precio_compra': tupa_marca[3], 'cantidad': tupa_marca[4]}
            arreglo.append(json)
        return arreglo
