import tkinter as tk
from tkinter import ttk

from bot_frame import ChatBotPage
from pass_frame import PasswordPage
from internet_frame import InternetTestPage

class MenuFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        b1 = ttk.Button(self, text="Chat con Bot",
            command= lambda : controller.show_frame(ChatBotPage))
        b2 = ttk.Button(self, text="Generador de contraseñas",
            command= lambda : controller.show_frame(PasswordPage))
        b3 = ttk.Button(self, text="Prueba de internet",
            command= lambda : controller.show_frame(InternetTestPage))

        b1.grid(row=0, column=1, sticky="w", pady=2)
        b2.grid(row=1, column=1, sticky="w", pady=2)
        b3.grid(row=2, column=1, sticky="w", pady=2)