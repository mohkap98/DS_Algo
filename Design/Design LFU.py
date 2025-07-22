from sortedcontainers import SortedDict

class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.count = 1
        self.prev = self.next = None

class DLL:
    def __init__(self):
        self.front = ListNode(-1, -1)
        self.rear = ListNode(-1, -1)
        self.front.next = self.rear
        self.rear.prev = self.front

    def insert_node(self, node):
        # Insert at front (most recently used in this freq)
        next_node = self.front.next
        self.front.next = node
        node.prev = self.front
        node.next = next_node
        next_node.prev = node

    def remove_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        node.prev = node.next = None

    def pop_LRU(self):
        if self.is_empty():
            return None
        lru = self.rear.prev
        self.remove_node(lru)
        return lru

    def is_empty(self):
        return self.front.next == self.rear

class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.key_to_node = {}
        self.freq_to_DLL = SortedDict()

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1

        node = self.key_to_node[key]
        freq = node.count

        # Remove from current freq DLL
        self.freq_to_DLL[freq].remove_node(node)
        if self.freq_to_DLL[freq].is_empty():
            del self.freq_to_DLL[freq]

        # Move to next freq
        node.count += 1
        self.freq_to_DLL.setdefault(node.count, DLL()).insert_node(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return

        if key not in self.key_to_node:
            if len(self.key_to_node) >= self.cap:
                # Evict LFU and LRU
                min_freq = next(iter(self.freq_to_DLL))
                lru_node = self.freq_to_DLL[min_freq].pop_LRU()
                del self.key_to_node[lru_node.key]
                if self.freq_to_DLL[min_freq].is_empty():
                    del self.freq_to_DLL[min_freq]

            new_node = ListNode(key, value)
            self.key_to_node[key] = new_node
            self.freq_to_DLL.setdefault(1, DLL()).insert_node(new_node)

        else:
            # Update value and frequency
            node = self.key_to_node[key]
            node.val = value
            freq = node.count

            self.freq_to_DLL[freq].remove_node(node)
            if self.freq_to_DLL[freq].is_empty():
                del self.freq_to_DLL[freq]

            node.count += 1
            self.freq_to_DLL.setdefault(node.count, DLL()).insert_node(node)
