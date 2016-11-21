import math
    
def getPrime(min, max):
    numbers = []
    for i in range(min, max):
        numbers.append(i)
    print len(numbers)
    print min
    limit = int(math.sqrt(max))
    for i in range(0, limit+1):
        print i
        c = 0
        a = 2
        while c<max:
            c = numbers[i] * a
            if c in numbers:
                numbers.remove(c)
                #print "remove: "+str(c)
            a+=1
    return numbers
            
getallen = getPrime(0, 1000)

print getallen
