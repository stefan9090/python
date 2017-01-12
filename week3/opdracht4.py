class treeNode:
    def __init__(self):
        self.n = 0
        self.d = dict()
    def writeWordsToFile(self, filename):
        file = open(filename, "w")
        self.writeToFile(file)
    def writeToFile(self, file):
        current = self
        if current.d:
            for x in sorted(current.d.keys()):
                if current.d[x].n:
                    file.write(x + ': ' + str(current.d[x].n) + '\n')
                current.d[x].writeToFile(file)

class tree:
    def __init__(self):
        self.root = treeNode()
    def insert(self, word):
        current = self.root
        buffer = ''
        for char in word:
            buffer+=char
            if not buffer in current.d:
                current.d[buffer] = treeNode()
        current.d[buffer].n+=1
        current = current.d[buffer]
    def writeDataToFile(self, filename):
        self.root.writeWordsToFile(filename)

def openFile(filename):
    file = open(filename, "r")
    print("Reading file: "+filename+"...")
    f = file.read()
    f = f.lower()
    buf = list(f)
    invalid = ',.?;:()=+-_'
    filtered = ""
    for i in buf:
        if i.isalpha():
            filtered+=i
        else:
            filtered+=' '
    file.close
    return filtered

def getFreqTree(filename):
    words = openFile(filename)
    myTree = tree()
    print("Inserting words into tree...")
    for word in words.split():
        myTree.insert(word)
    return myTree
          
def writeFreqTree(myTree, filename):
    print("Words written to file: "+filename)
    myTree.writeDataToFile(filename)      

def getFreq(filename):
    words = openFile(filename)
    myDict = {}
    print("Inserting words into dictionary...")
    for word in words.split():
        if word not in myDict:
            myDict[word] = 1
        else:
            myDict[word] = myDict.get(word)+1
    return myDict
    

def writeFreq(myDict, filename):
    file = open(filename, "w")
    print("Words written to file: "+filename)
    for k, v in sorted(myDict.items()):
        file.write(k + ': '+str(v)+'\n')
    file.close()

def compareFiles(filename1, filename2):
    print("\nComparing files: "+filename1+" and "+filename2+"...")
    return openFile(filename1)==openFile(filename2)

writeFreq(getFreq("kjv.txt"), "freqTable.txt")
writeFreqTree(getFreqTree("kjv.txt"), "freqTableTree.txt") 
print(compareFiles("freqTableTree.txt", "freqTable.txt"))
    



