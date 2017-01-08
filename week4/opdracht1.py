class hashEntry:
    def __init__(self,element,isActive):
        self.element = element
        self.isActive = isActive

class hashTable:
    def __init__(self, size):
        self.size = size
        self.table = [set()] * size
        for i in range(self.size):
            self.table[i] = set()
        self.used = 0
        
    def __repr__(self):
        #return "\n".join([str(for i in list(x)) for x in self.table )
        toReturn = '====Hash Table====\n'
        for x in range(len(self.table)):
            toReturn += str(x) + ": "
            for i in list(self.table[x]):
                toReturn += str(i.element) + ' '
            toReturn += '\n'
        return toReturn
    
    def getPos(self, element):
        return hash(element)%self.size
    
    def insert(self, e):
        current = self.getPos(e)
        self.table[current].add(hashEntry(e, True))
        self.used += 1
        buf = self.size
        if self.used > 0.75*buf:
            self.rehash(self.size*2)
        
    def delete(self, e):
        current = self.getPos(e)
        buffer = list(self.table[current])
        for i in range(len(buffer)):
            if e == buffer[i].element:
                del buffer[i]
                self.used-=1
                print("Removed: " + str(e) + " Index = " + str(self.search(e)))
                break
        self.table[current] = set(buffer)
        
    def search(self, e):
        current = self.getPos(e)
        buffer = list(self.table[current])
        for i in range(len(buffer)):
            if buffer[i].element == e:
                return current
        return -1
    
    def rehash(self, newSize):
        if newSize > self.size:
            oldSize = self.size
            oldTable = self.table

            self.size = newSize
            self.table = [set()]*self.size
            for x in range(self.size):
                self.table[x] = set()

            for i in range(oldSize):
                buffer = list(oldTable[i])
                for x in buffer:
                    self.insert(x.element)
            print(self)
                   


import random
from datetime import datetime
random.seed(datetime.now())

table = hashTable(10)

randomNumbers = []
for i in range(200):
    buf = random.random()
    table.insert(buf)
    randomNumbers.append(buf)
for i in range(100):
    del randomNumbers[randomNumbers.index(random.choice(randomNumbers))]
for i in randomNumbers:
    table.delete(i)



