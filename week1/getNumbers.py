def getNumbers(a):
    valid = []
    buff = []
    for i in range(len(a)):
        if ord(a[i])>47 and ord(a[i])<58:
            while True:
                buff += a[i]
                if ord(a[i])<47 and ord(a[i])>58 or i>len(a):
                    valid.append(buff)
                    break
                i+=1
    return valid

a = '123fe43'
print getNumbers(a)


