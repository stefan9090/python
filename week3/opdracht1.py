def check(a,i):  # ga na of i aan a toegevoegd kan worden
    n = len(a)
    return not (i in a or # niet in dezelfde kolom 
                i+n in [a[j]+j for j in range(n)] or # niet op dezelfde diagonaal 
                i-n in [a[j]-j for j in range(n)]) # niet op dezelfde diagonaal

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
                print(a)
            else:
                rsearch(N)        
            del a[-1] # verwijder laatste element

a = [] # a geeft voor iedere rij de kolompositie aan
t = 0

rsearch(10)
printQueens(a)

#===========================================================

#from itertools import permutations
#print()
# = 8
#cols = range(n)
#for vec in permutations(cols):
#    if n == len(set(vec[i]+i for i in cols)) \
#         == len(set(vec[i]-i for i in cols)):
#        print (vec )


