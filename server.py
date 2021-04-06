import os
from flask import Flask, request
from werkzeug.utils import secure_filename
import random


from config.conexion import Conexion
from entidades.marca import Marca
from entidades.categoria import Categoria
from entidades.color import Color
from entidades.persona import Persona
from entidades.usuario import Usuario
from entidades.producto import Producto
from entidades.fotografia import Fotografia
from entidades.venta import Venta
from entidades.detalle_venta import DetalleVenta
from entidades.adqisicion import Adquisicion
from entidades.detalle_adquisicion import DetalleAdquisicion

app = Flask(__name__)
conexion = Conexion(app, True)
#
marca = Marca(Conexion(app, True))
categoria = Categoria(Conexion(app, True))
color = Color(conexion)
persona = Persona(conexion)
usuario = Usuario(conexion)
producto = Producto(Conexion(app, True))
fotografia = Fotografia(conexion)
venta = Venta(conexion, DetalleVenta(conexion))
adquisicion = Adquisicion(conexion, DetalleAdquisicion(conexion))


@app.route('/')
def hello_world():
    return 'Hello, World!'

# Operaciones Marca
@app.route('/marca', methods=['GET','POST','PUT','DELETE'])
def operaciones_marca():
    if request.is_json:
        jsonDatos = request.get_json()
        if request.method == 'POST':
            return {"filas_afectadas": marca.insertar(jsonDatos['nombre'])}
        elif request.method == 'PUT':
            return {"filas_afectadas": marca.actualizar(jsonDatos['nombre'],jsonDatos['id'])}
    else:
        if request.method == 'GET':
            return {"datos": marca.getAll(int(request.args.get('id')))}
        elif request.method == 'DELETE':
            return {"filas_afectadas": marca.eliminar(request.headers['id'])}
        else:
            return 'No es un json'

    return 'Operaciones crud de marca'


# Operaciones Categoria
@app.route('/categoria', methods=['GET','POST','PUT','DELETE'])
def operaciones_categoria():
    if request.is_json:
        jsonDatos = request.get_json()
        if request.method == 'POST':
            return {"filas_afectadas": categoria.insertar(jsonDatos['nombre'])}
        if request.method == 'PUT':
            return {"filas_afectadas": categoria.actualizar(jsonDatos['nombre'],jsonDatos['id'])}
    else:
        if request.method == 'GET':
            return {"datos":categoria.getAll(int(request.args.get('id')))}
        elif request.method == 'DELETE':
            return {"filas_afectadas": categoria.eliminar(request.headers['id'])}

        return 'No es un json'

    return 'Operaciones crud de categoria'



# Operaciones colores
@app.route('/color', methods=['GET','POST','PUT','DELETE'])
def operaciones_color():
    if request.is_json:
        jsonDatos = request.get_json()
        if request.method == 'POST':
            return {"filas_afectadas": color.insertar(jsonDatos['color'], jsonDatos['codigo'])}
        elif request.method == 'PUT':
            return {"filas_afectadas": color.actualizar(jsonDatos['color'], jsonDatos['id'], jsonDatos['codigo'])}
    else:
        if request.method == 'GET':
            return {"datos":color.getAll(int(request.args.get('id')))}
        elif request.method == 'DELETE':
            return {"filas_afectadas": color.eliminar(request.headers['id'])}

        return 'No es un json'

    return 'Operaciones crud de colores'



# Operaciones Persona
@app.route('/persona', methods=['GET','POST','PUT','DELETE'])
def operaciones_persona():
    if request.is_json:
        jsonDatos = request.get_json()
        if request.method == 'POST':
            return {"filas_afectadas": persona.insertar(jsonDatos['nombre'], jsonDatos['apellido_paterno'], jsonDatos['apellido_materno'], jsonDatos['fechaNaci'], jsonDatos['sexo'])}
        elif request.method == 'PUT':
            return {"filas_afectadas": persona.actualizar(jsonDatos['id'], jsonDatos['nombre'], jsonDatos['apellido_paterno'],jsonDatos['apellido_materno'],jsonDatos['fechaNaci'],jsonDatos['sexo'])}
    else:
        if request.method == 'GET':
            return {"datos":persona.getAll(int(request.args.get('id')))}
        elif request.method == 'DELETE':
            return {"filas_afectadas": persona.eliminar(request.headers['id'])}
        return 'No es un json'

    return 'Operaciones crud de persona'



# Operaciones Usuario
@app.route('/usuario', methods=['GET','POST','PUT','DELETE'])
def operaciones_usuario():
    if request.is_json:
        jsonDatos = request.get_json()
        if request.method == 'POST':
            return {"filas_afectadas": usuario.insertar(jsonDatos['id'], jsonDatos['usuario'], jsonDatos['contrasena'], jsonDatos['permisos'])}
        elif request.method == 'PUT':
            return {"filas_afectadas": usuario.actualizar(jsonDatos['id'], jsonDatos['usuario'], jsonDatos['contrasena'], jsonDatos['permisos'])}
    else:
        if request.method == 'GET':
            return {"datos": usuario.getAll(int(request.args.get('id')))}
        elif request.method == 'DELETE':
            return {"filas_afectadas": usuario.eliminar(request.headers['id'])}

        return 'No es un json'

    return 'Operaciones crud de usuario'


