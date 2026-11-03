class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.m = {}
        
    
    def addNode(self, new_node):
        temp = self.head.next
        new_node.next = temp
        new_node.prev = self.head
        self.head.next = new_node
        temp.prev = new_node
    
    def deleteNode(self, deleteNode):
        prev = deleteNode.prev
        nxt = deleteNode.next
        nxt.prev = prev
        prev.next = nxt

    def get(self, key: int) -> int:
        if key in self.m:
            resNode = self.m[key]
            ans = resNode.val
            del self.m[key]
            self.deleteNode(resNode)
            self.addNode(resNode)
            self.m[key] = self.head.next
            return ans
        return -1

        

    def put(self, key: int, value: int) -> None:
        # key exits:
        #   modify value
        # key not exits:
        #   insert key
        #       capacity full -> delete least recently key
        #       capacity not full -> insert key and value
        if key in self.m:
            curr = self.m[key]
            del self.m[key]
            self.deleteNode(curr)
        
        if self.capacity == len(self.m):
            del self.m[self.tail.prev.key]
            self.deleteNode(self.tail.prev)

        self.addNode(Node(key,value))
        self.m[key] = self.head.next
        
