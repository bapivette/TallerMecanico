class Usuario:
    def __init__(self, usuario_id=None, nombre="", username="", password="", perfil=""):
        self.usuario_id = usuario_id
        self.nombre = nombre
        self.username = username
        self.password = password
        self.perfil = perfil

    def to_dict(self):
        return {
            'usuario_id': self.usuario_id,
            'nombre': self.nombre,
            'username': self.username,
            'password': self.password,
            'perfil': self.perfil
        }
