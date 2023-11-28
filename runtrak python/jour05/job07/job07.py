def note (x):
    for i in x :
        t = i % 10
        if (t == 0)  or (t == 1) or (t == 2) or (t == 6) or (t == 7):
            x[x.index(i)] = i

        else:
            if (t > 5):
                print (t)
                x[ x.index(i) ] = ((i // 10) *10) + 10
            else:
                x[ x.index(i) ] = ((i // 10) *10) + 5


lis = [90,91,92,93,94,95,96,97,98,99,100]

note (lis)
print (lis)