def somme_pair (l):
    s = 0
    for i in range (len(l)):
        if (l[i] % 2 == 0):
            s += l[i]
    return s

L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]

print ("la somme des valeurs paires est : \n", somme_pair (L))