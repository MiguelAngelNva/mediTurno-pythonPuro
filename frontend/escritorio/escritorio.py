import tkinter as tk
from tkinter import ttk, messagebox
import json
import requests

# Configuración de módulos y rutas
MODULOS = {
    "comentarios": "modulos/comentarios/configuracion/config.json",
    "medicos": "modulos/medicos/configuracion/config.json",
    "ciudades": "modulos/ciudades/configuracion/config.json",
    "documentos": "modulos/documentos/configuracion/config.json",
    "estados": "modulos/estados/configuracion/config.json",
    "pacientes": "modulos/pacientes/configuracion/config.json",
    "sedes": "modulos/sedes/configuracion/config.json",
    "citas": "modulos/citas/configuracion/config.json",
    "notificadores": "modulos/notificadores/configuracion/config.json",
    "especialidades": "modulos/especialidades/configuracion/config.json",
    "medico_especialidad": "modulos/medico_especialidad/configuracion/config.json",
    "tipos_citas": "modulos/tipos_citas/configuracion/config.json"
}

def cargar_config(path):
    with open(path, encoding="utf-8") as f:
        config = json.load(f)
        return config["api_base"], config["endpoints"]

def listar_elementos(api, endpoint):
    try:
        r = requests.get(f"{api}{endpoint['read_all']}")
        if r.status_code == 200:
            return r.json()
        else:
            return [{"error": f"Status {r.status_code}"}]
    except Exception as e:
        return [{"error": str(e)}]

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestor de Módulos Mediturno")
        self.geometry("800x500")

        self.modulo_actual = None
        self.api = None
        self.endpoints = None

        self.crear_widgets()

    def crear_widgets(self):
        # Selector de módulo
        tk.Label(self, text="Módulo:", font=("Arial", 12)).pack(pady=5)
        self.modulo_var = tk.StringVar()
        modulos_lista = list(MODULOS.keys())
        self.selector = ttk.Combobox(self, textvariable=self.modulo_var, values=modulos_lista, state="readonly")
        self.selector.pack()

        self.selector.bind("<<ComboboxSelected>>", self.seleccionar_modulo)

        # Botones
        tk.Button(self, text="Listar elementos", command=self.mostrar_datos).pack(pady=10)

        # Vista de resultados
        self.tabla = tk.Text(self, wrap=tk.WORD, height=20)
        self.tabla.pack(expand=True, fill="both", padx=10, pady=10)

    def seleccionar_modulo(self, event=None):
        modulo = self.modulo_var.get()
        ruta = MODULOS.get(modulo)
        if not ruta:
            messagebox.showerror("Error", "Ruta de módulo no encontrada")
            return
        try:
            self.api, self.endpoints = cargar_config(ruta)
            self.modulo_actual = modulo
            messagebox.showinfo("Listo", f"Configuración cargada para '{modulo}'")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar el módulo: {e}")

    def mostrar_datos(self):
        if not self.api or not self.endpoints:
            messagebox.showwarning("Atención", "Primero selecciona un módulo válido.")
            return
        datos = listar_elementos(self.api, self.endpoints)
        self.tabla.delete(1.0, tk.END)
        for item in datos:
            self.tabla.insert(tk.END, json.dumps(item, indent=2, ensure_ascii=False) + "\n\n")

if __name__ == "__main__":
    app = App()
    app.mainloop()
