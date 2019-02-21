class Node:
    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt

class Stack:
    def __init__(self):
        self.top = None
    
    def push(self, obj):
        newNode = Node(obj, None)
        if not self.top:
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode

    def pop(self):
        if not self.top:
            return None
        
        if not self.top.next:
            tmp = self.top
            self.top = None
            return tmp.value
        
        tmp = self.top
        self.top = tmp.next
        return tmp.value
    
    def peek(self):
        return self.top
    
    def count(self):
        count = 0
        tmp = self.top

        while(tmp):
            count += 1
            tmp = tmp.next
        
        return count
