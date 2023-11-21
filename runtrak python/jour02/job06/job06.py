def isprim(x):
    test = True
    for i in range (2, x):
        if (x % i == 0):
            test = False
    return test
for i in range (1, 101):
    if (isprim(i) == True):
        print (i)