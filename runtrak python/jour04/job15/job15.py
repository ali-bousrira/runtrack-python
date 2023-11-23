def arond (l):
    lc = []
    for i in l:
        if (i % 1 < 0.5):
            lc.append(i // 1)
        else:
            lc.append((i // 1) +1)
    return lc

l = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

print (arond (l))