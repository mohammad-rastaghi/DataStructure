class Node:
    def __init__(self.data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertEnd(self, newNode):
        if self.head is None:
            self.head = newNode
            return
        last_node = self.head
        while True:
            if last_node is None:
                last_node = newNode
                break
            last_node = last_node.next
    
    def listIsEmpty(self):
        if self.head is None:
            return True
        else:
            return False
            