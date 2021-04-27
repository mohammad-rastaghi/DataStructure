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
    
    def insertHead(self, newNode):
        if self.listIsEmpty():
            self.head = newNode
            return
        temp = self.head
        self.head = newNode
        newNode.next = temp

    def insertAt(self, newNode, position):
        if self.listIsEmpty() is False:
            if position is 0:
                self.insertHead(newNode)
                return
            if position < 0 or position > self.listlength():
                print('your input position is Invalid!!')
                return
            currentNode = self.head
            currentPosition = 0
            while True:
                if currentPosition == position:
                    newNode.next = prevNode.next
                    prevNode.next = newNode
                    break
                prevNode = currentNode
                currentNode = currentNode.next
                currentPosition += 1
        else:
            print('your list is Empty!!')

    def deleteEnd(self):
        if self.listIsEmpty() is False:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    del lastNode
                    preNode.next = None
                    break
                preNode = lastNode
                lastNode = lastNode.next
        else:
            print('Your list is Empty.Delete operation was failed!!')

    def deleteHead(self):
        if self.listIsEmpty() is False:
            preHead = self.head
            self.head = preHead.next
            preHead.next = None
            del preHead
            return
        else:
            print('sorry! your list is Empty and delete operation was Failed!')

    def listlength(self):
        if self.listIsEmpty():
            return 0
        length = 0
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            currentNode = currentNode.next
            length += 1
        return length
 
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
#forth
forthNode = Node('sara')
linked = LinkedList()
linked.insertEnd(firstNode)
linked.insertEnd(secondNode)
linked.insertHead(thirdNode)
linked.insertAt(forthNode, 1)
linked.deleteHead()
linked.printer()