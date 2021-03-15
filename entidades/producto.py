class Producto:
    def __init__(self, conexion):
        self.conexion = conexion


    def insertar(self, id_categoria, id_marca, modelo, existencias, precio, descripcion, codigo_barras, detalles_adicionales):
        return self.conexion.insetar_actualizar_eliminar("INSERT INTO tbl_productos (id_categoria, id_marca, modelo, existencias, precio, descripcion, codigo_barras, detalles_adicionales) VALUE('"+str(id_categoria)+"', '"+str(id_marca)+"', '"+modelo+"', '"+str(existencias)+"', '"+str(precio)+"', '"+descripcion+"', '"+codigo_barras+"', '"+detalles_adicionales+"')")


    def actualizar(self, id, id_categoria, id_marca, modelo, existencias, precio, descripcion, codigo_barras, detalles_adicionales):
        return self.conexion.insetar_actualizar_eliminar("UPDATE tbl_productos SET id_categoria='"+str(id_categoria)+"', id_marca='"+str(id_marca)+"', modelo='"+modelo+"', existencias='"+str(existencias)+"', precio='"+str(precio)+"', descripcion='"+descripcion+"', codigo_barras='"+codigo_barras+"', detalles_adicionales='"+detalles_adicionales+"' WHERE id_producto = "+str(id))


    def actualizarPrecio(self, id, precio):
        return self.conexion.insetar_actualizar_eliminar("UPDATE tbl_productos SET precio="+str(precio)+" WHERE id_producto = "+str(id))


    def actualizarExistencias(self, id, existencias):
        return self.conexion.insetar_actualizar_eliminar("UPDATE tbl_productos SET existencias=existencias + "+str(existencias)+"  WHERE id_producto = "+str(id))


    def eliminar(self, id):
        return self.conexion.insetar_actualizar_eliminar("DELETE FROM tbl_productos WHERE id_producto="+str(id))

    def getAll(self, id = 0):
        if id == 0:
            respuesta = self.conexion.traerRegistros("SELECT * FROM tbl_productos")
        else:
            respuesta = self.conexion.traerRegistros("SELECT * FROM tbl_productos WHERE id_producto="+str(id))
        arreglo = []
        for tupa_marca in respuesta:
            json ={'id_producto':tupa_marca[0], 'id_categoria':tupa_marca[1], 'id_marca':tupa_marca[2], 'modelo':tupa_marca[3], 'existencias':tupa_marca[4], 'descripcion':tupa_marca[5], 'codigo_barras':tupa_marca[6], 'detalles_adicionales':tupa_marca[7]}
            arreglo.append(json)
        return arreglo
