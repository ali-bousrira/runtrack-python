def draw_rectangle (width, height):
    line = ""
    test = False
    for i in range (height):
        line = ""
        if (i == 0) or (i == height-1):
            test = True
        else:
            test = False
        for j in range (width):
            if (j == 0) or (j == width-1):
                line += "|"
            elif (test == False):
                line += " "
            elif (test == True):
                line += "-"
        print (line)
                


draw_rectangle(10, 3)