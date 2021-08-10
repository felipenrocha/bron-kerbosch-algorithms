# Felipe Nacimento Rocha 17/0050084
# Teoria e Aplicacao de Grafos Trabalho 1
# Para melhor visualizacao da interface recomenda-se o uso de python3, entretanto eh possivel ler os resultados em python2
from bron_no_pivot import bron_kerb_algorithm_no_pivot
from bron_pivot import bron_kerb_algorithm_with_pivot
from bron import read_file, create_dolphin_list, get_all_vertex

def main():

    golfinhos_txt = read_file('soc-dolphins.txt')
    lista_adjacencia_golfinhos = create_dolphin_list(golfinhos_txt)

    bron_kerb_algorithm_no_pivot(
        R=[], P=get_all_vertex(lista_adjacencia_golfinhos), X=[])

    bron_kerb_algorithm_with_pivot(
        R=[], P=get_all_vertex(lista_adjacencia_golfinhos), X=[])






main()
