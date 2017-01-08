class ListNode:
    def __init__(self,data,next_node):
        self.data = data
        self.next = next_node

    def __repr__(self):
        return str(self.data)

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        s = ''
        current = self.head
        if current != None:
            s = s + str(current)
            current = current.next
        while current != None:
            s = s + " -> " + str(current)
            current = current.next
        if not s: # s == '':
            s = 'empty list'
        return s

    def addLast(self,e):
        if not self.head: # self.head == None:
            self.head = ListNode(e,None)
            self.tail = self.head
        else:
            n = ListNode(e,None)
            self.tail.next = n
            self.tail = self.tail.next

    def delete(self,e):
        if self.head: # self.head != None:
            if self.head.data == e:
                self.head = self.head.next
                if self.head == None:
                    self.tail = None
            else:
                current = self.head
                while current.next != None and current.next.data != e:
                    current = current.next
                if current.next != None:
                    current.next = current.next.next
                if current.next == None:
                    self.tail = current

class MyCircularList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def __repr__(self):
        s = ''
        current = self.head
        index = 0
        while index != self.size:
            s = s + " -> " + str(current)
            current = current.next
            index+=1
        return s
    def append(self, data):
        if not self.size:
            self.head = ListNode(data, self.head)
            self.size += 1
        elif self.size == 1:
            self.tail = ListNode(data, self.head)
            self.head.next = self.tail
            self.size += 1
        else:
            newNode = ListNode(data, self.head)
            self.tail.next = newNode
            self.tail = self.tail.next
            self.size += 1
    def delete(self,data):
        if self.size:
            if self.head.data == data:
                if self.size==1:
                    self.head = None
                    self.tail = None
                    self.size = 0
                else:
                    self.head = self.head.next
                    self.size -= 1
                    print("self.head deleted")
            else:
                current = self.head
                while current.next != self.head and current.next.data != data:
                    current = current.next
                current.next = current.next.next
                self.size -= 1
                print("Some node deleted")
                
                    
                    
if __name__ == '__main__':
    mylist =  MyCircularList()
    mylist.append(5)
    mylist.append(6)
    mylist.append(7)
    mylist.delete(7)
    print(mylist)
