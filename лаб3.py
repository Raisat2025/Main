 
import networkx as nx 
# Создаем граф по модели Эрдеша-Реньи
G = nx.erdos_renyi_graph(22, 0.2)
a = 0
for n in G.nodes():
     a = a + G.degree(n)
    #  Выводим результат
print(float(a) / len(G.nodes()))     