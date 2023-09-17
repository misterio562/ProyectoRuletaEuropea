class RepositorioApuestasSingleton:
    _instance = None  # Variable para almacenar la única instancia

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.apuestas = []  # Inicializar la lista de apuestas
        return cls._instance

    def agregar_apuesta(self, apuesta):
        self.apuestas.append(apuesta)  # Agrega una apuesta a la lista

    def limpiar_apuesta(self):
        self.apuestas = [] # Limpia la lista

    def obtener_lista_apuestas(self):
        return self.apuestas  # Devuelve la lista completa de apuestas

    def obtener_apuestas_por_numero(self, numero):
        apuestas_con_numero = [apuesta for apuesta in self.apuestas if apuesta.getNumeroApostado() == numero]
        return apuestas_con_numero

    def obtener_apuestas_por_color(self, color):
        apuestas_con_color = [apuesta for apuesta in self.apuestas if apuesta.getColorApostado() == color]
        return apuestas_con_color
