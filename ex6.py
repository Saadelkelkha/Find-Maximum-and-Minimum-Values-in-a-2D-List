t = []

for i in range(0, 4):
    l = []
    for j in range(0, 6):
        n = int(input("Type number: "))
        l.append(n)
    t.append(l)

for j in range (6):
    max = t[0][j]
    min = t[0][j]
    for i in range(4):
        if max<t[i][j] :
            max=t[i][j]
        if min>t[i][j] :
            min>t[i][j]
    print("the maximum in column",j+1,"is :",max)
    print("the minimum in column",j+1,"is :",min)

for i in range (4):
    max = t[i][0]
    min = t[i][0]
    for j in range(6):
        if max<t[i][j] :
            max=t[i][j]
        if min>t[i][j] :
            min>t[i][j]
    print("the maximum in line",i+1,"is :",max)
    print("the minimum in line",i+1,"is :",min)