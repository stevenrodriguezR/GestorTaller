import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import shutil
from gestor_taller import GestorTaller
from validador_datos import ValidadorDatos
from ventana_detalles import VentanaDetalles
from excepciones_taller import ErrorValidacionException

class AppTaller:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sistema de Gestión de Taller Mecánico")
        self.root.geometry("880x580")
        self.gestor = GestorTaller()

        self.crear_menu()
        self.crear_interfaz()
        self.cargar_datos_tablas()

    def crear_menu(self):
        barra_menu = tk.Menu(self.root)
        menu_archivo = tk.Menu(barra_menu, tearoff=0)
        menu_archivo.add_command(label="Exportar copia Excel", command=self.exportar_excel)
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Salir", command=self.root.quit)
        barra_menu.add_cascade(label="Archivo", menu=menu_archivo)

        menu_ayuda = tk.Menu(barra_menu, tearoff=0)
        menu_ayuda.add_command(label="Acerca de", command=self.mostrar_acerca_de)
        barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)

        self.root.config(menu=barra_menu)

    def crear_interfaz(self):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.tab_clientes = ttk.Frame(self.notebook)
        self.tab_vehiculos = ttk.Frame(self.notebook)
        self.tab_ordenes = ttk.Frame(self.notebook)

        self.notebook.add(self.tab_clientes, text="Clientes")
        self.notebook.add(self.tab_vehiculos, text="Vehículos")
        self.notebook.add(self.tab_ordenes, text="Órdenes de Trabajo")

        self.construir_tab_clientes()
        self.construir_tab_vehiculos()
        self.construir_tab_ordenes()

    def construir_tab_clientes(self):
        frame_form = ttk.LabelFrame(self.tab_clientes, text="Registro de Cliente", padding=10)
        frame_form.pack(fill=tk.X, padx=10, pady=5)

        ttk.Label(frame_form, text="Cédula:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_cedula = ttk.Entry(frame_form, width=22)
        self.entry_cedula.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame_form, text="Nombre:").grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.entry_nombre = ttk.Entry(frame_form, width=25)
        self.entry_nombre.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(frame_form, text="Teléfono:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_telefono = ttk.Entry(frame_form, width=22)
        self.entry_telefono.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frame_form, text="Dirección:").grid(row=1, column=2, padx=5, pady=5, sticky="w")
        self.entry_direccion = ttk.Entry(frame_form, width=25)
        self.entry_direccion.grid(row=1, column=3, padx=5, pady=5)

        frame_botones = ttk.Frame(frame_form)
        frame_botones.grid(row=2, column=0, columnspan=4, pady=10)

        ttk.Button(frame_botones, text="Guardar Cliente", command=self.guardar_cliente).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_botones, text="Eliminar Seleccionado", command=self.eliminar_cliente).pack(side=tk.LEFT, padx=5)

        self.tree_clientes = ttk.Treeview(self.tab_clientes, columns=("Cedula", "Nombre", "Telefono", "Direccion"), show="headings")
        self.tree_clientes.heading("Cedula", text="Cédula")
        self.tree_clientes.heading("Nombre", text="Nombre")
        self.tree_clientes.heading("Telefono", text="Teléfono")
        self.tree_clientes.heading("Direccion", text="Dirección")
        self.tree_clientes.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.tree_clientes.bind("<Double-1>", self.ver_detalle_cliente)

    def construir_tab_vehiculos(self):
        frame_form = ttk.LabelFrame(self.tab_vehiculos, text="Registro de Vehículo", padding=10)
        frame_form.pack(fill=tk.X, padx=10, pady=5)

        ttk.Label(frame_form, text="Placa:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_placa = ttk.Entry(frame_form, width=18)
        self.entry_placa.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame_form, text="Marca:").grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.combo_marca = ttk.Combobox(frame_form, values=["Chevrolet", "Mazda", "Renault", "Toyota", "Honda", "Ford", "Otro"], width=18)
        self.combo_marca.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(frame_form, text="Modelo:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_modelo = ttk.Entry(frame_form, width=18)
        self.entry_modelo.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frame_form, text="Año:").grid(row=1, column=2, padx=5, pady=5, sticky="w")
        self.entry_anio = ttk.Entry(frame_form, width=18)
        self.entry_anio.grid(row=1, column=3, padx=5, pady=5)

        ttk.Label(frame_form, text="Cédula Propietario:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.entry_prop_cedula = ttk.Entry(frame_form, width=18)
        self.entry_prop_cedula.grid(row=2, column=1, padx=5, pady=5)

        self.var_garantia = tk.BooleanVar()
        ttk.Checkbutton(frame_form, text="Vehículo en garantía", variable=self.var_garantia).grid(row=2, column=2, columnspan=2, padx=5, pady=5, sticky="w")

        frame_botones = ttk.Frame(frame_form)
        frame_botones.grid(row=3, column=0, columnspan=4, pady=10)

        ttk.Button(frame_botones, text="Guardar Vehículo", command=self.guardar_vehiculo).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_botones, text="Eliminar Seleccionado", command=self.eliminar_vehiculo).pack(side=tk.LEFT, padx=5)

        self.tree_vehiculos = ttk.Treeview(self.tab_vehiculos, columns=("Placa", "Marca", "Modelo", "Anio", "Propietario"), show="headings")
        self.tree_vehiculos.heading("Placa", text="Placa")
        self.tree_vehiculos.heading("Marca", text="Marca")
        self.tree_vehiculos.heading("Modelo", text="Modelo")
        self.tree_vehiculos.heading("Anio", text="Año")
        self.tree_vehiculos.heading("Propietario", text="Cédula Propietario")
        self.tree_vehiculos.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

    def construir_tab_ordenes(self):
        frame_form = ttk.LabelFrame(self.tab_ordenes, text="Gestión de Órdenes de Trabajo", padding=10)
        frame_form.pack(fill=tk.X, padx=10, pady=5)

        ttk.Label(frame_form, text="ID Orden:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_id_orden = ttk.Entry(frame_form, width=18)
        self.entry_id_orden.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame_form, text="Placa Vehículo:").grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.entry_orden_placa = ttk.Entry(frame_form, width=18)
        self.entry_orden_placa.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(frame_form, text="Descripción Fallo:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_fallo = ttk.Entry(frame_form, width=45)
        self.entry_fallo.grid(row=1, column=1, columnspan=3, padx=5, pady=5, sticky="w")

        ttk.Label(frame_form, text="Costo ($):").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.entry_costo = ttk.Entry(frame_form, width=18)
        self.entry_costo.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(frame_form, text="Estado:").grid(row=2, column=2, padx=5, pady=5, sticky="w")
        frame_radio = ttk.Frame(frame_form)
        frame_radio.grid(row=2, column=3, padx=5, pady=5, sticky="w")

        self.var_estado = tk.StringVar(value="Pendiente")
        ttk.Radiobutton(frame_radio, text="Pendiente", variable=self.var_estado, value="Pendiente").pack(side=tk.LEFT)
        ttk.Radiobutton(frame_radio, text="En Proceso", variable=self.var_estado, value="En Proceso").pack(side=tk.LEFT)
        ttk.Radiobutton(frame_radio, text="Finalizado", variable=self.var_estado, value="Finalizado").pack(side=tk.LEFT)

        frame_botones = ttk.Frame(frame_form)
        frame_botones.grid(row=3, column=0, columnspan=4, pady=10)

        ttk.Button(frame_botones, text="Registrar Orden", command=self.guardar_orden).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_botones, text="Eliminar Seleccionada", command=self.eliminar_orden).pack(side=tk.LEFT, padx=5)

        self.tree_ordenes = ttk.Treeview(self.tab_ordenes, columns=("ID", "Placa", "Fallo", "Estado", "Costo"), show="headings")
        self.tree_ordenes.heading("ID", text="ID Orden")
        self.tree_ordenes.heading("Placa", text="Placa")
        self.tree_ordenes.heading("Fallo", text="Descripción Fallo")
        self.tree_ordenes.heading("Estado", text="Estado")
        self.tree_ordenes.heading("Costo", text="Costo")
        self.tree_ordenes.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.tree_ordenes.bind("<Double-1>", self.ver_detalle_orden)

    def guardar_cliente(self):
        try:
            cedula = self.entry_cedula.get()
            nombre = self.entry_nombre.get()
            telefono = self.entry_telefono.get()
            direccion = self.entry_direccion.get()

            if not ValidadorDatos.validar_no_vacio(cedula, nombre):
                raise ErrorValidacionException("Cédula y nombre son obligatorios.")

            self.gestor.registrar_cliente(cedula, nombre, telefono, direccion)
            messagebox.showinfo("Éxito", "Cliente registrado correctamente.")
            self.limpiar_campos_cliente()
            self.cargar_datos_tablas()
        except ErrorValidacionException as e:
            messagebox.showwarning("Validación", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")

    def eliminar_cliente(self):
        seleccion = self.tree_clientes.selection()
        if not seleccion:
            messagebox.showwarning("Atención", "Seleccione un cliente de la tabla.")
            return
        item = self.tree_clientes.item(seleccion[0])
        cedula = item["values"][0]
        if messagebox.askyesno("Confirmar", f"¿Eliminar el cliente con cédula {cedula}?"):
            self.gestor.backend.eliminar_dato("Clientes", cedula)
            self.cargar_datos_tablas()

    def ver_detalle_cliente(self, event):
        seleccion = self.tree_clientes.selection()
        if seleccion:
            valores = self.tree_clientes.item(seleccion[0])["values"]
            datos = {
                "Cédula": valores[0],
                "Nombre": valores[1],
                "Teléfono": valores[2],
                "Dirección": valores[3]
            }
            VentanaDetalles(self.root, "Detalle del Cliente", datos)

    def guardar_vehiculo(self):
        try:
            placa = self.entry_placa.get().upper()
            marca = self.combo_marca.get()
            modelo = self.entry_modelo.get()
            anio = self.entry_anio.get()
            cedula_prop = self.entry_prop_cedula.get()

            if not ValidadorDatos.validar_placa(placa):
                raise ErrorValidacionException("Ingrese una placa válida (mínimo 5 caracteres).")

            self.gestor.registrar_vehiculo(placa, marca, modelo, anio, cedula_prop)
            messagebox.showinfo("Éxito", "Vehículo registrado correctamente.")
            self.limpiar_campos_vehiculo()
            self.cargar_datos_tablas()
        except ErrorValidacionException as e:
            messagebox.showwarning("Validación", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")

    def eliminar_vehiculo(self):
        seleccion = self.tree_vehiculos.selection()
        if not seleccion:
            messagebox.showwarning("Atención", "Seleccione un vehículo de la tabla.")
            return
        placa = self.tree_vehiculos.item(seleccion[0])["values"][0]
        if messagebox.askyesno("Confirmar", f"¿Eliminar el vehículo de placa {placa}?"):
            self.gestor.backend.eliminar_dato("Vehiculos", placa)
            self.cargar_datos_tablas()

    def guardar_orden(self):
        try:
            id_orden = self.entry_id_orden.get()
            placa = self.entry_orden_placa.get().upper()
            fallo = self.entry_fallo.get()
            estado = self.var_estado.get()
            costo = self.entry_costo.get()

            if not ValidadorDatos.validar_no_vacio(id_orden, placa, fallo, costo):
                raise ErrorValidacionException("Todos los campos de la orden son obligatorios.")

            self.gestor.registrar_orden(id_orden, placa, fallo, estado, costo)
            messagebox.showinfo("Éxito", "Orden de trabajo registrada.")
            self.limpiar_campos_orden()
            self.cargar_datos_tablas()
        except ErrorValidacionException as e:
            messagebox.showwarning("Validación", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")

    def eliminar_orden(self):
        seleccion = self.tree_ordenes.selection()
        if not seleccion:
            messagebox.showwarning("Atención", "Seleccione una orden de la tabla.")
            return
        id_orden = self.tree_ordenes.item(seleccion[0])["values"][0]
        if messagebox.askyesno("Confirmar", f"¿Eliminar la orden {id_orden}?"):
            self.gestor.backend.eliminar_dato("Ordenes", id_orden)
            self.cargar_datos_tablas()

    def ver_detalle_orden(self, event):
        seleccion = self.tree_ordenes.selection()
        if seleccion:
            valores = self.tree_ordenes.item(seleccion[0])["values"]
            datos = {
                "ID Orden": valores[0],
                "Placa Vehículo": valores[1],
                "Fallo Reportado": valores[2],
                "Estado Actual": valores[3],
                "Costo Estimado": f"${valores[4]}"
            }
            VentanaDetalles(self.root, "Detalle de Orden de Trabajo", datos)

    def cargar_datos_tablas(self):
        for item in self.tree_clientes.get_children():
            self.tree_clientes.delete(item)
        for fila in self.gestor.obtener_clientes():
            self.tree_clientes.insert("", tk.END, values=fila)

        for item in self.tree_vehiculos.get_children():
            self.tree_vehiculos.delete(item)
        for fila in self.gestor.obtener_vehiculos():
            self.tree_vehiculos.insert("", tk.END, values=fila)

        for item in self.tree_ordenes.get_children():
            self.tree_ordenes.delete(item)
        for fila in self.gestor.obtener_ordenes():
            self.tree_ordenes.insert("", tk.END, values=fila)

    def limpiar_campos_cliente(self):
        self.entry_cedula.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_telefono.delete(0, tk.END)
        self.entry_direccion.delete(0, tk.END)

    def limpiar_campos_vehiculo(self):
        self.entry_placa.delete(0, tk.END)
        self.combo_marca.set("")
        self.entry_modelo.delete(0, tk.END)
        self.entry_anio.delete(0, tk.END)
        self.entry_prop_cedula.delete(0, tk.END)

    def limpiar_campos_orden(self):
        self.entry_id_orden.delete(0, tk.END)
        self.entry_orden_placa.delete(0, tk.END)
        self.entry_fallo.delete(0, tk.END)
        self.entry_costo.delete(0, tk.END)

    def exportar_excel(self):
        destino = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Archivos Excel", "*.xlsx")])
        if destino:
            try:
                shutil.copy(self.gestor.backend.nombre_archivo, destino)
                messagebox.showinfo("Exportar", "Copia del archivo Excel guardada exitosamente.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo exportar el archivo: {e}")

    def mostrar_acerca_de(self):
        messagebox.showinfo("Acerca de", "Gestor de Taller Mecánico v1.0\nProgramación II")

    def iniciar(self):
        self.root.mainloop()