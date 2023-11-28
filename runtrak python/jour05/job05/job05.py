list_min = []
for i in range (ord ("a"), ord ("z")+1):
    list_min.append (chr (i))
list_maj = []
for i in range (ord ("A"), ord ("Z")+1):
    list_maj.append (chr (i))
print (list_min, "/",list_maj)


def cod (x, n):
    nouvx = ""
    l = len (list_maj)

    for i in range (len(x)):
        t = x[i]
        if (t in list_min):
            if (n > 0):
                if (n > l):
                    n = n % l
                if (list_min.index(t) + n > l):
                    n = list_min.index(t) + n - l
            if (n < 0):
                if (n < -l):
                    n = n % l
                if (list_min.index(t) + n < 0):
                    n = list_min.index(t) + n + l
            nouvx += list_min[list_min.index(t) + n]


        if (t in list_maj):
            if (n > 0):
                if (n > l):
                    n = n % l
                if (list_maj.index(t) + n > l):
                    n = list_maj.index(t) + n - l
            if (n < 0):
                if (n < -l):
                    n = n % l
                if (list_maj.index(t) + n < 0):
                    n = list_maj.index(t) + n + l
            nouvx += list_maj[list_maj.index(t) + n]
        if not (t in list_maj or t in list_min):
                nouvx += t


    print (nouvx)


cod (input ("intrrez un echaine : \n"), int(input ("entre le decalage : \n")))