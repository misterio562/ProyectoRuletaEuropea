import tkinter as tk
from tkinter import simpledialog
from Entity.apuesta import Apuesta
from Entity.player import Player
from rulette.datos_generales.number_colors import number_colors
from GestionRepositorio.repositorio_apuestas import RepositorioApuestasSingleton


class Mesa():

    row12_buttons = []
    row1324_buttons = []
    row118_buttons = []
    row2536_buttons = []
    even_buttons = []
    red_buttons = []
    black_buttons = []
    odd_buttons = []
    row1936_buttons = []
    cd_buttons = []
    cc_buttons = []
    ci_buttons = []

    # Crear una matriz 3x8 (3 filas y 12 columnas) inicializada con ceros
    matrix = [[0 for _ in range(12)] for _ in range(3)]

    # Ahora puedes asignar valores a elementos individuales de la matriz
    matrix[0][0] = 3
    matrix[0][1] = 6
    matrix[0][2] = 9
    matrix[0][3] = 12
    matrix[1][0] = 2
    matrix[1][1] = 5
    matrix[1][2] = 8
    matrix[1][3] = 11
    matrix[2][0] = 1
    matrix[2][1] = 4
    matrix[2][2] = 7
    matrix[2][3] = 10

    matrix[0][4] = 15
    matrix[0][5] = 18
    matrix[0][6] = 21
    matrix[0][7] = 24
    matrix[1][4] = 14
    matrix[1][5] = 17
    matrix[1][6] = 20
    matrix[1][7] = 23
    matrix[2][4] = 13
    matrix[2][5] = 16
    matrix[2][6] = 19
    matrix[2][7] = 22

    matrix[0][8] = 27
    matrix[0][9] = 30
    matrix[0][10] = 33
    matrix[0][11] = 36
    matrix[1][8] = 26
    matrix[1][9] = 29
    matrix[1][10] = 32
    matrix[1][11] = 35
    matrix[2][8] = 25
    matrix[2][9] = 28
    matrix[2][10] = 31
    matrix[2][11] = 34

    _instance = None  # Variable para almacenar la instancia única

    def __new__(cls, ventana):
        if cls._instance is None:
            cls._instance = super(Mesa, cls).__new__(cls)
            cls._instance.frame = tk.Frame(ventana, width=1000, height=600, padx=10)
            cls._instance.frame.place(x=440, y=150)
            cls._instance.fichas = []
            cls._instance.monto = 0

            cls._instance.player = Player()
            cls._instance.player.get_saldo()

            cls._instance.widget(ventana)
        return cls._instance

    def resetMonto(self):
        self.monto = 0
        self.lblMonto.config(text=f"Apuestas total {self.monto}")

    def actualizarMonto(self):
        self.lblDinero.config(text=f"Saldo {self.player.get_saldo()}")
        


    @classmethod
    def crearMesaSinParámetro(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
        return cls._instance


    def ingresarApuesta(self, ta, n=None, c=None):
        try:
            valor = simpledialog.askinteger("Apostando...", "Valor a apostar:")
            if valor is not None:
                self.crearApuesta(valor, n, c, ta)
            else:
                print("No se ingresó ningún valor entero.")
        except ValueError:
            print("Entrada no válida. Debes ingresar un número entero válido.")

    def crearApuesta(self, monto, n, c, ta):
        
        player = Player()
        player.set_saldo(player.get_saldo()-monto)
        self.actualizarMonto()
        apuesta = Apuesta(ta, monto)
        apuesta.crearApuesta(n, c)

        self.repositorio_apuestas = RepositorioApuestasSingleton()
        self.repositorio_apuestas.agregar_apuesta(apuesta)

        for apuesta in self.listApuestas():
            print(f"Tipo de apuestas: {apuesta.getTipoApuesta()}")
            print(f"Número apostado: {apuesta.getNumeroApostado()} ")
            print(f"Color: {apuesta.getColorApostado()}")
            print(f"Monto apostado: {apuesta.getMontoApostado()}")
            

        self.montoTotal()

    def listApuestas(self):
        return self.repositorio_apuestas.obtener_lista_apuestas()

    def sumarMontosApuestas(self):
        suma_montos = 0
        for apuesta in self.listApuestas():
            suma_montos += apuesta.getMontoApostado()  # Sumamos el monto de cada apuesta
        return suma_montos

    def montoTotal(self):
        self.monto = self.sumarMontosApuestas()
        self.lblMonto.config(text=f"Apuestas total {self.monto}")

    def widget(self, ventana):

        # Datos del jugador
        self.lblDinero = tk.Label(
            ventana, text=f"Saldo {self.player.get_saldo()}", font=("Helvetica", 30))
        self.lblDinero.place(x=500, y=10)

        self.lblMonto = tk.Label(
            ventana, text=f"Apuesta total {self.monto}", font=("Helvetica", 30))
        self.lblMonto.place(x=750, y=10)

        # Botones del tablero
        cero = tk.Button(self.frame, text="0", bg="green", width=3, height=5)
        cero.grid(row=1, column=0, rowspan=3)

        row0_button112 = tk.Button(
            self.frame, text="1 - 12", bg="lightblue", width=19, command=lambda c=None, n=None, ta="1-12": self.ingresarApuesta(ta, n, c))
        row0_button112.grid(row=0, column=1, columnspan=4, )
        row0_button112.bind("<Enter>", self.on_button112_hover)
        row0_button112.bind("<Leave>", self.on_button112_leave)

        row0_button1324 = tk.Button(
            self.frame, text="13 - 24", bg="lightblue", width=19, command=lambda c=None, n=None, ta="13-24": self.ingresarApuesta(ta, n, c))
        row0_button1324.grid(row=0, column=5, columnspan=4)
        row0_button1324.bind("<Enter>", self.on_button1324_hover)
        row0_button1324.bind("<Leave>", self.on_button1324_leave)

        row0_button2536 = tk.Button(
            self.frame, text="25 - 36", bg="lightblue", width=19, command=lambda c=None, n=None, ta="25-36": self.ingresarApuesta(ta, n, c))
        row0_button2536.grid(row=0, column=9, columnspan=4)
        row0_button2536.bind("<Enter>", self.on_button2536_hover)
        row0_button2536.bind("<Leave>", self.on_button2536_leave)

        row0_button118 = tk.Button(
            self.frame, text="1 - 18", bg="lightblue", width=8, command=lambda c=None, n=None, ta="1-18": self.ingresarApuesta(ta, n, c))
        row0_button118.grid(row=4, column=1, columnspan=2)
        row0_button118.bind("<Enter>", self.on_button118_hover)
        row0_button118.bind("<Leave>", self.on_button118_leave)

        even = tk.Button(self.frame, text="even", bg="lightblue", width=8, command=lambda c=None, n=None, ta="even": self.ingresarApuesta(ta, n, c))
        even.grid(row=4, column=3, columnspan=2)
        even.bind("<Enter>", self.on_buttoneven_hover)
        even.bind("<Leave>", self.on_buttoneven_leave)

        rombo_red_image = tk.PhotoImage(file="assets/rombored.png")
        red = tk.Button(self.frame, text="Red", bg="red", width=8, command=lambda c=None, n=None, ta="red": self.ingresarApuesta(ta, n, c))
        red.grid(row=4, column=5, columnspan=2)
        red.bind("<Enter>", self.on_buttonred_hover)
        red.bind("<Leave>", self.on_buttonred_leave)

        rombo_black_image = tk.PhotoImage(file="assets/romboblack.png")
        black = tk.Button(self.frame, text="black",
                          fg="white", bg="black", width=8, command=lambda c=None, n=None, ta="black": self.ingresarApuesta(ta, n, c))
        black.grid(row=4, column=7, columnspan=2)
        black.bind("<Enter>", self.on_buttonblack_hover)
        black.bind("<Leave>", self.on_buttonblack_leave)

        odd = tk.Button(self.frame, text="Odd", bg="lightblue", width=8, command=lambda c=None, n=None, ta="odd": self.ingresarApuesta(ta, n, c))
        odd.grid(row=4, column=9, columnspan=2)
        odd.bind("<Enter>", self.on_buttonodd_hover)
        odd.bind("<Leave>", self.on_buttonodd_leave)

        row0_button1936 = tk.Button(
            self.frame, text="19 - 36", bg="lightblue", width=8, command=lambda c=None, n=None, ta="19-36": self.ingresarApuesta(ta, n, c))
        row0_button1936.grid(row=4, column=11, columnspan=2)
        row0_button1936.bind("<Enter>", self.on_button1936_hover)
        row0_button1936.bind("<Leave>", self.on_button1936_leave)

        columna_derecha = tk.Button(
            self.frame, text="2to1", bg="lightblue", width=3, command=lambda c=None, n=None, ta="cd": self.ingresarApuesta(ta, n, c))
        columna_derecha.grid(row=1, column=13,)
        columna_derecha.bind("<Enter>", self.on_buttoncd_hover)
        columna_derecha.bind("<Leave>", self.on_buttoncd_leave)

        columna_central = tk.Button(
            self.frame, text="2to1", bg="lightblue", width=3, command=lambda c=None, n=None, ta="cc": self.ingresarApuesta(ta, n, c))
        columna_central.grid(row=2, column=13,)
        columna_central.bind("<Enter>", self.on_buttoncc_hover)
        columna_central.bind("<Leave>", self.on_buttoncc_leave)

        columna_izquierda = tk.Button(
            self.frame, text="2to1", bg="lightblue", width=3, command=lambda c=None, n=None, ta="ci": self.ingresarApuesta(ta, n, c))
        columna_izquierda.grid(row=3, column=13,)
        columna_izquierda.bind("<Enter>", self.on_buttonci_hover)
        columna_izquierda.bind("<Leave>", self.on_buttonci_leave)

        for row in range(3):
            for column in range(1, 13):
                number = Mesa.matrix[row][column-1]
                self.color_number = number_colors.get(number)
                button = tk.Button(self.frame, text=f"{number}", foreground="white", bg=self.color_number,
                                   command=lambda c=None, n=number, ta="numero": self.ingresarApuesta(ta, n, c ))
                button.grid(row=row+1, column=column)
                button.bind("<Button-1>")

                if column < 5:
                    Mesa.row12_buttons.append(button)

                if 4 < column < 9:
                    Mesa.row1324_buttons.append(button)

                if column < 7:
                    Mesa.row118_buttons.append(button)

                if 8 < column < 13:
                    Mesa.row2536_buttons.append(button)

                if number % 2 == 0:
                    Mesa.even_buttons.append(button)

                if self.color_number == "red":
                    Mesa.red_buttons.append(button)

                if self.color_number == "black":
                    Mesa.black_buttons.append(button)

                if number % 2 != 0:
                    Mesa.odd_buttons.append(button)

                if 6 < column < 13:
                    Mesa.row1936_buttons.append(button)

                if row == 0:
                    Mesa.cd_buttons.append(button)

                if row == 1:
                    Mesa.cc_buttons.append(button)

                if row == 2:
                    Mesa.ci_buttons.append(button)

    def on_button112_hover(self, event):
        for button in Mesa.row12_buttons:
            button.config(borderwidth=3, highlightbackground="gray",
                          bg="white smoke", fg="gray")

    def on_button112_leave(self, event):
        for button in Mesa.row12_buttons:
            button_number = int(button.cget("text"))
            button.config(bg=number_colors.get(button_number),
                          fg="white", borderwidth=0, highlightbackground="white")

    def on_button1324_hover(self, event):
        for button in Mesa.row1324_buttons:
            button.config(borderwidth=3, highlightbackground="gray",
                          bg="white smoke", fg="gray")

    def on_button1324_leave(self, event):
        for button in Mesa.row1324_buttons:
            button_number = int(button.cget("text"))
            button.config(bg=number_colors.get(button_number),
                          fg="white", borderwidth=0, highlightbackground="white")

    def on_button118_hover(self, event):
        for button in Mesa.row118_buttons:
            button.config(borderwidth=3, highlightbackground="gray",
                          bg="white smoke", fg="gray")

    def on_button118_leave(self, event):
        for button in Mesa.row118_buttons:
            button_number = int(button.cget("text"))
            button.config(bg=number_colors.get(button_number),
                          fg="white", borderwidth=0, highlightbackground="white")

    def on_button2536_hover(self, event):
        for button in Mesa.row2536_buttons:
            button.config(borderwidth=3, highlightbackground="gray",
                          bg="white smoke", fg="gray")

    def on_button2536_leave(self, event):
        for button in Mesa.row2536_buttons:
            button_number = int(button.cget("text"))
            button.config(bg=number_colors.get(button_number),
                          fg="white", borderwidth=0, highlightbackground="white")

    def on_buttoneven_hover(self, event):
        for button in Mesa.even_buttons:
            button.config(borderwidth=3, highlightbackground="gray",
                          bg="white smoke", fg="gray")

    def on_buttoneven_leave(self, event):
        for button in Mesa.even_buttons:
            button_number = int(button.cget("text"))
            button.config(bg=number_colors.get(button_number),
                          fg="white", borderwidth=0, highlightbackground="white")

    def on_buttonred_hover(self, event):
        for button in Mesa.red_buttons:
            button.config(borderwidth=3, highlightbackground="gray",
                          bg="white smoke", fg="gray")

    def on_buttonred_leave(self, event):
        for button in Mesa.red_buttons:
            button_number = int(button.cget("text"))
            button.config(bg=number_colors.get(button_number),
                          fg="white", borderwidth=0, highlightbackground="white")

    def on_buttonblack_hover(self, event):
        for button in Mesa.black_buttons:
            button.config(borderwidth=3, highlightbackground="gray",
                          bg="white smoke", fg="gray")

    def on_buttonblack_leave(self, event):
        for button in Mesa.black_buttons:
            button_number = int(button.cget("text"))
            button.config(bg=number_colors.get(button_number),
                          fg="white", borderwidth=0, highlightbackground="white")

    def on_buttonodd_hover(self, event):
        for button in Mesa.odd_buttons:
            button.config(borderwidth=3, highlightbackground="gray",
                          bg="white smoke", fg="gray")

    def on_buttonodd_leave(self, event):
        for button in Mesa.odd_buttons:
            button_number = int(button.cget("text"))
            button.config(bg=number_colors.get(button_number),
                          fg="white", borderwidth=0, highlightbackground="white")

    def on_button1936_hover(self, event):
        for button in Mesa.row1936_buttons:
            button.config(borderwidth=3, highlightbackground="gray",
                          bg="white smoke", fg="gray")

    def on_button1936_leave(self, event):
        for button in Mesa.row1936_buttons:
            button_number = int(button.cget("text"))
            button.config(bg=number_colors.get(button_number),
                          fg="white", borderwidth=0, highlightbackground="white")

    def on_buttoncd_hover(self, event):
        for button in Mesa.cd_buttons:
            button.config(borderwidth=3, highlightbackground="gray",
                          bg="white smoke", fg="gray")

    def on_buttoncd_leave(self, event):
        for button in Mesa.cd_buttons:
            button_number = int(button.cget("text"))
            button.config(bg=number_colors.get(button_number),
                          fg="white", borderwidth=0, highlightbackground="white")

    def on_buttoncc_hover(self, event):
        for button in Mesa.cc_buttons:
            button.config(borderwidth=3, highlightbackground="gray",
                          bg="white smoke", fg="gray")

    def on_buttoncc_leave(self, event):
        for button in Mesa.cc_buttons:
            button_number = int(button.cget("text"))
            button.config(bg=number_colors.get(button_number),
                          fg="white", borderwidth=0, highlightbackground="white")

    def on_buttonci_hover(self, event):
        for button in Mesa.ci_buttons:
            button.config(borderwidth=3, highlightbackground="gray",
                          bg="white smoke", fg="gray")

    def on_buttonci_leave(self, event):
        for button in Mesa.ci_buttons:
            button_number = int(button.cget("text"))
            button.config(bg=number_colors.get(button_number),
                          fg="white", borderwidth=0, highlightbackground="white")
