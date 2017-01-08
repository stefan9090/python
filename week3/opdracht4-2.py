

class trieNode():
    def __init__(self):
        self.child = {}
        self.count = 0
    def insert(self, char):
        self.child[char] = trieNode()
    def __repr__(self):
        return str(self.child.items())+str(self.count)

class trie():
    def __init__(self):
        self.root = trieNode()
        
    def __repr__(self):
        for i in self.root.child.keys():
            if self.root.child[i].count == 0:
                print(i)
        return ' '
    
    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.child.keys():
                current.insert(char)
            current = current.child[char]
        current.count += 1
        
    def getCount(self, word):
        current = self.root
        for char in word:
            current = current.child[char]
        print(current.count)

    def getWords(self):
        current = self.root
        buffer = ''
        while True:
            for i in current.child.keys():
                print(i)
                current = current.child[i]

myTrie = trie()

file = open("someText.txt", "r")
f = file.read()
f = f.lower()
buf = list(f)
invalid = ',.?;:()=+-_'
filtered = ""
x = 0
while x<len(buf):
    if buf[x] in invalid:
        buf[x] == ' '
    else:
        filtered+=buf[x]
    x+=1

for words in filtered.split():
    myTrie.insert(words)

myTrie.getWords()

#print(myTrie)

file.close()

