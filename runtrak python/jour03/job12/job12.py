def inv (x):
    r = ""
    for i in range (len(x)):
        r += x [-(i+1)]
    print (r)


inv (input ("donner la chaine a inverser : \n"))