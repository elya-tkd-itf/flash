def command(now, finish):
    if (now == finish): 
        return 1
    if (now > finish):
        return 0
    return command(now+1, finish) + command(now+50, finish)

print(command(12, 137))