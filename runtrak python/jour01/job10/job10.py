mtini = int(input('montant initial de l’investissement : \n'))
tard = int(input('taux de rendement annuel : \n'))
while tard>100 :
    tard = int(input('taux de rendement annuel : \n'))
mtini += 5000
tard += 2
print ("l'invertisseur a ajouter 5 000euros donc le montant devient " , mtini , "et le taux devient ", tard)
mtini -= (mtini/100)*10
tard -= 1
print ("l'inverstisseur a retirer ", mtini, 'ducou le taux de rendement tombe a ', tard)