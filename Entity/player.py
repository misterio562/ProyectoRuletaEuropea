import tkinter as tk

class Player:

    _instance = None  # Variable de clase para almacenar la única instancia

    def __new__(cls, initial_balance=1000):
        if cls._instance is None:
            cls._instance = super(Player, cls).__new__(cls)
            cls._instance._balance = initial_balance
            cls._instance.bets = []
        return cls._instance

    def get_saldo(self):
        return self._balance
    
    def set_saldo(self, nuevo_saldo):
        if nuevo_saldo >= 0:
            self._balance = nuevo_saldo

    def descontarSaldo(self, monto):
        self._balance = self._balance - monto        
    

    def apostar():
        pass


