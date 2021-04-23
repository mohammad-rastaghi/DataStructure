class Node:
    def __init__(self, data):
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
            if last_node.next is None:
                last_node.next = newNode
                break
            last_node = last_node.next
    
    def listIsEmpty(self):
        if self.head is None:
            return True
        else:
            return False
    
    def printer(self):
        if self.listIsEmpty():
            print('your linked list is Empty!!')
            return
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next
            
                

#first
firstNode = Node('adam')
#second
secondNode = Node('Harry')
#third
thirdNode = Node('jean')
linked = LinkedList()
linked.insertEnd(firstNode)
linked.insertEnd(secondNode)
linked.insertEnd(thirdNode)
linked.printer()