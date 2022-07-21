def year(now, finish):
    if (now == finish): 
        return 1
    if ((now > finish) or (now in [13, 33])):
        return 0
    return year(now+1, finish) + year(now+4, finish) + year(now*2, finish)

print(year(3, 19)*year(19, 34))
