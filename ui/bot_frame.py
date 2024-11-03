import tkinter as tk
from tkinter import ttk

class ChatBotPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label = ttk.Label(self, text="Empieza a hablar con el bot!")
        # label.pack()
        chat_history = tk.Frame(self)
        chat_history.pack(side="top", expand=True, fill=tk.X)
        scrollbar = ttk.Scrollbar(chat_history)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        mylist = tk.Listbox(chat_history, yscrollcommand=scrollbar.set)

        for line in range(100):
            mylist.insert(tk.END, 'This is line number' + str(line))
            
        mylist.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=mylist.yview)

        chat_input = tk.Frame(self)
        chat_input.pack(side="bottom", expand=True, fill=tk.X)

        l1 = ttk.Label(chat_input, text='You: ')
        l1.pack(side="left")
        e1 = ttk.Entry(chat_input)
        e1.pack(side="right", expand=True, fill=tk.X, padx=10)