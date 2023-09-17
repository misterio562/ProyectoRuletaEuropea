import tkinter as tk
import math
import random
from rulette.datos_generales.number_colors import number_colors
from rulette.mesa import Mesa
from Entity.comparar_apuestas import CompararApuestas
from GestionRepositorio.repositorio_apuestas import RepositorioApuestasSingleton
from Entity.apuesta import Apuesta
from Entity.player import Player

class Rulette():

    # Variable de entrada para la rueda
    angle = 85
    rotation_speed = 6.0

    # Dimensiones del Canvas
    CANVAS_WIDTH = 500
    CANVAS_HEIGHT = 400
    X_CENTER = CANVAS_WIDTH // 2
    Y_CENTER = CANVAS_HEIGHT // 2

    def __init__(self, ventana):
        self.frame = tk.Frame(ventana, width=30, bg="green")
        self.frame.pack(side="left")

        self.canvas = tk.Canvas(self.frame, width=422, height=500)
        self.canvas.pack()

        self.numero_ganador = 0

        self.label = tk.Label(self.frame, text=f"El número ganador es el: {self.numero_ganador}", font=(
            "Helvetica", 12, "bold"))
        self.label.place(x=110, y=420)

        self.rotate_button = tk.Button(
            self.frame, text="¡Girar!", command=self.rotate_circle)
        self.rotate_button.place(x=180, y=450)

    def draw_circle(self):
        # Datos del tamaño del Círculo
        x = 220
        y = Rulette.Y_CENTER
        radius = 200  # Reducido el radio para acercar la bolita al centro

        num_slices = 37
        slice_angle = 360 / num_slices

        select_number = self.obtenerNumeroAleatorio(number_colors)

        self.numero_ganador = select_number
        for iteraciones, (n, c) in enumerate(number_colors.items(), start=0):

            start_angle = math.radians(
                iteraciones * slice_angle + Rulette.angle)
            end_angle = math.radians(
                (iteraciones + 1) * slice_angle + Rulette.angle)

            start_x = x + radius * math.cos(start_angle)
            start_y = y - radius * math.sin(start_angle)
            end_x = x + radius * math.cos(end_angle)
            end_y = y - radius * math.sin(end_angle)

            label_x = (x + radius * 0.9 *
                       math.cos((start_angle + end_angle) / 2))
            label_y = (y - radius * 0.9 *
                       math.sin((start_angle + end_angle) / 2))

            self.canvas.create_polygon(x, y, start_x, start_y, end_x,
                                       end_y, fill=c, outline="white")

            self.canvas.create_text(label_x, label_y, text=str(
                n), fill="white", font=("Helvetica", 10, "bold"))

            if n == select_number:
                label_xx = (x + radius * 0.7 *
                            math.cos((start_angle + end_angle) / 2))
                label_yy = (y - radius * 0.7 *
                            math.sin((start_angle + end_angle) / 2))
                self.canvas.create_oval(
                    label_xx - 10, label_yy - 10, label_xx + 10, label_yy + 10, fill="white", outline="black")

    def draw_circle2(self):
        x = 220
        y = Rulette.Y_CENTER
        radius = 160

        self.canvas.create_oval(
            x - radius, y - radius, x + radius, y + radius, outline="white", width=2)

    def draw_circle3(self):
        x = 220
        y = Rulette.Y_CENTER
        radius = 120

        self.canvas.create_oval(x - radius, y - radius, x + radius,
                                y + radius, fill="black", outline="white", width=2)

    def rotate_circle(self):
        if Rulette.rotation_speed == 0:
            Rulette.rotation_speed = 6.0  # Restablecer la velocidad de rotación

        Rulette.angle += Rulette.rotation_speed
        Rulette.rotation_speed *= 0.995
        if Rulette.rotation_speed < 0.2:
            Rulette.rotation_speed = 0
            # self.label.config(
            # text=f"El número ganador es el: {self.numero_ganador} {number_colors[self.numero_ganador]}")
            repo_apuestas = RepositorioApuestasSingleton()
            clase_apuesta = Apuesta.crearApuestaSinParametros()
            mesa = Mesa.crearMesaSinParámetro()
            print("-----------------------------------------")
            player = Player()
            saldo = player.get_saldo()
            for apuesta in repo_apuestas.obtener_lista_apuestas():
                ganancia = clase_apuesta.calcular_ganancia(apuesta.getTipoApuesta(),apuesta.getNumeroApostado(),apuesta.getMontoApostado(),self.numero_ganador)
                if ganancia == 0:
                    saldo = saldo - apuesta.getMontoApostado()
                else:
                    saldo = saldo + ganancia
                print(f"Tipo de apuestas: {apuesta.getTipoApuesta()}")
                print(f"Número apostado: {apuesta.getNumeroApostado()} ")
                print(f"Color: {apuesta.getColorApostado()}")
                print(f"Monto apostado: {apuesta.getMontoApostado()}")

            player.set_saldo(saldo)
            mesa.actualizarMonto()    
            
            mesa.resetMonto()
            # print(repo_apuestas.apuestas)
            # print(self.numero_ganador)


            # for apuesta in repo_apuestas.obtener_lista_apuestas():
            #     print("Numero: ", apuesta.getNumeroApostado())
            #     print("Monto: ",apuesta.getMontoApostado())
            #     print("Color: ",apuesta.getColorApostado())


            # ca = CompararApuestas(self.numero_ganador, repo_apuestas.obtener_lista_apuestas())
            # ca.validar_apuestas()
            
            repo_apuestas.limpiar_apuesta()
        else:
            self.canvas.delete("all")

            self.draw_circle()
            self.draw_circle2()
            self.draw_circle3()

            self.frame.after(16, self.rotate_circle)

    def obtenerNumeroAleatorio(self, diccionario):
        # Obtén una lista de las claves (números) del diccionario
        numeros = list(diccionario.keys())

        # Elije un número aleatorio de la lista de claves
        numero_aleatorio = random.choice(numeros)

        # Obtén el color correspondiente al número aleatorio
        color = diccionario[numero_aleatorio]

        return numero_aleatorio

    def printRulette(self):
        self.draw_circle()
        self.draw_circle2()
        self.draw_circle3()
