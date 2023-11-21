nom = "lenovo legion 5"
prix = 780
qtst = 52
print (nom)
print (prix)
print (qtst)
achat = int(input('combient voulez vous acheter inferieur a : '+ str(qtst ) + '\n'))
while achat>qtst:
    achat = int(input('combient voulez vous acheter inferieur a : '+ str(qtst) + '\n'))
qtst -= achat
print ('il rest que ', qtst)
print ('le prix a augmenter de 10%')
prix += (prix/100)*10
print (nom)
print (prix)
print (qtst)