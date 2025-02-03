class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.previous = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.previous = self.right, self.left
    
    def remove(self, node):
        previous, next = node.previous, node.next
        previous.next, next.previous = next, previous

    def insert(self, node):
        previous, next = self.right.previous, self.right
        previous.next = next.previous = node
        node.next, node.previous = next, previous

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)