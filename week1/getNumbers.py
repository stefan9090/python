def getNumbers(string):
    returnList = []
    numbers = ""
    for i in string:
        if i>='0' and i <='9':
            numbers+=i
        elif len(numbers)>0:
            returnList.append(numbers)
            numbers = ""
    returnList.append(numbers)
    return returnList
a = '123fe43he567'
print (getNumbers(a))


