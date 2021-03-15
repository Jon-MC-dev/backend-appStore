from entidades.producto import Producto

class Venta:
    def __init__(self, conexion, detalle):
        self.conexion = conexion
        self.detalle = detalle
        self.producto = Producto(conexion)

    def detalles(self, detalles_json):
        self.json_detalles = detalles_json


    def insertar(self,id , id_usuario_empleado, id_persona_cliente, fecha_hora):
        fi = self.conexion.insetar_actualizar_eliminar("INSERT INTO tbl_ventas (id_venta, id_usuario_empleado, id_persona_cliente, fecha_hora, precio_total) VALUE('"+str(id)+"', '"+str(id_usuario_empleado)+"', '"+str(id_persona_cliente)+"', '"+fecha_hora+"', '0')")
        total = 0
        for detalle in self.json_detalles:
            self.producto.actualizarExistencias(detalle['id_producto'], - detalle['cantidad'])
            total += detalle['precio_venta'] * detalle['cantidad'];
            self.detalle.insertar(id, detalle['id_producto'], detalle['precio_venta'], detalle['cantidad'])
        self.actualizar(id, total)
        return fi

    def actualizar(self, id, precio_total):
        return self.conexion.insetar_actualizar_eliminar("UPDATE tbl_ventas SET precio_total='"+str(precio_total)+"' WHERE id_venta = "+str(id))


    def eliminar(self, id):
        return self.conexion.insetar_actualizar_eliminar("DELETE FROM tbl_ventas WHERE id_venta="+str(id))

    def getAll(self, id = 0):
        if id == 0:
            respuesta = self.conexion.traerRegistros("SELECT * FROM tbl_ventas")
        else:
            respuesta = self.conexion.traerRegistros("SELECT * FROM tbl_ventas WHERE id_venta="+str(id))
        arreglo = []
        for tupa_marca in respuesta:
            json ={'id_venta': tupa_marca[0], 'id_usuario_empleado': tupa_marca[1], 'id_persona_cliente': tupa_marca[2], 'fecha_hora': tupa_marca[3], 'precio_total': str(tupa_marca[4])}
            arreglo.append(json)
        return arreglo
