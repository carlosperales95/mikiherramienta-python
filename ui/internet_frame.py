import tkinter as tk
from tkinter import ttk

class InternetTestPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Elegir opciones de test de internet:")
        label.pack(side="top")

        upload_box = ttk.Checkbutton(self, text="Subida")
        upload_box.pack(pady=10)

        download_box = ttk.Checkbutton(self, text="Descarga")
        download_box.pack(pady=10)

        ping_box = ttk.Checkbutton(self, text="Ping")
        ping_box.pack(pady=10)

        test_btn = ttk.Button(self, text="Test")
        test_btn.pack(pady=10)
