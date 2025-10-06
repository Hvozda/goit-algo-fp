import heapq # імпорт бібліотеки для роботи з пріоритетною чергою

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_edge(self, u, v, weight):
        """Додає ребро до графа"""
        if u not in self.vertices:
            self.vertices[u] = []
        if v not in self.vertices:
            self.vertices[v] = []
        self.vertices[u].append((v, weight))
        self.vertices[v].append((u, weight))  
        
    def dijkstra(self, start):
        distances = {vertex: float('inf') for vertex in self.vertices}
        distances[start] = 0

        priority_queue = [(0, start)]  # (відстань, вершина)
        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.vertices[current_vertex]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances
    
if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B', 4)
    g.add_edge('A', 'C', 2)
    g.add_edge('B', 'C', 5)
    g.add_edge('B', 'D', 10)
    g.add_edge('C', 'E', 3)
    g.add_edge('E', 'D', 4)
    g.add_edge('D', 'F', 11)

    start_vertex = 'A'
    distances = g.dijkstra(start_vertex)

    print(f"Найкоротші відстані від вершини {start_vertex}:")
    for vertex, distance in distances.items():
        print(f"До вершини {vertex}: {distance}")
