
class Vehiculo:
    def __init__(self, placa, marca, modelo, anio, cedula_propietario):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.cedula_propietario = cedula_propietario

    def obtener_info_vehiculo(self):
        return f"Placa: {self.placa} | {self.marca} {self.modelo} ({self.anio})"