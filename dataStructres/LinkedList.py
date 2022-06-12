class Node:
    def __init__(self,data,next=None) :
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self,head=None):
        self.head = head

    def deleteAtPosition(self,index):
        if index==0:
            self.head = self.head.next
            return
        temp = self.head
        counter = 0
        while temp.next!=None:
            counter = counter+1
            if counter == index:
                
                temp.next = temp.next.next

            temp=temp.next
        
            
    def insertAtStart(self,value):
        if self.head==None:
            self.head = Node(value)
            return 
        head_prev = self.head
        self.head = Node(value)
        self.head.next = head_prev
        
    def printLinkedList(self):
        temp=self.head
        while temp.next != None:
            print(temp.data,end=' -> ')
            temp=temp.next
        print(temp.data)

    def insertAtEnd(self, value):
        if self.head==None:
            self.head = Node(value)
            return
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next=Node(value)
        return


def main():
    obj =  LinkedList()
    obj.insertAtEnd(2)
    obj.insertAtEnd(3)
    obj.insertAtStart(1)
    obj.insertAtEnd(4)
    obj.printLinkedList()


if __name__ == "__main__":
    main()