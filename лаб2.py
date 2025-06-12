# Лабораторная работа: Вычисление центральности в собственных векторах ("горкой")

import networkx as nx

# 1. Создаём граф из 15 узлов в виде цепочки (path graph)
G = nx.path_graph(15)

# 2. Вычисляем центральность в собственных векторах с помощью numpy-метода
centrality = nx.eigenvector_centrality_numpy(G)

# 3. Выводим центральность для каждой вершины
print("Центральность вершин (eigenvector centrality):")
for n in centrality:
    print(f"Вершина {n}: {centrality[n]:.4f}")
    