import heapq

def dijkstra(graph, start):
    distances = {vertex:
float("infinity") for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            
           distance = current_distance + weight
           if distance < distances[neighbor]:
               distances[neighbor] =distance
               heapq.heappush(priority_queue,(distance, neighbor))
    return distance
graph = {
    "A":{"B": 4, "C": 7},
    "B":{"A": 4, "D": 2,"E":5},
    'C': {'A': 7, 'D': 2, 'E': 5},
    'D': {'B': 2, 'C': 2, 'E': 1,'F': 4},
    'E': {'C': 5, 'D': 1, 'F': 11},
    'F': {'B': 8, 'D': 4, 'E': 11}
}
result = dijkstra(graph, 'A')
print(result)
    

           



#                 