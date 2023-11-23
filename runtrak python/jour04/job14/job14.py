def my_long_word(n, x):
    c = 0
    t = ""
    tt = ""
    for i in x:
        if (i != " ") and (i != ","):
            c += 1
            t += i
        else:

            if (c >= n):
                tt += t
                tt += " "
                t = ""
                c = 0
            else:
                t = ""
                c = 0
    print (tt)

my_long_word(3, "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance")