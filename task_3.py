import heapq
import math


class Graph:
    def __init__(self):
        self.adjacency = {}  # вершина -> список (сусід, вага)

    def add_vertex(self, vertex):
        self.adjacency.setdefault(vertex, [])

    def add_edge(self, u, v, weight):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adjacency[u].append((v, weight))
        self.adjacency[v].append((u, weight))


def dijkstra(graph, start):
    """Повертає словник {вершина: найкоротша відстань від start}."""
    distances = {vertex: math.inf for vertex in graph.adjacency}
    distances[start] = 0

    # heap зберігає пари (відстань, вершина); heapq — бінарна купа,
    # heappop завжди повертає елемент з найменшою відстанню за O(log n)
    heap = [(0, start)]

    while heap:
        current_dist, current_vertex = heapq.heappop(heap)

        # застарілий запис: до цієї вершини вже знайшли кращий шлях раніше — пропускаємо
        if current_dist > distances[current_vertex]:
            continue

        for neighbor, weight in graph.adjacency[current_vertex]:
            new_dist = current_dist + weight

            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))

    return distances


if __name__ == "__main__":
    g = Graph()
    g.add_edge("A", "B", 4)
    g.add_edge("A", "C", 1)
    g.add_edge("C", "B", 2)
    g.add_edge("B", "D", 5)
    g.add_edge("C", "D", 8)
    g.add_edge("D", "E", 3)

    result = dijkstra(g, "A")
    for vertex, dist in result.items():
        print(f"A -> {vertex}: {dist}")
