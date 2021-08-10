# Felipe Nacimento Rocha 17/0050084
# Teoria e Aplicacao de Grafos Trabalho 1
# Para melhor visualizacao da interface recomenda-se o uso de python3, entretanto eh possivel ler os resultados em python2
from bron_no_pivot import bron_kerb_algorithm_no_pivot
from bron_pivot import bron_kerb_algorithm_with_pivot
from bron import read_file, create_dolphin_list, get_all_vertex

import os

def main():
    interface()


def interface():
    golfinhos_txt = read_file('soc-dolphins.txt')
    lista_adjacencia_golfinhos = create_dolphin_list(golfinhos_txt)
    os.system('cls' if os.name == 'nt' else 'clear')
    menu_selection = 0
    while(int(menu_selection) != 5):
        
        print("Trabalho teoria de Grafos 1 - Algoritmos Bron-Kerbosch")
        menu_selection = input("1) Lista de Adjacencias\n"
                               "2) Algoritmo Bron-Kerbosch sem Pivo \n"
                               "3) Algoritmo Bron-Kerbosch com Pivo\n"
                               "4) O Coeficiente médio de Aglomeração do Grafo."
                               "\n5)Sair \nSelecao: ")
      
        print(menu_selection)
        if int(menu_selection) == 1:
            print("Lista de adjacencia: \n", lista_adjacencia_golfinhos)
        
        
        elif int(menu_selection) == 2:
            bron_kerb_algorithm_no_pivot(
                R=[], P=get_all_vertex(lista_adjacencia_golfinhos), X=[])
       
       
        elif int(menu_selection) == 3:
            bron_kerb_algorithm_with_pivot(
                R=[], P=get_all_vertex(lista_adjacencia_golfinhos), X=[])
       
       
        elif int(menu_selection) == 4:
            print("Coeficiente médio de Aglomeração do Grafo: ")

main()
