from bron import create_dolphin_list, difference, neighbor, union, read_file, intersection


def average_cluster(lista):
    soma = 0
    i = 0
    for v in lista:
        soma = soma + index_cluster(v, lista)
        i = i + 1
    average = soma / i
    return average


def index_cluster(v, lista):
    """Ci = 2*(links to node i) / nb*(nb-1)"""

    ni = len(neighbor(v, lista))
    ti = get_ti(v, lista)
    try:
        coeficiente = (2 * ti) / (ni*(ni - 1))
    except ZeroDivisionError:
        coeficiente = 0
    return coeficiente


def get_ti(v, lista):
    i = 0
    for vizinho in neighbor(v, lista):
        for vizinho_2 in neighbor(vizinho, lista):
            if int(v) in neighbor(vizinho_2, lista):   
                i = i + 1
    return i
