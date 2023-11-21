
n = input("Entrez un entier supérieur a zero : \n")
while  (not n.isnumeric()) or (int(n) <= 0):
    n = input("Entrez un entier supérieur a zero : \n")
n = int(n)
print ("Table de multiplication de ", n)
for i in range (1, 11):
    print (i * n)