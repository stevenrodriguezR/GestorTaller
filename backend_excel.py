import os
import openpyxl


class BackendExcel:
    def __init__(self, nombre_archivo="taller_mecanico.xlsx"):
        self.nombre_archivo = nombre_archivo
        self.inicializar_archivo()

    def inicializar_archivo(self):
        if not os.path.exists(self.nombre_archivo):
            wb = openpyxl.Workbook()
            ws_clientes = wb.active
            ws_clientes.title = "Clientes"
            ws_clientes.append(["Cédula", "Nombre", "Teléfono", "Dirección"])

            ws_vehiculos = wb.create_sheet(title="Vehiculos")
            ws_vehiculos.append(["Placa", "Marca", "Modelo", "Año", "Cédula Propietario"])

            ws_ordenes = wb.create_sheet(title="Ordenes")
            ws_ordenes.append(["ID Orden", "Placa Vehículo", "Descripción Fallo", "Estado", "Costo"])

            wb.save(self.nombre_archivo)

    def leer_datos(self, hoja):
        wb = openpyxl.load_workbook(self.nombre_archivo)
        if hoja in wb.sheetnames:
            ws = wb[hoja]
            datos = []
            for fila in ws.iter_rows(min_row=2, values_only=True):
                if any(fila):
                    datos.append(fila)
            return datos
        return []

    def escribir_dato(self, hoja, registro):
        wb = openpyxl.load_workbook(self.nombre_archivo)
        if hoja in wb.sheetnames:
            ws = wb[hoja]
            ws.append(registro)
            wb.save(self.nombre_archivo)
            return True
        return False

    def actualizar_dato(self, hoja, id_busqueda, nuevo_registro):
        wb = openpyxl.load_workbook(self.nombre_archivo)
        if hoja in wb.sheetnames:
            ws = wb[hoja]
            for fila in range(2, ws.max_row + 1):
                if str(ws.cell(row=fila, column=1).value) == str(id_busqueda):
                    for col, valor in enumerate(nuevo_registro, start=1):
                        ws.cell(row=fila, column=col, value=valor)
                    wb.save(self.nombre_archivo)
                    return True
        return False

    def eliminar_dato(self, hoja, id_busqueda):
        wb = openpyxl.load_workbook(self.nombre_archivo)
        if hoja in wb.sheetnames:
            ws = wb[hoja]
            for fila in range(2, ws.max_row + 1):
                if str(ws.cell(row=fila, column=1).value) == str(id_busqueda):
                    ws.delete_rows(fila)
                    wb.save(self.nombre_archivo)
                    return True
        return False