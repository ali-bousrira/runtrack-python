test = False
string = input("donne la chaine :\n")
for i in range(len(string)):
    if (string[i] == 'e'):
        test = True
if (test == False):
    print ("e nexiste pas dans la chaine")
else:
    print ("e exista dans la chaine")