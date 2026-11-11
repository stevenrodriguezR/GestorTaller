from backend_excel import BackendExcel
from excepciones_taller import ErrorValidacionException


class GestorTaller:
    def __init__(self):
        self.backend = BackendExcel()

    def registrar_cliente(self, cedula, nombre, telefono, direccion):
        if not cedula or not nombre:
            raise ErrorValidacionException("La cédula y el nombre son obligatorios.")

        clientes = self.backend.leer_datos("Clientes")
        for c in clientes:
            if str(c[0]) == str(cedula):
                raise ErrorValidacionException("Ya existe un cliente con esa cédula.")

        return self.backend.escribir_dato("Clientes", [cedula, nombre, telefono, direccion])

    def obtener_clientes(self):
        return self.backend.leer_datos("Clientes")

    def registrar_vehiculo(self, placa, marca, modelo, anio, cedula_propietario):
        if not placa or not cedula_propietario:
            raise ErrorValidacionException("La placa y la cédula del propietario son obligatorias.")
        return self.backend.escribir_dato("Vehiculos", [placa, marca, modelo, anio, cedula_propietario])

    def obtener_vehiculos(self):
        return self.backend.leer_datos("Vehiculos")

    def registrar_orden(self, id_orden, placa, fallo, estado, costo):
        try:
            costo_float = float(costo)
        except ValueError:
            raise ErrorValidacionException("El costo debe ser un valor numérico válido.")

        return self.backend.escribir_dato("Ordenes", [id_orden, placa, fallo, estado, costo_float])

    def obtener_ordenes(self):
        return self.backend.leer_datos("Ordenes")