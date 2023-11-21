def int_input():
    n = input("Entrez un entier supérieur a zero : \n")
    while  (not n.isnumeric()) or (int(n) <= 0):
        n = input("Entrez un entier supérieur a zero : \n")
    n = int(n)
    return n

def rec(a, b, c):
    rect = False
    if (a)**2 == (b)**2 + (c)**2:
        rect = True
    if (b)**2 == (a)**2 + (c)**2:
        rect = True
    if (c)**2 == (a)**2 + (b)**2:
        rect = True
    return rect

def iso (a, b, c):
    isot = False
    if (a == b) or (a == c) or (b == c):
        isot = True
    return isot

def equi (a, b, c):
    equit = False
    if (a == b == c):
        equit = True
    return equit

def istrian(a, b ,c):
    istriant = False
    if (a + b > c) and (a + c > b) and (b + c > a):
        istriant = True
    return istriant

a = int_input()
b = int_input()
c = int_input()

if not(istrian(a, b, c)):
    print ("on ne peut pas faire un trianbge avec ses trois longeurs")
else:
    print ("one peut crer un triangle avec se s trois longeurs")
    if (equi(a, b, c)):
        print ("se triangle est equilatéral")
    elif (rec(a, b, c)) and (iso(a, b, c)):
        print ("se triangle est rectangle est isocele")
    elif (rec(a, b, c)):
        print ("se triangle est rectangle")
    elif (iso(a, b, c)):
        print ("se triangle est isocele")
    else:
        print ("se triangle est quelconque")
