# destinado a funcoes comuns p/ ambos algoritmos


def neighbor(v, lista):
    """retorna os vertices adjacentes a v"""
    return lista[str(v)]


def get_all_vertex(lista):
    """retorna P (all vertex from adjacency list)"""
    vertices = []
    for key, value in lista.items():
        vertices.append(int(key))
    return vertices

# copied from https://www.geeksforgeeks.org/python-intersection-two-lists/ and
# https://www.geeksforgeeks.org/python-union-two-lists/


# Python program to illustrate the intersection
# of two lists in most simple way


def intersection(lst1, lst2):
    
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


def union(lst1, lst2):
    return lst1 + lst2


def difference(lst1, lst2):
    """return lst1 \ lst2"""
    
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

        obs.: o código é meio confuso devido a forma como está escrito o soc-doplhins.txt e nao queria alterá-lo
    """

    lista_golfinhos = {}

    # divide o texto a partir da string do arquivo, so precisamos da 2a posicao que eh onde estao os numeros:
    txtNumeros = txt.split("62 62 159")[1]

    # dividindo os espacos para resultar em uma array com os valores separados por um espaco ex.: ["11 1"]
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


    
