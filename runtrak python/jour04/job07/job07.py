def mul_3 (l):
    c = 0
    for i in range (len(l)):
        if (l[i] % 3 == 0):
            c += 1
    return c

L = [8, 24, 48, 2, 16]

print ("le nombre de multiple de 3 est : \n", mul_3(L))