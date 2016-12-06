def machtv3(a, n):
    assert n > 0
    m = 1
    n -= 1
    count = 0
    while n > 0:
        if n%2 == 0:
            n/=2
            a=a**2
        else:
            n-=1
            a=a*a
        count += 1
    print(count)
    return a
val = machtv3(2, 1000)
print(val)
