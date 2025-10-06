import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
import time


#  Клас вузла 
class Node:
    def __init__(self, key, color="#1A237E"): # темно-синій стартовий
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


#  Додає ребра у граф 
def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
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


#  Малює дерево 
def draw_tree(tree_root, highlight_nodes=None, title=""):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.clf()
    plt.title(title, fontsize=14)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500,
    node_color=colors, font_color="white")
    plt.pause(0.8)


# Створює дерево з масиву (як купу) 
def build_heap_tree(arr, index=0):
    if index >= len(arr):
        return None
    node = Node(arr[index])
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    node.left = build_heap_tree(arr, left_index)
    node.right = build_heap_tree(arr, right_index)
    return node


#  Генерація кольорів
def generate_colors(n):
    """Плавно переходить від темного синього до блакитного"""
    colors = []
    for i in range(n):
        blue = 120 + int(135 * (i / max(1, n - 1)))
    colors.append(f'#1A{blue:02X}F0')
    return colors


# Обхід у ширину (черга) 
def bfs_iterative(root):
    if not root:
        return []

    visited = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
    visited.append(node)
    if node.left:
        queue.append(node.left)
    if node.right:
        queue.append(node.right)
    return visited


# Обхід у глибину (стек) 
def dfs_iterative(root):
    if not root:
        return []

    visited = []
    stack = [root]

    while stack:
        node = stack.pop()
    visited.append(node)
    if node.right:
        stack.append(node.right)
    if node.left:
        stack.append(node.left)
    return visited


# Візуалізація обходу 
def visualize_traversal(root, traversal_func, title):
    order = traversal_func(root)
    colors = generate_colors(len(order))

    for i, node in enumerate(order):
        node.color = colors[i]
    draw_tree(root, title=f"{title}: крок {i + 1}, відвідано {node.val}")
plt.show()


#  Основна частина 
if __name__ == "__main__":  
    heap_array = [1, 3, 6, 5, 9, 8]
heap_root = build_heap_tree(heap_array)

plt.ion() # інтерактивний режим для анімації

print("Обхід у глибину (DFS):")
visualize_traversal(heap_root, dfs_iterative, "DFS")

# Повертаємо дерево до початкового стану для BFS
heap_root = build_heap_tree(heap_array)

print("Обхід у ширину (BFS):")
visualize_traversal(heap_root, bfs_iterative, "BFS")