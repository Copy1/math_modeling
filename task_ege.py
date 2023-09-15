F=(x or y) and (not(y==z)) and not(w)
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f=(x or y) and (not(y == 2)) and not (w)
                print(x, y ,z, w, int(F))