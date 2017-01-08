import queue

class myqueue(list):
    def __init__(self,a=[]):
        list.__init__(self,a)

    def dequeue(self):
        return self.pop(0)

    def enqueue(self,x):
        self.append(x)


class BSTNode:
    def __init__(self,element,left,right):
        self.element = element
        self.left = left
        self.right = right

    def __repr__(self,nspaces=0):
        s1 = ''
        s2 = ''
        s3 = ''
        if self.right != None:
            s1 = self.right.__repr__(nspaces + 3)
        s2 = s2 + ' '*nspaces + str(self.element) + '\n'
        if self.left != None:
            s3 = self.left.__repr__(nspaces + 3)
        return s1 + s2 + s3

    def height(self):
        if self.left:
            hleft = self.left.height()
        else:
            hleft = -1
        if self.right:
            hright = self.right.height()
        else:
            hright = -1
        return 1 + max(hleft,hright)

    def rinsert(self, data):
        if data == self.value:
            return False
        elif data>self.element:
            if self.right == None:
                self.right = BSTNode(data, None, None)
                return True
            else:
                self.right.rinsert(data)
        else:
            if self.left == None:
                self.left = BSTNode(data, None, None)
                return True
            else:
                self.left.rinsert(data)
        
    def insert(self,e):
        parent = self
        current = None
        found = False

        if parent.element < e:
            current = parent.right
        elif parent.element > e:
            current = parent.left
        else:
            found = True;

        while not found and current:
            parent = current
            if parent.element < e:
                current = parent.right
            elif parent.element > e:
                current = parent.left
            else:
                found = True

        if not found:
            if parent.element < e:
                parent.right = BSTNode(e,None,None)
            else:
                parent.left = BSTNode(e,None,None)
        return not found

    def insertArray(self,a, low=0, high=-1):
        if len(a) == 0:
            return
        if high == -1:
            high = len(a)-1
        mid = (low+high+1)//2
        self.insert(a[mid])
        if mid > low:
            self.insertArray(a,low,mid-1)
        if high > mid:
            self.insertArray(a,mid + 1,high)

    def search(self,e):
        current = self
        found = False
        while not found and current:
            if current.element < e:
                current = current.right
            elif current.element > e:
                current = current.left
            else:
                found = True
        if found:
            return current
        else:
            return None

    def search2(self,e):
        if self.element == e:
            return self
        parent = self.getParent(e)
        if parent == None:
            return None
        if parent.element < e:
            return parent.right
        return parent.left

    def rsearch(self, data):
        print("hi")
        if self.element == data:
            print("found")
            return "found"
        elif data > self.element:
            if self.right == None:
                return False
            else:
                self.right.rsearch(data)
        else:
            if self.left == None:
                return False
            else:
                self.left.rsearch(data)

    

    def getParent(self,e):
        parent = self
        current = None
        found = False

        if parent.element < e:
            current = parent.right
        elif parent.element > e:
            current = parent.left;
        else:
            return None

        while not found and current:
            if current.element == e:
                found = True
            else:
                parent = current
                if current.element < e:
                    current = current.right
                else:
                    current = current.left
        if found:
            return parent
        else:
            return None
        
    def parentMinRightTree(self):
        parent = self.right
        current = parent.left
        while current.left:
            parent = current
            current = current.left
        return parent

    def delete(self,e):
        parent = self.getParent(e);

        if parent == None:
            return False
        if parent.element < e:
            current = parent.right
            if current.left == None:
                parent.right = parent.right.right
                return True
            else:
                if current.right == None:
                    parent.right = parent.right.left
                    return True
        else:
            current = parent.left
            if current.left == None:
                parent.left = parent.left.right
                return True
            else:
                if current.right == None:
                    parent.left = parent.left.left
                    return True
        if current.right.left == None:
            current.element = current.right.element
            current.right = current.right.right
            return True
        node = current.parentMinRightTree()
        current.element = node.left.element
        node.left = node.left.right
        return True

class BST:
    def __init__(self,a=None):
        if a:
            mid = len(a)//2
            self.root = BSTNode(a[mid],None,None)
            self.root.insertArray(a[:mid])
            self.root.insertArray(a[mid+1:])
        else:
            self.root = None

    def __repr__(self):
        if self.root:
            return str(self.root)
        else:
            return 'null-tree'

    def height(self):
        if self.root:
            return self.root.height()
        else:
            return -1
    
    def showLevelOrder(self):
        q = myqueue()
        printable = []
        q.enqueue(self.root)
        atMax = False
        while True:
            
            for i in range(len(q)):
                current = q.dequeue()
                printable.append(current.element)
                if current.left:     
                    q.enqueue(current.left)
                if current.right:    
                    q.enqueue(current.right)
                if current.element == self.max():
                    atMax = True
            print(printable)
            printable.clear()
            if atMax:
                break
         
    def search(self,e):
        if self.root and e:
            return self.root.search(e)
        else:
            return None
        
    def rsearch(self, data):
        if self.root and data:
            self.root.rsearch(data)
        else:
            return False

    def insert(self,e):
        if e:
            if self.root:
                return self.root.insert(e)
            else:
                self.root = BSTNode(e,None,None)
                return True
        else:
            return False

    def rinsert(self, data):
        if self.root:
            self.root.rinsert(data)
        else:
            self.root = BSTNode(data, None, None)
        
        
    def max(self):
        current = self.root
        while current.right != None:
            current = current.right
        return current.element

    
    def delete(self,e):
        if self.root and e:
            if self.root.element == e:
                if self.root.left == None:
                    self.root = self.root.right
                elif self.root.right == None:
                    self.root = self.root.left
                elif self.root.right.left == None:
                    self.root.element = self.root.right.element
                    self.root.right = self.root.right.right
                else:
                    node = self.root.parentMinRightTree();
                    self.root.element = node.left.element
                    node.left = node.left.right
                return True
            else:
                return self.root.delete(e)
        else:
            return False

if __name__ == '__main__':
    b = BST([1,2,3, 8, 7])
    print(b)
    print("height = "+str(b.height()))
    print("max = "+str(b.max()))
    print("found? = "+str(b.search(1)))
    print("------------")
    b.showLevelOrder()
