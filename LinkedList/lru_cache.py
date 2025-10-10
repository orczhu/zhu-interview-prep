# TODO
# LRU cache, I am not sure where am I write_docstringdict

class LRUCache:
    """
    @param: capacity: An integer
    """
    class Node:
        def __init__(self, key: int, val: int):
            self.val = val
            self.key = key
            self.pre = None
            self.next = None
        
    def __init__(self, capacity):
        # do intialization if necessary
        self.cap = capacity
        # key is key value is Node
        self.lru_dict = {}
        self.head = self.Node(-1, -1)
        self.tail = self.Node(-1, -1)
        self.head.next = self.tail
        self.tail.pre = self.head
    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        # write your code here
        if key in self.lru_dict:
            # missing remove myself
            node = self.lru_dict[key]
            self.remove_myself(node)
            self.move_to_tail(node)
            return self.lru_dict.get(key).val
        else:
            return -1

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        # write your code here
        if key in self.lru_dict:
            # update key
            node = self.lru_dict[key]
            node.val = value
            self.remove_myself(node)
            self.move_to_tail(node)
            return
        # need to add new entry
        if len(self.lru_dict) == self.cap:
            self.remove_head()
        new_node = self.Node(key, value)
        self.lru_dict[key] = new_node
        self.move_to_tail(self.lru_dict.get(key))
    
    def remove_head(self) -> None:
        temp = self.head.next
        self.head.next = temp.next
        temp.next.pre = self.head
        self.lru_dict.pop(temp.key)
    
    def move_to_tail(self, node) -> None:
        temp = self.tail.pre
        temp.next = node
        node.next = self.tail
        node.pre = temp
    def remove_myself(self, node) -> None:
        node.pre.next = node.next
        node.next.pre = node.pre
    

