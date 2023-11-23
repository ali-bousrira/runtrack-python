def prod (l):
    s = 1
    for i in range (len(l)):
        if (90 >= l[i] >= 25):
            s *= l[i]
    if (s != 1):
        return s
    else:
        return "pas de valeur entre 25 et 90"    

L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

print ("la somme des valeurs entre 25 et 90 est : \n", prod(L))