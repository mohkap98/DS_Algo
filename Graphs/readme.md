# 📊 Graphs in Data Structures and Algorithms (DSA)

Graphs are one of the most powerful and versatile data structures in computer science. They are widely used to model real-world problems like networks, maps, social connections, and more.

---

## 📌 What is a Graph?

A **Graph** is a collection of:
- **Vertices (Nodes)** – the fundamental units
- **Edges (Links)** – connections between the vertices

### Types of Graphs:

| Type               | Description                              |
|--------------------|------------------------------------------|
| Undirected Graph   | Edges have no direction (A - B)          |
| Directed Graph     | Edges have direction (A → B)             |
| Weighted Graph     | Edges have weights (A —3→ B)             |
| Unweighted Graph   | All edges are equal                      |
| Cyclic Graph       | Contains at least one cycle              |
| Acyclic Graph      | Contains no cycles                       |
| Connected Graph    | Every node can be reached from any other |
| Disconnected Graph | Some nodes are isolated                  |

---

## 🧠 Graph Representations

1. **Adjacency Matrix**
   - 2D array: `matrix[i][j] = 1` if edge exists between i and j
   - Space: O(V²)

2. **Adjacency List**
   - Dictionary/List of lists storing neighbors
   - Space: O(V + E)
   - **Preferred for sparse graphs**

---

## ⚙️ Common Graph Algorithms

| Algorithm                  | Purpose                          |
|----------------------------|----------------------------------|
| Breadth-First Search (BFS) | Explore neighbors level by level |
| Depth-First Search (DFS)   | Explore as deep as possible      |
| Topological Sort           | Sort nodes in a DAG              |
| Dijkstra’s Algorithm       | Shortest path (non-negative weights) |
| Bellman-Ford               | Shortest path (negative weights allowed) |
| Floyd-Warshall             | All-pairs shortest paths         |
| Prim’s Algorithm           | Minimum Spanning Tree (MST)      |
| Kruskal’s Algorithm        | Minimum Spanning Tree (MST)      |
| Union-Find (DSU)           | Cycle detection, connected comps |
| Tarjan's / Kosaraju's      | Strongly connected components    |

---

## 📦 Example: Adjacency List Representation in Python

```python
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = defaultdict(list)

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)  # for undirected graphs

    def print_graph(self):
        for key in range(self.V):
            print(f"{key} -> {self.adj[key]}")
