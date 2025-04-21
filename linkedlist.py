class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtBegin(self, val):
        newNode = Node(val)
        
        if self.head == None:
            self.head = newNode
            return
        
        ptr = self.head
        while ptr.next:
            ptr = ptr.next
        ptr.next = newNode
    
    def printList(self):
        ptr = self.head
        while ptr:
            print(f"{ptr.data} ->", end=" ")
            ptr=ptr.next
            
listt = LinkedList()
[listt.insertAtBegin(i*8) for i in range(2, 10)]
listt.printList();

