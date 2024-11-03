import tkinter as tk
from tkinter import ttk

class PasswordPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Elegir opciones de contraseña:")
        label.pack(side="top")

        symbol_box = ttk.Checkbutton(self, text="Simbolos")
        symbol_box.pack(pady=10)

        mayus_box = ttk.Checkbutton(self, text="Mayusculas")
        mayus_box.pack(pady=10)

        pl = tk.IntVar()

        pass_len = tk.Scale(self, from_=5, to=30, variable=pl, orient=tk.HORIZONTAL)
        pass_len.pack(pady=10)

        gen_btn = ttk.Button(self, text="Generar")
        gen_btn.pack(pady=10)