# Operaciones producto
@app.route('/producto', methods=['GET','POST','PUT','DELETE'])
def operaciones_producto():
    if request.is_json:
        jsonDatos = request.get_json()
        if request.method == 'POST':
            return {"filas_afectadas": producto.insertar(jsonDatos['id_categoria'], jsonDatos['id_marca'], jsonDatos['modelo'], jsonDatos['existencias'], jsonDatos['precio'], jsonDatos['descripcion'], jsonDatos['codigo_barras'], jsonDatos['detalles_adicionales'])}
        elif request.method == 'PUT':
            return {"filas_afectadas": producto.actualizar(jsonDatos['id'], jsonDatos['id_categoria'], jsonDatos['id_marca'], jsonDatos['modelo'], jsonDatos['existencias'], jsonDatos['descripcion'], jsonDatos['codigo_barras'], jsonDatos['detalles_adicionales'])}

    else:
        if request.method == 'GET':
            return {"datos": producto.getAll(int(request.args.get('id')))}
        elif request.method == 'DELETE':
            return {"filas_afectadas": producto.eliminar(request.headers['id'])}

        return 'No es un json'

    return 'Operaciones crud de producto'


# Operaciones fotografia
@app.route('/fotografia', methods=['GET','POST','PUT','DELETE'])
def operaciones_fotografia():
    if 'foto' in request.files:
        archivo = request.files['foto']
        nombre_archivo = secure_filename(archivo.filename)
        t = archivo.save(os.path.join("./archivos", str(random.randint(1, 1000)) + nombre_archivo))

        if request.method == 'POST':
            return {"filas_afectadas": fotografia.insertar(request.form['id_producto'], nombre_archivo, request.form['id_color'])}
        elif request.method == 'PUT':
            return {"filas_afectadas": fotografia.actualizar(request.form['id_fotografia'], request.form['id_producto'], nombre_archivo, request.form['id_color'])}
        elif request.method == 'DELETE':
            return {"filas_afectadas": fotografia.eliminar(request.form['id_fotografia'])}
        elif request.method == 'GET':
            return {"datos": fotografia.getAll(request.form['id_fotografia'])}


    else:
        return "No se ha recibido la foto"


    return "Listos para subir foto"
    #if request.is_json:
    #    jsonDatos = request.get_json()
    #    if request.method == 'POST':
    #        return {"filas_afectadas": fotografia.insertar(jsonDatos['id_producto'], jsonDatos['fotografia'], jsonDatos['id_color'])}
    #    elif request.method == 'PUT':
    #        return {"filas_afectadas": fotografia.actualizar(jsonDatos['id'], jsonDatos['id_producto'], jsonDatos['fotografia'], jsonDatos['id_color'])}
    #    elif request.method == 'DELETE':
    #        return {"filas_afectadas": fotografia.eliminar(jsonDatos['id'])}
    #    elif request.method == 'GET':
    #        return {"datos": fotografia.getAll(jsonDatos['id'])}
    #else:
    #    return 'No es un json'

    #return 'Operaciones crud de fotografia'


# Operaciones venta
@app.route('/venta', methods=['GET','POST','PUT','DELETE'])
def operaciones_venta():
    if request.is_json:
        jsonDatos = request.get_json()
        if request.method == 'POST':
            id_venta = conexion.getMaxID('tbl_ventas', 'id_venta') + 1;
            venta.detalles(jsonDatos['detalle'])
            return {"filas_afectadas": venta.insertar(id_venta, jsonDatos['id_usuario_empleado'], jsonDatos['id_persona_cliente'], jsonDatos['fecha_hora'])}

    else:
        if request.method == 'GET':
            return {"datos": venta.getAll(int(request.args.get('id')))}
        elif request.method == 'DELETE':
            return {"filas_afectadas": venta.eliminar(request.headers['id'])}

        return 'No es un json'

    return 'Operaciones crud de venta'


# Operaciones Adquisicion
@app.route('/adquisicion', methods=['GET','POST','PUT','DELETE'])
def operaciones_adquisicion():
    if request.is_json:
        jsonDatos = request.get_json()
        if request.method == 'POST':
            id_adquisicion = conexion.getMaxID('tbl_adquisiciones', 'id_adquisicion') + 1;
            adquisicion.detalles(jsonDatos['detalle'])
            return {"filas_afectadas": adquisicion.insertar(id_adquisicion, jsonDatos['id_persona'], jsonDatos['fecha_hora'])}

    else:
        if request.method == 'GET':
            return {"datos": adquisicion.getAll(int(request.args.get('id')))}
        elif request.method == 'DELETE':
            return {"filas_afectadas": adquisicion.eliminar(request.headers['id'])}

        return 'No es un json'

    return 'Operaciones crud de adquisicion'


@app.route('/maxID')
def getMaxID():
    if request.method == 'GET':
        return {"numMax": conexion.getMaxID(request.args.get('tbl'), request.args.get('campo'))}
    return 'getMaxID'


if __name__== '__main__':
    app.run(debug=True,host='0.0.0.0')
