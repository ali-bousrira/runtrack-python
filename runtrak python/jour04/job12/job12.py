def tri(l):
    c = 0
    for i in l:
        k = i 
        j = c-1
        while j >= 0 and k < l[j] : 
                l[j + 1] = l[j] 
                j -= 1
        l[j + 1] = k
        c += 1


L = [8, 24, 27, 48, 48, 2,16, 9, 102, 7, 84, 91]

tri (L)

print (L)