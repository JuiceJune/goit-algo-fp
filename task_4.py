import heapq
import uuid

import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4()) # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуємо значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def build_tree_from_heap(heap, index=0):
    """Рекурсивно перетворює масив-купу heap у дерево з об'єктів Node.

    Для елемента з індексом i лівий нащадок знаходиться за індексом 2*i + 1,
    правий — за індексом 2*i + 2 (стандартна властивість купи, представленої масивом).
    """
    if index >= len(heap):
        return None

    node = Node(heap[index])
    node.left = build_tree_from_heap(heap, 2 * index + 1)
    node.right = build_tree_from_heap(heap, 2 * index + 2)
    
    return node


if __name__ == "__main__":
    numbers = [10, 4, 5, 1, 0, 3]
    heapq.heapify(numbers)
    print("Масив-купа:", numbers)

    root = build_tree_from_heap(numbers)
    draw_tree(root)
