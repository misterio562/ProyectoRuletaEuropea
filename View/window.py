import tkinter as tk
from rulette.ruleta import Rulette
from rulette.mesa import Mesa
from Entity.player import Player

class Ventana:
    def __init__(self, titulo):
        self.root = tk.Tk()
        self.root.title(titulo)

        self.root.geometry("1200x500")

    def mostrar(self):
        rulette = Rulette(self.root)
        rulette.printRulette()

        mesa = Mesa(self.root)
        

        player = Player()

        

        self.root.mainloop()
