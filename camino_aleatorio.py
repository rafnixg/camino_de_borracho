"""Modulo principal."""

from borracho import BorrachoTradicional
from campo import Campo
from coordenada import Coordenada


def caminata(campo, borracho, pasos):
    """Funcion auxiliar para la simulacion de la caminata."""
    inicio = campo.obtener_coordenada(borracho)

    for _ in range(pasos):
        campo.mover_borracho(borracho)

    return inicio.distancia(campo.obtener_coordenada(borracho))


def simular_caminata(pasos, numero_de_intentos, tipo_de_borracho):
    """Simula la caminata."""
    borracho = tipo_de_borracho(nombre='Rafnix')
    origen = Coordenada(0, 0)
    distancias = []

    for _ in range(numero_de_intentos):
        campo = Campo()
        campo.anadir_borracho(borracho, origen)
        simulacion_caminata = caminata(campo, borracho, pasos)
        distancias.append(round(simulacion_caminata, 1))

    return distancias


def main(distancias_de_caminata, numero_de_intentos, tipo_de_borracho):
    """Funcion principal."""
    for pasos in distancias_de_caminata:
        distancias = simular_caminata(pasos, numero_de_intentos, tipo_de_borracho)  # noqa

        distancia_media = round(sum(distancias) / len(distancias), 4)
        distancia_maxima = max(distancias)
        distancia_minima = min(distancias)

        print(f'{tipo_de_borracho.__name__} caminata aleatoria de {pasos}')  # noqa
        print(f'Media = {distancia_media}')
        print(f'Max = {distancia_maxima}')
        print(f'Min = {distancia_minima}')


if __name__ == '__main__':
    """Punto de entrada."""
    distancias_de_caminata = [10, 100, 1000, 10000]
    numero_de_intentos = 100

    main(distancias_de_caminata, numero_de_intentos, BorrachoTradicional)
