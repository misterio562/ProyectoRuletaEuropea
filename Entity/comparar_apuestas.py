class CompararApuestas:

    def __init__(self, numero_ganador, list_apuestas = []):
        self.numero_ganador = numero_ganador
        self.list_apuestas = list_apuestas

    def getNumeroGanador(self):
        return self.numero_ganador
    
    def getListApuestas(self):
        return self.list_apuestas

    def validar_apuestas(self):
        for iteracion in self.list_apuestas:
            numero_apostado = iteracion.getNumeroApostado()

            if numero_apostado == self.numero_ganador:
                print("Ganó")
            else:
                print("Perdió")   


