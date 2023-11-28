def draw_rect_dia (n):
    n += 2
    line = ""
    t = n - 1
    for i in range (n):
        line = ""
        if (i == 0) or (i == n - 1):
            test = True
        else:
            test = False
        for j in range (n):
                if (test == True):
                    if (j == 0) or (j == n - 1):
                         line += "+"
                    else:
                         line += "-"
                else :
                    if (j - t == 0):
                          line += " "
                    else:
                         line += "#"
        print (line)
        t -= 1


draw_rect_dia (10)