# 🌳 Binary Search Tree (BST)

A **Binary Search Tree (BST)** is a binary tree data structure in which each node has at most two children, and the tree maintains a specific ordering property.

## 📌 BST Property

For every node `N`:
- All values in the **left subtree** of `N` are **less than** `N.val`.
- All values in the **right subtree** of `N` are **greater than** `N.val`.


---

## ✅ Basic Operations

| Operation | Description                           | Time Complexity (Avg) | Time Complexity (Worst) |
|-----------|---------------------------------------|------------------------|--------------------------|
| Insert    | Add a new value                       | O(log n)               | O(n)                     |
| Delete    | Remove a node                         | O(log n)               | O(n)                     |
| Search    | Find a value in the tree              | O(log n)               | O(n)                     |
| Inorder   | Traverse in ascending order           | O(n)                   | O(n)                     |

---

## ⚙️ Common BST Algorithms

### 1. **Insert a Node**
```python
def insert(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root
