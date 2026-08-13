from collections import deque

from task_4 import Node, draw_tree


def color_for_step(step, total_steps, dark=(20, 20, 90), light=(210, 235, 255)):
    """Повертає hex-колір (#RRGGBB), що інтерполює між dark і light
    залежно від step: 0 -> найтемніший, останній крок -> найсвітліший."""
    ratio = step / max(total_steps - 1, 1)
    r = round(dark[0] + (light[0] - dark[0]) * ratio)
    g = round(dark[1] + (light[1] - dark[1]) * ratio)
    b = round(dark[2] + (light[2] - dark[2]) * ratio)
    return f"#{r:02X}{g:02X}{b:02X}"


def dfs_traversal(root: Node):
    """Обхід у глибину (preorder) через явний стек, БЕЗ рекурсії."""
    order = []
    stack = [root]
    while stack:
        node = stack.pop()
        order.append(node)
        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)

    return order


def bfs_traversal(root):
    """Обхід у ширину через явну черг (deque), БЕЗ рекурсії."""
    order = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        order.append(node)
        if node.right:
            queue.append(node.right)
        
        if node.left:
            queue.append(node.left)
    return order


def colorize_by_order(order):
    """Присвоює кожному вузлу колір відповідно до його позиції в order."""
    for step, node in enumerate(order):
        node.color = color_for_step(step, len(order))


def build_sample_tree():
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)
    return root


if __name__ == "__main__":
    dfs_root = build_sample_tree()
    dfs_order = dfs_traversal(dfs_root)
    print("DFS порядок:", [n.val for n in dfs_order])
    colorize_by_order(dfs_order)
    draw_tree(dfs_root)

    bfs_root = build_sample_tree()
    bfs_order = bfs_traversal(bfs_root)
    print("BFS порядок:", [n.val for n in bfs_order])
    colorize_by_order(bfs_order)
    draw_tree(bfs_root)
