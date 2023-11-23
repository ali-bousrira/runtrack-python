def switche_l (l):
    if (l == []):
        print ("la list est vide")

    else:
        x = l[-1]
        l[-1] = l[0]
        l[0] = x
        print (l)

    
switche_l ([])
switche_l ([1,2,3,4,5])