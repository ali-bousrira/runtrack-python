def dist (nb_march, haut):
    nb_parcour = 5 * 7 * 2
    haut_tt = nb_march * haut
    print ("Pour ", nb_march, "marches de ", haut, "cm, le gardien parcourt ", (haut_tt * nb_parcour) / 100, " m par semaine.")



dist (int(input("donnez le nombre de marche : \n")), int(input("donnez l'hauteur de chaque marche : \n")))