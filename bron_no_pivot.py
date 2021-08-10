from bron import create_dolphin_list, difference, get_all_vertex, neighbor, union, read_file, intersection

def bron_kerb_algorithm_no_pivot(R, P, X):
    """"
    based on: https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm


    algorithm BronKerbosch1(R, P, X) is
    if P and X are both empty then
        report R as a maximal clique
    for each vertex v in P do
        BronKerbosch1(R U v, P intersect N(v), X intersect N(v))
        P := P \  v
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
