from Adapter import AbstractAdapter
from jugador import Personaje

class AdapterPlayer(AbstractAdapter, Personaje):

    def __init__(self):
        Personaje.__init__(self)

    def hit(self, x, y):
        self.disparar(x, y)

    def draw(self, window):
        self.dibujar(window)

    def move(self):
        self.mover()
