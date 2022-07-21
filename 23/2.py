numbers = set()
def teleportation(now, counter):
    if (counter == 6): 
        numbers.add(now)
        return
    teleportation(now+1, counter+1)
    teleportation(now*3, counter+1)
teleportation(2, 0)
print(len(numbers))
