def sup_rep (l):
    lc = []
    for i in l:
        if (i not in lc):
            lc.append(i)
    return lc

L = [10,20,30,20,10,50,60,40,80,50,40]

L = sup_rep(L)

print (L)