
def mybin(val):
    temp = ""
    assert type(val) == int
    if(val == 0):
        return '0'
    elif(val==1):
        return '1'
    else:
        return temp + str(mybin(val//2) + str(val % 2)


tm = mybin(6)
print(tm)
                          


