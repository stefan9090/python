def money(maxJ, m):
    maxI = 0
    while(m[maxI]<maxJ):
        maxI+=1
    maxJ+=1
    a = [[0 for x in range(maxJ)]for y in range(maxI)]
    for i in range(len(a[0])):
        a[0][i] = 1
    
    for i in range(1, maxI):
        for j in range(maxJ):
            if j>=m[i]:
                a[i][j] = a[i-1][j]+a[i][j-m[i]]
            elif j<m[i]:
                a[i][j] = a[i-1][j]
    #for x in a:
    #    print(x)
    return a[maxI-1][maxJ-1]

m = [1,2,5,10,20,50,100,200,500,1000,2000,5000,10000]
print(money(7, m))
