def max (l):
    max = l[0]
    for i in range (len(l)):
        if (l[i] > max):
            max = l[i]
    return max

def min (l):
    min = l [0]
    for i in range (len(l)):
        if (min > l[i]):
            min = l[i]
    return min

L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

print ("la valeur max est : ", max (L), "\n la valeur min est : ", min (L))