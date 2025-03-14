from .conexion import Conexion

class DbUsuario:

    def save(self, usuario):
        con = Conexion()
        conn = con.open()
        cursor = conn.cursor()
        sql = "INSERT INTO usuarios (nombre, username, password, perfil) VALUES (%s, %s, %s, %s)"
        datos = (usuario['nombre'], usuario['username'], usuario['password'], usuario['perfil'])
        cursor.execute(sql, datos)
        conn.commit()
        conn.close()

    def search(self, usuario_id):
        con = Conexion()
        conn = con.open()
        cursor = conn.cursor()
        sql = f"SELECT * FROM usuarios WHERE usuario_id={usuario_id}"
        cursor.execute(sql)
        row = cursor.fetchone()
        conn.close()
        if row:
            return {
                'usuario_id': row[0],
                'nombre': row[1],
                'username': row[2],
                'password': row[3],
                'perfil': row[4]
            }
        return None

    def edit(self, usuario):
        con = Conexion()
        conn = con.open()
        cursor = conn.cursor()
        sql = f"UPDATE usuarios SET nombre=%s, username=%s, perfil=%s WHERE usuario_id=%s"
        datos = (usuario['nombre'], usuario['username'], usuario['perfil'], usuario['usuario_id'])
        cursor.execute(sql, datos)
        conn.commit()
        conn.close()

    def remove(self, usuario_id):
        con = Conexion()
        conn = con.open()
        cursor = conn.cursor()
        sql = f"DELETE FROM usuarios WHERE usuario_id={usuario_id}"
        cursor.execute(sql)
        conn.commit()
        conn.close()

    def authenticate(self, username, password):
        con = Conexion()
        conn = con.open()
        cursor = conn.cursor()
        sql = "SELECT * FROM usuarios WHERE username=%s"
        cursor.execute(sql, (username,))
        row = cursor.fetchone()
        conn.close()
        if row and row[3] == password:
            return {
                'usuario_id': row[0],
                'nombre': row[1],
                'username': row[2],
                'perfil': row[4]
            }
        return None
