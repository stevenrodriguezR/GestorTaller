import tkinter as tk
from tkinter import ttk

class VentanaDetalles(tk.Toplevel):
    def __init__(self, master, titulo, datos_dict):
        super().__init__(master)
        self.title(titulo)
        self.geometry("380x280")
        self.resizable(False, False)

        frame_principal = ttk.Frame(self, padding=20)
        frame_principal.pack(fill=tk.BOTH, expand=True)

        ttk.Label(frame_principal, text=titulo, font=("Arial", 12, "bold")).pack(pady=(0, 15))

        for clave, valor in datos_dict.items():
            fila = ttk.Frame(frame_principal)
            fila.pack(fill=tk.X, pady=4)
            ttk.Label(fila, text=f"{clave}:", font=("Arial", 10, "bold"), width=18, anchor="w").pack(side=tk.LEFT)
            ttk.Label(fila, text=str(valor), font=("Arial", 10), anchor="w").pack(side=tk.LEFT, fill=tk.X, expand=True)

        ttk.Button(frame_principal, text="Cerrar", command=self.destroy).pack(pady=(20, 0))