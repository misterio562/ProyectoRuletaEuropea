from rulette.datos_generales.number_colors import number_colors

class Apuesta:
    def __init__(self, tipo_apuesta, monto_apostado):
        self._tipo_apuesta = tipo_apuesta  # Tipo de apuesta (por ejemplo, "número", "color", "docena", etc.)
        self._monto_apostado = monto_apostado  # Monto apostado en la apuesta
        self._numero_apostado = None  # Número específico (solo si es una apuesta de número)
        self._color_apostado = None  # Color específico (solo si es una apuesta de color)

    @classmethod
    def crearApuestaSinParametros(cls):
        return cls(None, 0)  # Crear una apuesta sin valores iniciales
    

    def getNumeroApostado(self):
        return self._numero_apostado
    
    def setNumeroApostado(self,numero_apostado):
        self._numero_apostado = numero_apostado

    def getColorApostado(self):
        return self._color_apostado
    
    def setColorApostado(self,colorApostado):
        self._color_apostado = colorApostado        

    def getMontoApostado(self):
        return self._monto_apostado

    def setMontoApostado(self,montoApostado):
        self._monto_apostado = montoApostado

    def getTipoApuesta(self):
        return self._tipo_apuesta
    
    def setTipoapuesta(self,tipoapuesta):
        self._tipo_apuesta = tipoapuesta

        
    def crearApuesta(self, numero, color):
        self.setNumeroApostado(numero)
        self.setColorApostado(color)


    def calcular_ganancia(self, tipo_apuesta, numero_apostado, monto, resultado):

        # Invierte el diccionario para buscar números por color
        color_numbers = {v: k for k, v in number_colors.items()}

        # Implementa la lógica para calcular las ganancias basadas en el resultado de la ruleta
        ganancia = 0
        
        
        # Verificar si la apuesta es en "1-12" y el resultado está en ese rango
        if tipo_apuesta == "1-12" and 1 <= resultado <= 12:
            ganancia += monto * 2  
            
        if tipo_apuesta == "1-18" and 1 <= resultado <= 18:
            ganancia += monto * 2  
            
        if tipo_apuesta == "13-24" and 13 <= resultado <= 24:
            ganancia += monto * 2  

        if tipo_apuesta == "25-36" and 25 <= resultado <= 36:
            ganancia += monto * 2   

        if tipo_apuesta == "19-36" and 19 <= resultado <= 36:
            ganancia += monto * 2         

        if tipo_apuesta == "even" and resultado %2 == 0:
            ganancia += monto * 2

        if tipo_apuesta == "odd" and resultado %2 != 0:
            ganancia += monto * 2  

        if tipo_apuesta == "red" and number_colors.get(resultado) == "red":
            ganancia += monto * 2  # Multiplicamos el monto por 2 en este ejemplo
          
        if tipo_apuesta == "black" and number_colors.get(resultado) == "black":
            ganancia += monto * 2  # Multiplicamos el monto por 2 en este ejemplo
            
        # Verificar si la apuesta es en la columna izquierda y el resultado está en esa columna
        if tipo_apuesta == "cd" and resultado in [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]:
            ganancia += monto * 3   
        # Verificar si la apuesta es en la columna central y el resultado está en esa columna
        if tipo_apuesta == "cc" and resultado in [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]:
            ganancia += monto * 3 
        # Verificar si la apuesta es en la columna derecha y el resultado está en esa columna
        if tipo_apuesta == "ci" and resultado in [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]:
            ganancia += monto * 3        
        # Verificar si la apuesta es en el número "5" y el resultado es igual a "5"
        if tipo_apuesta == "numero" and numero_apostado == resultado:
            ganancia += monto * 36  # Multiplicamos el monto por 36 en este ejemplo

            

        print(f"La ganancia es de: {ganancia}")

        return ganancia


        # if resultado == self.numero:
        #     # El jugador acertó el número, ganancia mayor
        #     return self.monto * 36
        # elif self.color == "rojo" and resultado in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]:
        #     # El jugador apostó a rojo y el resultado es un número rojo, ganancia 2x
        #     return self.monto * 2
        # elif self.color == "negro" and resultado in [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]:
        #     # El jugador apostó a negro y el resultado es un número negro, ganancia 2x
        #     return self.monto * 2
        # else:
        #     # El jugador perdió la apuesta
        #     return 0


# # Ejemplo de uso
# apuesta_jugador1 = Apuesta(7, "rojo", 10.0)
# resultado_ruleta = 7
# ganancia_jugador1 = apuesta_jugador1.calcular_ganancia(resultado_ruleta)

# print(f"Jugador 1 apostó al número {apuesta_jugador1.numero} ({apuesta_jugador1.color})")
# print(f"Ganancia del jugador 1: {ganancia_jugador1}")
