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


def test_paire (x):
    if ((x % 2) == 0):
        print ("se nombre est paire")
    else:
        print ("se nombre est impaire")


for i in range (5):
    test_paire (int_input())