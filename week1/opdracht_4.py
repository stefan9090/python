from random import randint
count = 0
for i in range(0, 100):
    random_numbers = []
    for i in range(0, 23):
        random_numbers.append(randint(1, 365))
    for i in range(len(random_numbers)):
        toRemove = random_numbers[0]
        del random_numbers[0]
        if toRemove in random_numbers:
            count+=1

print count
    
