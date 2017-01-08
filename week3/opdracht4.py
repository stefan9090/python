def getFreq():
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
    myDict = {}
    for word in filtered.split():
        if word not in myDict:
            myDict[word] = 1
        else:
            myDict[word] = myDict.get(word)+1
    return myDict
    
    file.close

def writeFreq(myDict):
    file = open("freqTabel.txt", "w")
    for k, v in sorted(myDict.items()):
        file.write(k + ': '+str(v)+'\n')
    file.close()

writeFreq(getFreq())

    
    



