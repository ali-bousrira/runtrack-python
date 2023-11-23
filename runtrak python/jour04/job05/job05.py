def is_number(d):
    try:
        int(d)
        return True
    except ValueError:
        return False


def int_input(x):
    n = input("Entrez un nombre entier n°{} : \n" .format(x))
    while  not is_number(n):
        n = input("Entrez un nombre entier n°{} : \n" .format(x))
    n = int(n)
    return n

L = []

for i in range (5):
    L.append (int_input(i+1))

print ("la deuxiem valeur de cette list est : \n", L [1])

def change (list):
    list[3] = list[2] + list[4]
    return list

print ("et la list modifier est : \n", change (L), "\n et la derbieur valeur est : \n", L[-1])
