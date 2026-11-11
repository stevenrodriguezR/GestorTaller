
class OrdenTrabajo:
    def __init__(self, id_orden, placa_vehiculo, descripcion_fallo, estado="Pendiente", costo=0.0):
        self.id_orden = id_orden
        self.placa_vehiculo = placa_vehiculo
        self.descripcion_fallo = descripcion_fallo
        self.estado = estado
        self.costo = costo

    def actualizar_estado(self, nuevo_estado):
        self.estado = nuevo_estado