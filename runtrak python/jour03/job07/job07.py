def test_lang (language):
    if (language.upper() == "JAVASCRIPT"):
        print ("tu es un développeur web")
    elif (language.upper() == "PYTHON"):
        print ("tu est un développeur IA")
    elif (language.upper() == "JAVA"):
        print ("tu es un dévelopeur logiciel")

language = input ("donner la langue de codage : \n")
while (language.upper() != "JAVASCRIPT") and (language.upper() != "PYTHON") and (language.upper() != "JAVA"):
    language = input ("donner la langue de codage : \n")


test_lang (language)