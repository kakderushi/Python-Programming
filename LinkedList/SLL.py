class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        
class LinkedList:
    def __init__ (self,head=None):
        self.head=head
        #insetion of new node in linked list
        def append(self,new_node):
            current=self.head
            if current:
                while current.next:
                    current=current.next
                current.next=new_node
            else:
                self.head=new_node
    #Delete the first node wiht given value
        def delete(self,value):
            current=self.head
            if current.value==value:
                self.head=current.next
            else:
                while current:
                    if current.value==value:
                        break
                    prev=current
                    current=current.next
                    
                if current==None:
                    return 
                prev.next=current.next
                current=None