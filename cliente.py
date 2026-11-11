
class Cliente:
    def __init__(self, cedula, nombre, telefono, direccion):
        self.cedula = cedula
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion

    def obtener_info(self):
        return f"CC: {self.cedula} - Nombre: {self.nombre} - Tel: {self.telefono}"