def is_number(d):
    try:
        float(d)
        return True
    except ValueError:
        return False


def int_input():
    n = input("Entrez un nombre : \n")
    while  not is_number(n):
        n = input("Entrez un nombre : \n")
    n = float(n)
    return n


def pos_ou_neg (n):
    if n < 0:
        print ("negatif")
    if n >= 0:
        print ("positif")


for i in range (5):
    pos_ou_neg (int_input ())