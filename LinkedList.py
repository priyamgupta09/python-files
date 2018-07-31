class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    def addNodeLast(self,data):
        newNode=Node(data)
        if(self.head==None):
            self.head=newNode
        else:
            ptr=self.head
            while(ptr.next!=None):
                ptr=ptr.next
            ptr.next=newNode
    
    def printList(self):
        ptr=self.head
        l=[]
        while(ptr!=None):
            l.append(ptr.data)
            ptr=ptr.next
        print(l)

    def reverseList(self):
        prev=None
        curr=self.head
        while(curr!=None):
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        self.head=prev

    def reverseRec(self,ptr):
        if(ptr.next==None):
            self.head=ptr
            return 0
        self.reverseRec(ptr.next)
        ptr.next.next=ptr
        ptr.next=None


l=LinkedList()
l.addNodeLast(6)
l.addNodeLast(5)
l.addNodeLast(3)
l.printList()
l.reverseList()
l.printList()
l.reverseRec(l.head)
l.printList()
