"""Modulo de coordenadas."""


class Coordenada:
    """Clase para las coordenadas."""

    def __init__(self, x, y):
        """Inicializa las coordenadas."""
        self.x = x
        self.y = y

    def mover(self, delta_x, delta_y):
        """Retorna una nueva Coordenada con la nueva posicion."""
        return Coordenada(self.x + delta_x, self.y + delta_y)

    def distancia(self, otra_coordenada):
        """Calcula la distancia entre las coordenada."""
        delta_x = self.x - otra_coordenada.x
        delta_y = self.y - otra_coordenada.y
        return (delta_x**2 + delta_y**2)**0.5
