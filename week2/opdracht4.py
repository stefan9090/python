
def mybin(val):
    buf = ""
    assert type(val) == int
    if(val == 0):
        return '0'
    elif(val==1):
        return '1'
    else:
        return buf + str(mybin(val//2) + str(val % 2))
    
                          

print(mybin(16))
print(mybin(255))
                          


