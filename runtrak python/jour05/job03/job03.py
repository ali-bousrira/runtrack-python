def draw_trian (x):
    t = t1 = x - 1
    test = False
    for i in range (x):
        if (i == x - 1):
            test = True
        line = ""
        for j in range (x * 2):
            if (test == False):
                if (j - t == 0):
                    line += "/"
                if (j - t1 == 1):
                    line += "\\"
                else:
                     line += " "
            if (test == True):
                if (j - t == 0):
                    line += "/"
                elif (j - t1 == 1):
                    line += "_\\"
                else:
                     line += "_"
        t -= 1
        t1 += 1 
        print (line)



draw_trian (10)