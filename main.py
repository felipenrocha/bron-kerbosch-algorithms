# Felipe Nacimento Rocha 17/0050084
# Teoria e Aplicacao de Grafos Trabalho 1




def main():
    golfinhos_txt = read_file('soc-dolphins.txt')
    lista_adjacencia_golfinhos = create_dolphin_list(golfinhos_txt)

    print(lista_adjacencia_golfinhos['62'])






# def bron_kerb_algorithm_no_pivot(R, P, X):
# """"
# based on: https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm


#     algorithm BronKerbosch1(R, P, X) is

#     if P and X are both empty then
#         report R as a maximal clique
#     for each vertex v in P do
#         BronKerbosch1(R ⋃ {v}, P ⋂ N(v), X ⋂ N(v))
#         P := P \ {v}
#         X := X ⋃ {v}


# """
    










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
    
    #dividindo os espaços para resultar em uma rray com os valores separados por um espaco ex.: ["11 1"]
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



 #segundo for para os vertices que nao aparecem na segunda coluna:
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
