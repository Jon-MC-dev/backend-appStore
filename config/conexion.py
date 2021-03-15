from flaskext.mysql import MySQL
class Conexion:

    def __init__(self, app):
        self.numeroConsultas = 0;
        app.config['MYSQL_DATABASE_USER'] = 'root'
        app.config['MYSQL_DATABASE_PASSWORD'] = ''
        app.config['MYSQL_DATABASE_DB'] = 'bd_app'
        app.config['MYSQL_DATABASE_HOST'] = 'localhost'
        self.mysql = MySQL()
        self.mysql.init_app(app)


    def conectar(self):
        self.numeroConsultas = self.numeroConsultas+1;
        print("NUMERO CONSULTAS: ["+str(self.numeroConsultas)+"]")
        self.conexion = self.mysql.connect() # conexion al SGDB
        self.cursor = self.conexion.cursor() # Obtener Cursor


    def desconectar(self):
        self.cursor.close()


    def insetar_actualizar_eliminar(self, sql):
        self.conectar()
        filas_afectadas = self.cursor.execute(sql)
        self.conexion.commit()
        self.desconectar()
        return filas_afectadas


    def traerRegistros(self,sql):
        self.conectar()
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        self.conexion.commit()
        self.desconectar()
        return data


    def getMaxID(self, tbl, campo):
        maxID = 0
        res = self.traerRegistros("SELECT MAX("+campo+") AS Maximo FROM "+tbl)
        if not res[0][0] is None:
             maxID = res[0][0]
        return maxID
