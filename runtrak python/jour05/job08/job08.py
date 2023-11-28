def tri_inser (tab):
    #initialisation du compteur
    c = 0
    for i in range(1, len(tab)): 
        k = tab[i] 
        j = i-1
        #virification du rangement
        while j >= 0 and k < tab[j] : 
            tab[j + 1] = tab[j] 
            j -= 1
            #incrementation du compteur
            c += 1
        tab[j + 1] = k
    return c


tab = [64, 90, 34, 32, 25, 22, 63, 12, 10, 11]
print("Nombre total de coups nécessaires pour trier la liste : ", tri_inser (tab), "\n", tab)
