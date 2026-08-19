from collections import deque
import heapq


# =========================================================
# 1. LIST (Array)
# =========================================================

numbers = [10, 20, 30, 40]

print("LIST:")
print(numbers)
print()


# =========================================================
# 2. TUPLE
# =========================================================

point = (10, 20)

print("TUPLE:")
print(point)
print()


# =========================================================
# 3. SET
# =========================================================

visited = set()

visited.add("A")
visited.add("B")
visited.add("C")

print("SET:")
print(visited)
print()


# =========================================================
# 4. DICTIONARY (Hash Map)
# =========================================================

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": []
}

print("DICTIONARY:")
print(graph)
print()


# =========================================================
# 5. STACK
#    LIFO = Last In, First Out
# =========================================================

stack = []

stack.append("A")
stack.append("B")
stack.append("C")

print("STACK:")

while stack:
    print("Pop:", stack.pop())

print()


# =========================================================
# 6. QUEUE
#    FIFO = First In, First Out
# =========================================================

queue = deque()

queue.append("A")
queue.append("B")
queue.append("C")

print("QUEUE:")

while queue:
    print("Dequeue:", queue.popleft())

print()


# =========================================================
# 7. PRIORITY QUEUE / MIN HEAP
# =========================================================

priority_queue = []

heapq.heappush(priority_queue, (3, "Low priority"))
heapq.heappush(priority_queue, (1, "High priority"))
heapq.heappush(priority_queue, (2, "Medium priority"))

print("PRIORITY QUEUE:")

while priority_queue:
    priority, task = heapq.heappop(priority_queue)
    print(priority, task)

print()


# =========================================================
# 8. LINKED LIST
# =========================================================

class LinkedNode:
    def __init__(self, data):
        self.data = data
        self.next = None


node1 = LinkedNode("A")
node2 = LinkedNode("B")
node3 = LinkedNode("C")

node1.next = node2
node2.next = node3

print("LINKED LIST:")

current = node1

while current:
    print(current.data, end=" -> ")
    current = current.next

print("None")
print()


# =========================================================
# 9. TREE
# =========================================================

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = TreeNode("A")

root.left = TreeNode("B")
root.right = TreeNode("C")

root.left.left = TreeNode("D")
root.left.right = TreeNode("E")

root.right.right = TreeNode("F")


# =========================================================
# 10. BFS ON TREE
# =========================================================

def bfs(root):

    if root is None:
        return

    queue = deque([root])

    while queue:

        node = queue.popleft()

        print(node.data, end=" ")

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)


print("TREE BFS:")
bfs(root)
print()
print()


# =========================================================
# 11. DFS ON TREE
# =========================================================

def dfs(node):

    if node is None:
        return

    print(node.data, end=" ")

    dfs(node.left)
    dfs(node.right)


print("TREE DFS:")
dfs(root)
print()
print()


# =========================================================
# 12. GRAPH
# =========================================================

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": []
}


# =========================================================
# 13. BFS ON GRAPH
# =========================================================

def graph_bfs(graph, start):

    queue = deque([start])
    visited = set()

    while queue:

        node = queue.popleft()

        if node in visited:
            continue

        visited.add(node)

        print(node, end=" ")

        for neighbor in graph[node]:

            if neighbor not in visited:
                queue.append(neighbor)


print("GRAPH BFS:")
graph_bfs(graph, "A")
print()
print()


# =========================================================
# 14. DFS ON GRAPH
# =========================================================

def graph_dfs(graph, node, visited=None):

    if visited is None:
        visited = set()

    if node in visited:
        return

    visited.add(node)

    print(node, end=" ")

    for neighbor in graph[node]:

        graph_dfs(graph, neighbor, visited)


print("GRAPH DFS:")
graph_dfs(graph, "A")
print()
print()


# =========================================================
# 15. ITERATOR
# =========================================================

numbers = [10, 20, 30]

iterator = iter(numbers)

print("ITERATOR:")

print(next(iterator))
print(next(iterator))
print(next(iterator))

print()


# =========================================================
# SUMMARY
# =========================================================

print("DATA STRUCTURES USED:")
print("""
1. List
2. Tuple
3. Set
4. Dictionary
5. Stack
6. Queue
7. Priority Queue / Heap
8. Linked List
9. Tree
10. Graph
11. Iterator
12. BFS
13. DFS
""")
