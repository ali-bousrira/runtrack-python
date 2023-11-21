chain = "abcdefghijklmnopqrstuvwxyz" * 10
for i in range (len(chain)+1):
    x = ""
    for j in range (i):
        x += chain[j]
    print (x)