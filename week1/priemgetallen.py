import math
    
def getPrime(min, max):
    numbers = []
    for i in range(min, max):
        numbers.append(i)
    limit = int(math.sqrt(max))
    for i in range(1, limit+1):
        c = 0
        a = 2
        while c<max:
            c = numbers[i] * a
            if c in numbers:
                numbers.remove(c)
            a+=1
    return numbers
            
getallen = getPrime(1, 1000)

print (getallen)
