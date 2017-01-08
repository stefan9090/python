import math
def mymax(a):
    max = math.inf
    for i in a:
        assert type(i in [int, float])
        if i>max:
            max = i
    return max

s
a = [1, 2, -4, 100]
print (mymax(a))


