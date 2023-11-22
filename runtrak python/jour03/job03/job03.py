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

def add (x, n):
    print ("La somme est : \n", x + n)

for i in range (5):
    add (int_input(), int_input())