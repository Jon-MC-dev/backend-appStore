from entidades.producto import Producto

class Adquisicion:
    def __init__(self, conexion, detalle):
        self.conexion = conexion
        self.detalle = detalle
        self.producto = Producto(conexion)

    def detalles(self, detalles_json):
        self.json_detalles = detalles_json


    def insertar(self,id , id_persona, fecha_hora):
        fi = self.conexion.insetar_actualizar_eliminar("INSERT INTO tbl_adquisiciones (id_adquisicion, id_persona, fecha_hora, precio_total) VALUE('"+str(id)+"','"+str(id_persona)+"', '"+fecha_hora+"', 0)")
        total = 0
        for detalle in self.json_detalles:
            total += detalle['precio_compra'] * detalle['cantidad'];
            self.producto.actualizarPrecio(detalle['id_producto'], detalle['precio_venta'])
            self.producto.actualizarExistencias(detalle['id_producto'], detalle['cantidad'])
            self.detalle.insertar(id, detalle['id_producto'], detalle['precio_compra'], detalle['cantidad'])
        self.actualizar(id, total)
        return fi

    def actualizar(self, id, precio_total):
        return self.conexion.insetar_actualizar_eliminar("UPDATE tbl_adquisiciones SET precio_total='"+str(precio_total)+"' WHERE id_adquisicion = "+str(id))


    def eliminar(self, id):
        return self.conexion.insetar_actualizar_eliminar("DELETE FROM tbl_adquisiciones WHERE id_adquisicion="+str(id))

    def getAll(self, id = 0):
        if id == 0:
            respuesta = self.conexion.traerRegistros("SELECT * FROM tbl_adquisiciones")
        else:
            respuesta = self.conexion.traerRegistros("SELECT * FROM tbl_adquisiciones WHERE id_adquisicion="+str(id))
        arreglo = []
        for tupa_marca in respuesta:
            json ={'id_adquisicion': tupa_marca[0], 'id_persona': tupa_marca[1], 'fecha_hora': tupa_marca[2], 'precio_total': tupa_marca[3]}
            arreglo.append(json)
        return arreglo
