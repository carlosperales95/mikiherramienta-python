import tkinter as tk
from tkinter import ttk

from menu import MenuFrame
from bot_frame import ChatBotPage
from pass_frame import PasswordPage
from internet_frame import InternetTestPage

class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Mikiherramienta")
        self.geometry("600x600")

        left_container = tk.Frame(self, bg="blue")
        left_container.pack(side="left", fill="both", expand=True)
        left_container.grid_rowconfigure(0, weight=1)
        left_container.grid_columnconfigure(0, weight=1)

        right_container = tk.Frame(self, bg="black")
        right_container.pack(side="right", fill="both")
        right_container.grid_rowconfigure(0, weight=1)
        right_container.grid_columnconfigure(1, weight=1)

        menu = MenuFrame(right_container, self)
        menu.pack(side="right", fill="both")

        self.frames = {}
        for F in (ChatBotPage, PasswordPage, InternetTestPage):
            frame = F(left_container, self)
            self.frames[F] = frame
            frame.grid(row=0, sticky="wens", padx=(60, 60), pady=60)
        self.show_frame(ChatBotPage)

    def show_frame(self, id):
        frame = self.frames[id]
        frame.tkraise()

root = tkinterApp()
root.mainloop()