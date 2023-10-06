class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
    def setNext(self,next):
        self.next = next
    def getNext(self):
        return self.next
    
if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node1.setNext(node2)
    node2.setNext(node3)
    node_tmp = node1 
    while node_tmp:
        print(node_tmp.data)
        node_tmp = node_tmp.next 
