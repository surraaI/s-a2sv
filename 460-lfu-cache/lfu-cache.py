class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0, 0)  
        self.tail = Node(0, 0)  
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add_node(self, node: Node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def remove_node(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def pop_tail(self):
        if self.size > 0:
            tail_node = self.tail.prev
            self.remove_node(tail_node)
            return tail_node
        return None

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0
        self.key_node_map = {}
        self.freq_map = {}

    def _update_freq(self, node: Node):
        freq = node.freq
        self.freq_map[freq].remove_node(node)
        if not self.freq_map[freq].size:
            del self.freq_map[freq]
            if self.min_freq == freq:
                self.min_freq += 1

        node.freq += 1
        freq = node.freq
        if freq not in self.freq_map:
            self.freq_map[freq] = DoublyLinkedList()
        self.freq_map[freq].add_node(node)

    def get(self, key: int) -> int:
        if key not in self.key_node_map:
            return -1

        node = self.key_node_map[key]
        self._update_freq(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_node_map:
            node = self.key_node_map[key]
            node.value = value
            self._update_freq(node)
        else:
            if self.size == self.capacity:
                min_freq_list = self.freq_map[self.min_freq]
                node_to_remove = min_freq_list.pop_tail()
                del self.key_node_map[node_to_remove.key]
                self.size -= 1

            new_node = Node(key, value)
            self.key_node_map[key] = new_node
            if 1 not in self.freq_map:
                self.freq_map[1] = DoublyLinkedList()
            self.freq_map[1].add_node(new_node)
            self.min_freq = 1
            self.size += 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
