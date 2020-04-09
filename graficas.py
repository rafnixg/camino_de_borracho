"""
Funciones para graficar datos.
"""

from bokeh.plotting import figure, show


def graficar_medias(x, y):
    grafica = figure(title='Camino aleatorio', x_axis_label='pasos', y_axis_label='distancia al punto de origen')

    grafica.line(x, y, legend_label='Distancia Media.')

    show(grafica)


def graficar_caminata(camino, pasos: int):
    grafica = figure(title='Camino aleatorio con %d pasos, partiendo del punto de origen.' % pasos,
                     x_axis_label='Eje x', y_axis_label='Eje y')

    list_x = []
    list_y = []
    for desplazamiento in camino:
        list_x.append(desplazamiento.x)
        list_y.append(desplazamiento.y)

    grafica.line(list_x, list_y, legend_label='Caminata.')

    show(grafica)
