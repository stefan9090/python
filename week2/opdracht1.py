def machtv3(a, n):
    assert n > 0
    m = 1
    count = 0
    while n > 0:
        if n%2 == 0:
            n/=2
            a = a * a
        else:
            n-=1
            m=m*a
        count += 1
    print(count)
    return m
val = machtv3(2, 1000)
print(val)
print(2**1000)
print("============")
val = machtv3(14, 101)
print(val)
print(14**101)
