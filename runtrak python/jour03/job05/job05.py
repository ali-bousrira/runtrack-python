def input_op ():
    x = input("donner l'operateur sois +,-,*,/,% : \n")
    while (x != "*") and (x != "+") and (x != "-") and (x != "/") and (x != "%") :
        x = input("donner l'operateur sois +,-,*,/,% : \n")
    return (x)


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


def calcule (num1, operator, num2):
    if (operator == "*"):
        print (num1 * num2)

    if (operator == "+"):
        print (num1 + num2)

    if (operator == "-"):
        print (num1 - num2)

    if (operator == "/"):
        print (num1 / num2)

    if (operator == "%"):
        print (num1 % num2)


calcule (int_input(), input_op(), int_input())
