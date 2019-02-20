class Node:
    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt
    
    def __repr__(self):
        return "{0} -> {1}".format(self.value, self.next)

class SingleLinkedList:
    def __init__(self):
        self.begin = None
        self.end = None
    
    def push(self, obj):
        newNode = Node(obj, None)
        if not self.begin:
            self.begin = newNode
        else:
            self.end.next = newNode
        self.end = newNode
    
    def pop(self):
        if self.begin is None or self.begin.next is None:
            tmp = self.begin
            self.begin = None
            self.end = None
            return None if not tmp else tmp.value
        
        tmp = self.begin
        prev = None
        while(tmp.next):
            prev = tmp
            tmp = tmp.next
        prev.next = None
        self.end = prev
        return tmp.value
    
    def shift(self, obj):
        newNode = Node(obj, None)
        if self.begin is None:
            self.end = newNode
        else:
            newNode.next = self.begin
        self.begin = newNode
    
    def unshift(self):
        if not self.begin:
            return None
        tmp = self.begin
        self.begin = self.begin.next
        return tmp.value
    
    def remove(self, obj):
        if not self.begin:
            return None
        
        index = self.get_index(obj)
        if obj == self.begin.value:
            self.unshift()
            return index
        
        if obj == self.end.value:
            self.pop()
            return index
        
        self.root = tmp
        prev = None
        while(tmp.next):
            prev = tmp
            tmp = tmp.next
            if tmp.value == obj:
                break
        
        prev.next = tmp.next
        return index
    
    def first(self):
        return self.begin.value
    
    def last(self):
        return self.end.value
    
    def count(self):
        tmp = self.begin
        count = 0
        while(tmp):
            count += 1
            tmp = tmp.next
        return count
    
    def get(self, index):
        tmp = self.begin
        position = 0
        while(tmp):
            if position == index:
                return tmp.value
            position += 1
            tmp = tmp.next
        return None
    
    def get_index(self, value):
        if self.begin == None:
            return None
        tmp = self.begin
        count = 0
        while(tmp):
            if tmp.value == value:
                return count
            count += 1
            tmp = tmp.next
        return -1
    
    def dump(self, mark):
        print(mark)