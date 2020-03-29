"""Modulo borrachos."""
import random


class Borracho:
    """Clase para los borrachos."""

    def __init__(self, nombre):
        """Inicializa el borracho."""
        self.nombre = nombre


class BorrachoTradicional(Borracho):
    """Clase para el borracho tradicional."""

    def __init__(self, name):
        """Inicializa el borracho tradicional."""
        super().__init__(name)

    def camina(self):
        """Retorna una tupla.

        Calcula el valor aleatorio con la direccion
        a donde se mueve el borracho.
        """
        return random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
