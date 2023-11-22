def int_input():
    n = input("Entrez un entier supérieur entre 0 et 20 : \n")
    while  (not n.isnumeric()) or (int(n) <= 0) or (float(n) > 20):
        n = input("Entrez un entier supérieur entre 0 et 20 : \n")
    return float(n)


def moyenne (x, y, z):
    return ((x + y + z) / 3)

moyenne_etudiant = moyenne (int_input(), int_input(), int_input())

if (20 >= moyenne_etudiant >= 15):
    print (" Trés bon élève")
if (14 >= moyenne_etudiant >= 11):
    print ("bon élève")
if (10 >= moyenne_etudiant >= 8):
    print ("Elèvz moyen")
if (7 >= moyenne_etudiant >=0):
    print ("Elève devant faire des efforts")