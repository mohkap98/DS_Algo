# Trie (Prefix Tree) Data Structure

## 📘 What is a Trie?

A **Trie** (pronounced "try") is a type of search tree used to efficiently store and retrieve keys in a dataset of strings. It is commonly used for **autocomplete**, **spell checking**, and **prefix-based searching**.

Each node in a trie represents a single character, and strings are stored character by character in a path from the root to a node marked as "end of word".

---

## 🔧 Use Cases
- Dictionary word lookup
- Auto-complete in search bars
- Spell checker
- IP routing (longest prefix match)
- Word games like Boggle or Scrabble

---

## 🧱 Trie Node Structure

Each node typically contains:
- A hash map (`children`) to point to its child nodes
- A boolean flag (`is_end_of_word`) to mark the end of a valid word

---

## 🧠 Operations

### 1. **Insert a word**
- Traverse each character of the word
- If a character is not present, add a new node
- Mark the final node as `end of word`

### 2. **Search for a word**
- Traverse the trie using the characters of the word
- If you reach a node marked as `end of word`, return true

### 3. **Check for a prefix**
- Similar to search, but you don’t need to check `is_end_of_word`

---

## 🧪 Example (Python)

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end_of_word = True

    def search(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.is_end_of_word

    def starts_with(self, prefix):
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True
