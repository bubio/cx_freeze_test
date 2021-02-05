#! env python
# -*- coding: utf-8 -*-

import tkinter as tk


class Application:
    def run(self):
        root = tk.Tk()

        button = tk.Button(root, text="Hello, Python3/Tkinter!!")
        button.pack()

        root.mainloop()
