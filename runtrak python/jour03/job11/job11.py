def time_to_test (x):
    heure = int(x) // 60
    min = int(x) % 60
    print (heure, "heures et ", min,"minutes")

n = input("Entrez le nombres de minutes : \n")
while  (not n.isnumeric()) or (int(n) <= 0):
    n = input("Entrez le nombres de minutes : \n")

time_to_test (n)