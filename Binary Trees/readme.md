# Binary Trees - Easy Explanation 🌳

## What is a Binary Tree?
A **Binary Tree** is a data structure where each node has at most **two children** (left and right).

Example:
```
    1
   / \
  2   3
 / \
4   5
```
- `1` is the **root** node.
- `2` and `3` are **children** of `1`.
- `4` and `5` are **children** of `2`.

## Types of Binary Trees 🏡
1. **Full Binary Tree**: Every node has **0 or 2** children.
2. **Complete Binary Tree**: All levels are filled except possibly the last, which is filled from left.
3. **Perfect Binary Tree**: All internal nodes have 2 children, and all leaf nodes are at the same level.
4. **Balanced Binary Tree**: The height difference between left and right subtrees is at most 1.
5. **Binary Search Tree (BST)**: Left child < Parent < Right child (used for efficient searching).

## Basic Operations ⚙️
1. **Insertion** - Add a node.
2. **Deletion** - Remove a node.
3. **Traversal** - Visit all nodes.

### Tree Traversal 🌲
1. **Inorder (Left → Root → Right)**:
   - Example: `4 → 2 → 5 → 1 → 3`
2. **Preorder (Root → Left → Right)**:
   - Example: `1 → 2 → 4 → 5 → 3`
3. **Postorder (Left → Right → Root)**:
   - Example: `4 → 5 → 2 → 3 → 1`
4. **Level Order Traversal (BFS)**:
   - Example: `1 → 2 → 3 → 4 → 5`

