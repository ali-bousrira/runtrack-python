type = input ("donner le type sois fruit ou legume : \n")
while (type.upper() != "FRUIT") and (type.upper() != "LEGUME"):
    type = input ("donner le type sois fruit ou legume : \n")

saison = input ("donner la saison : \n")
while (saison.upper() != "HIVER") and (saison.upper() != "ETE"):
    saison = input ("donner la saison : \n")


def fruit_leg (type, saison):
    if (type.upper() == "FRUIT") and (saison.upper() == "HIVER"):
        print ("orange, mandarine et kiwi")

    if (type.upper() == "FRUIT") and (saison.upper() == "ETE"):
        print ("Poire, fraise, cassis")

    if (type.upper() == "LEGUME") and (saison.upper() == "HIVER"):
        print ("carotte, topinambour, endire")

    if (type.upper() == "LEGUME") and (saison.upper() == "ETE"):
        print ("artichaut, aubergine, navet")


fruit_leg(type, saison)