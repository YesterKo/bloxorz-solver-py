b1 = [-1,-1]
b2 = [-1,-1]
fin = (-1,-1)
kaart = []
with open(input(),"r") as file:
    lines = file.readlines()
    for line in lines:
        rida = []
        for i in line:
            if i == "x":
                rida.append(1)
            elif i == "b":
                if b1[0] == -1:
                    b1 = [len(kaart),len(rida)]
                else:
                    b2 = [len(kaart),len(rida)]
                rida.append(1)
            elif i == "o":
                fin = (len(kaart),len(rida))
                rida.append(1)
            elif i == " ":
                rida.append(0)
        if len(rida) != 0: kaart.append(tuple(rida))
print(tuple(kaart))
print("plokk = " + str([b1,b2]))
print("lopp = " + str(fin))
