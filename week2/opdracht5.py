def check(a,i):  # ga na of i aan a toegevoegd kan worden
    n = len(a)
    return not (i in a or # niet in dezelfde kolom 
                i+n in [a[j]+j for j in range(n)] or # niet op dezelfde diagonaal 
                i-n in [a[j]-j for j in range(n)]) # niet op dezelfde diagonaal

#def valid(a,i):
     

def printQueens(a):
    n = len(a)
    for i in range(n):
        for j in range(n):
            if a[i] == j:
                print("X", end= " ")
            else:
                print("*", end= " ")
        print()
    print()

def rsearch(N):
    global a
    for i in range(N):
        if check(a,i):
            a.append(i)
            if len(a) == N:
                print("done")
                del a[0:]
                a[0]+=1
                
                return True
            else:
                if rsearch(N):
                    return True
            del a[-1] # verwijder laatste element
    return False


index = 0
a = [7] # a geeft voor iedere rij de kolompositie aan
t = 0



rsearch(8)
print(a)
printQueens(a)

#===========================================================


