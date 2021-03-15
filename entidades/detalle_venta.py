class DetalleVenta:
    def __init__(self, conexion):
        self.conexion = conexion


    def insertar(self, id_venta, id_producto, precio_venta, cantidad):
        return self.conexion.insetar_actualizar_eliminar("INSERT INTO tbl_detalle_venta (id_venta, id_producto, precio_venta, cantidad) VALUE ('"+str(id_venta)+"', '"+str(id_producto)+"', '"+str(precio_venta)+"', '"+str(cantidad)+"')")


    def actualizar(self, id, precio_total):
        return self.conexion.insetar_actualizar_eliminar("UPDATE tbl_detalle_venta SET precio_total='"+precio_total+"' WHERE id_detalle = "+str(id))


    def eliminar(self, id):
        return self.conexion.insetar_actualizar_eliminar("DELETE FROM tbl_detalle_venta WHERE id_detalle="+str(id))


    def getAll(self, id = 0):
        if id == 0:
            respuesta = self.conexion.traerRegistros("SELECT * FROM tbl_detalle_venta")
        else:
            respuesta = self.conexion.traerRegistros("SELECT * FROM tbl_detalle_venta WHERE id_venta="+str(id))
        arreglo = []
        for tupa_marca in respuesta:
            json ={'id_detalle': tupa_marca[0], 'id_venta': tupa_marca[1], 'id_producto': tupa_marca[2], 'precio_venta': tupa_marca[3], 'cantidad': tupa_marca[4]}
            arreglo.append(json)
        return arreglo
