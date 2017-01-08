from random import randint
count = 0
def experiment():
    global count
    for i in range(0, 100000):
        random_numbers = []
        for i in range(0, 23):
            random_numbers.append(randint(1, 366))
        for i in range(len(random_numbers)):
            toRemove = random_numbers[0]
            del random_numbers[0]
            if toRemove in random_numbers:
                count+=1
                break
        
experiment()
print (count)
    
