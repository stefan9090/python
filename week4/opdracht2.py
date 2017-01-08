import random
myDict = {}

while True:
    x = random.random()
    hashX = hash(x)
    print(str(hashX) + ": " + str(x))
    if hashX in myDict.keys():
        print("hash("+str(x)+")==hash("+str(myDict[hashX])+")=="+str(hashX))
        break
    else:
        myDict[hashX] = x

