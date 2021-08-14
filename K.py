a= int(input("vared kon adad ro"))
b= [["-" for i in range(a)] for j in range(a)]

for i in range(a):
    for j in range(i + 1):
        if j == 0 or j == i:
            b[i][j] = 1
        else:
            b[i][j] = int(paskal[i - 1][j - 1]) + int(b[i - 1][j])

for i in range(a):
    for j in range(a):
        if b[i][j] != "-":
            print(paskal[i][j], end=' ')
    print()
