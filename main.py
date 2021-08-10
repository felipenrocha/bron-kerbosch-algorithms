# Felipe Nacimento Rocha 17/0050084
# Teoria e Aplicacao de Grafos Trabalho 1
# Para melhor visualizacao da interface recomenda-se o uso de python3, entretanto eh possivel ler os resultados em python2
import random


def main():

    golfinhos_txt = read_file('soc-dolphins.txt')
    lista_adjacencia_golfinhos = create_dolphin_list(golfinhos_txt)
    
    bron_kerb_algorithm_no_pivot(
        R=[], P=get_all_vertex(lista_adjacencia_golfinhos), X=[])

    bron_kerb_algorithm_with_pivot(
        R=[], P=get_all_vertex(lista_adjacencia_golfinhos), X=[])


def bron_kerb_algorithm_no_pivot(R, P, X):
    """"
    based on: https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm


    algorithm BronKerbosch1(R, P, X) is
    if P and X are both empty then
        report R as a maximal clique
    for each vertex v in P do
        BronKerbosch1(R U v, P intersect N(v), X intersect N(v))
        P := P -  v
        X := X U v
        """
    golfinhos_txt = read_file('soc-dolphins.txt')
    lista = create_dolphin_list(golfinhos_txt)

    #  Retirado dos slides das aulas:
    #  R: vertices que seriam parte do clique
    #  P: vertices que tem ligacao com todos os vertices de R (candidatos).
    #  Conjunto X: vertices ja analisados e que nao  levam a uma extensao do conjunto R.

    if len(P) == 0 and len(X) == 0:
        print(' Clique maximal encontrado: ', R,
              '\n', 'No de Vertices: ', len(R))

    for v in P[:]:
        bron_kerb_algorithm_no_pivot(
            R=union(R, [v]),
            P=intersection(P, neighbor(v, lista)),
            X=intersection(X, neighbor(v, lista)))
        P.remove(v)
        X.append(v)


def bron_kerb_algorithm_with_pivot(R, P, X):
    """
    based on: https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm

    algorithm BronKerbosch2(R, P, X) is
        if P and X are both empty then
            report R as a maximal clique
        choose a pivot vertex u in P ⋃ X
        for each vertex v in P \ N(u) do
            BronKerbosch2(R ⋃ {v}, P ⋂ N(v), X ⋂ N(v))
            P := P \ {v}
            X := X ⋃ {v}
    """
    golfinhos_txt = read_file('soc-dolphins.txt')
    lista = create_dolphin_list(golfinhos_txt)

    if len(P) == 0 and len(X) == 0:
        print(' Clique maximal encontrado: ', R,
              '\n', 'No de Vertices: ', len(R))
    #   random pivot:
    try:
        u = random.choice(list(union(P, X)))
        P_new = difference(P, neighbor(u, lista))
    except IndexError:
        P_new = P

    for v in P_new[:]:
        bron_kerb_algorithm_with_pivot(
            R=union(R, [v]),
            P=intersection(P, neighbor(v, lista)),
            X=intersection(X, neighbor(v, lista)))
        P.remove(v)
        X.append(v)


def neighbor(v, lista):
    """retorna os vertices adjacentes a v"""
    return lista[str(v)]


def get_all_vertex(lista):
    """retorna P (all vertex from adjacency list)"""
    vertices = []
    for key, value in lista.items():
        vertices.append(int(key))
    return vertices


# Python program to illustrate the intersection
# of two lists in most simple way
def intersection(lst1, lst2):
    # copied from https://www.geeksforgeeks.org/python-intersection-two-lists/ and
    # https://www.geeksforgeeks.org/python-union-two-lists/
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


def union(lst1, lst2):
    return lst1 + lst2


def difference(lst1, lst2):
    lista_difference = []
    for value in lst1:
        if value not in lst2:
            lista_difference.append(value)
    return lista_difference

# criação lista de adjacencia:


def read_file(filename):
    """
    Funcao p ler o arquivo txt que servira de base de dados do grafo
    string :: IO
    filename -> arquivo
    """
    arquivo = open(filename, "r")

    golfinhos = arquivo.read()

    arquivo.close()
    return golfinhos


def create_dolphin_list(txt):
    """
    cria lista de adjacencia a partir do texto do arquivo
    string :: list
    txt -> lista_golfinhos

    lista_golfinhos = {
        vertice_1 : [vertices_adjacentes],
        vertice_2 : [vertices_adjacentes],
        ...
        vertice_n : [vertices_adjacentes]
        }

        vertices_adjacentes = [v1, v2, v3],    vn Inteiro
    """

    lista_golfinhos = {}

    # divide o texto a partir da string do arquivo, so precisamos da 2a posicao que eh onde estao os numeros:
    txtNumeros = txt.split(
        "62 62 159")[1]

    # dividindo os espacos para resultar em uma aray com os valores separados por um espaco ex.: ["11 1"]
    txtArray = txtNumeros.split("\n")

    # variavel responsavel por manter o vertice atual da lista
    vertice_atual = ""
    # array para os vertices adjacentes de cada vertice até o 55
    vertices_adjacentes = []
    for texto in txtArray:

        vertices = texto.split(" ")

        # usando a segunda coluna como chave para vertice vertice[0]: vertice adjacente vertice[1]: vertice atual
        if len(vertices) == 2:
            if vertice_atual != vertices[1]:
                # se o vertice for novo ele eh inserido na lista e eh definido como vertice atual e os vertices adjacentes sao zerados
                vertice_atual = vertices[1]
                vertices_adjacentes = []
                vertices_adjacentes.append(int(vertices[0]))
                lista_golfinhos[vertice_atual] = vertices_adjacentes

            else:
                # se vertice ja existir na lista, adiciona o novo vertice adjacente
                vertices_adjacentes = lista_golfinhos.get(vertice_atual)
                vertices_adjacentes.append(int(vertices[0]))
                lista_golfinhos[vertice_atual] = vertices_adjacentes

 # segundo for para os vertices que nao aparecem na segunda coluna:
    for texto in txtArray:

        vertices = texto.split(" ")

        # usando a segunda coluna como chave para vertice vertice[1]: vertice adjacente vertice[0]: vertice atual
        if len(vertices) == 2:
            vertice_atual = vertices[0]
            if not lista_golfinhos.get(vertice_atual):
                # se o vertice for novo ele eh inserido na lista e eh definido como vertice atual e os vertices adjacentes sao zerados

                vertices_adjacentes = []
                vertices_adjacentes.append(int(vertices[1]))
                lista_golfinhos[vertice_atual] = vertices_adjacentes

            else:
                # se vertice ja existir na lista, adiciona o novo vertice adjacente
                vertices_adjacentes = lista_golfinhos.get(vertice_atual)
                if int(vertices[0]) not in vertices_adjacentes:
                    vertices_adjacentes.append(int(vertices[1]))
                lista_golfinhos[vertice_atual] = vertices_adjacentes

    return lista_golfinhos


main()
