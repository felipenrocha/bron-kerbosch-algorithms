
from bron import create_dolphin_list, difference, neighbor, union, read_file, intersection
import random

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
