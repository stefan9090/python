def mymax(a):
    max = 0
    for i in a:
        assert (i>0), "i==0"
        assert (type(i)==int), "i is not a int"
        if i>max:
            max = i
    return max


a = [3, 4, 4, 100]
print mymax(a)


