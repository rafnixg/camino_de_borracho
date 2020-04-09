"""Modulo principal."""

import sys

from borracho import BorrachoTradicional
from campo import Campo
from coordenada import Coordenada
from graficas import graficar_medias, graficar_caminata


def caminata(campo, borracho, pasos):
    """Funcion auxiliar para la simulacion de la caminata."""
    inicio = campo.obtener_coordenada(borracho)

    for _ in range(pasos):
        campo.mover_borracho(borracho)

    return inicio.distancia(campo.obtener_coordenada(borracho))


def simular_caminata(pasos, numero_de_intentos):
    """Simula la caminata."""
    borracho = BorrachoTradicional(nombre='Rafnix')
    origen = Coordenada(0, 0)
    distancias = []

    for _ in range(numero_de_intentos):
        campo = Campo()
        campo.anadir_borracho(borracho, origen)
        simulacion_caminata = caminata(campo, borracho, pasos)
        distancias.append(round(simulacion_caminata, 1))

    return distancias


def obtener_camino_recorrido(pasos):
    """
    Crea y obtiene el camino recorrido por un borracho.
    """
    borracho = BorrachoTradicional(nombre='Rafnix')
    origen = Coordenada(0, 0)

    campo = Campo()
    campo.anadir_borracho(borracho, origen)

    camino_recorrido = [campo.obtener_coordenada(borracho)]

    for _ in range(pasos):
        campo.mover_borracho(borracho)
        camino_recorrido.append(campo.obtener_coordenada(borracho))

    return camino_recorrido


def main():
    """Funcion principal."""
    opciones_validas = ['0', '1', '2', 'exit']

    menu = ('\n********************************************************************************************\n'
            '* Seleccione una de las siguientes opciones:                                               *\n'
            '*                                                                                          *\n'
            '* 0: Obtener los datos Min, Max y Media para un camino aleatorio de N pasos en M intentos. *\n'
            '* 1: Gráfica de Medias para una lista de caminatas con N1...Nn pasos c/u en M intentos.    *\n'
            '* 2: Gráfica de la camina realiza para un caso de N pasos.                                 *\n'
            '* exit: Finalizar la ejecución del programa                                                *\n'
            '*                                                                                          *\n'
            '* las cantidades de pasos se solicitarán a continuación.                                   *\n'
            '********************************************************************************************\n')

    opcion = input(menu)

    while opcion not in opciones_validas:
        opcion = input('Opcion inválida, por favor reintentar.\n')

    if opcion == 'exit':
        print('Nos vemos!')
        sys.exit(0)

    opcion = int(opcion)

    if opcion == 2:
        pasos = int(input('Cantidades de pasos: '))
        camino_recorrido = obtener_camino_recorrido(pasos)

        graficar_caminata(camino_recorrido, pasos)
    else:
        distancias_de_caminata = [int(x) for x in input('numeros de pasos, separados por un espacio: ').split()]
        numero_de_intentos = int(input('Cantidades de intentos: '))

        distancia_media_por_caminata = []

        for pasos in distancias_de_caminata:
            distancias = simular_caminata(pasos, numero_de_intentos)

            distancia_media = round(sum(distancias) / len(distancias), 4)
            distancia_maxima = max(distancias)
            distancia_minima = min(distancias)

            distancia_media_por_caminata.append(distancia_media)

            if opcion == 0:
                print('caminata aleatoria de %s pasos\n'
                      'Distancia Media recorrida = %s\n'
                      'Distancia Maxima recorrida = %s\n'
                      'Distancia Minima recorrida = %s\n'
                      % (pasos, distancia_media, distancia_maxima, distancia_minima))
            else:
                graficar_medias(distancias_de_caminata, distancia_media_por_caminata)


if __name__ == '__main__':
    while 1:
        main()
