kaart = (
        (0,0,0,0,0,0,0,0,0,0,0,0),
        (0,1,1,1,1,1,1,1,1,1,1,0),
        (0,1,1,1,1,1,1,1,1,1,1,0),
        (0,1,1,1,1,1,1,1,1,1,1,0),
        (0,1,1,1,1,1,1,1,1,1,1,0),
        (0,1,1,1,1,1,1,1,1,1,1,0),
        (0,1,1,1,1,1,1,1,1,1,1,0),
        (0,1,1,1,1,1,1,1,1,1,1,0),
        (0,1,1,1,1,1,1,1,1,1,1,0),
        (0,1,1,1,1,1,1,1,1,1,1,0),
        (0,1,1,1,1,1,1,1,1,1,1,0),
        (0,0,0,0,0,0,0,0,0,0,0,0)
        )

plokk = ((1,1),(1,1)) #0 alati vasakul üleval, 1 paremal all
teada = {0:plokk}
edasi = {plokk}
auk = (10,10)
kaigunr = 0

#0 - up, 1 - down, 2 - left, 3 - right
def move(i, suund):
    iplokk = [[i[0][0],i[0][1]],[i[1][0],i[1][1]]]
    if iplokk[0] == iplokk[1]:
        if suund == "N":#match tuleb alles 3.10-s, mul ja mujal ka 3.9
            iplokk[0][1] -= 2
            iplokk[1][1] -= 1
        elif suund == "S":
            iplokk[0][1] += 1
            iplokk[1][1] += 2
        elif suund == "E":
            iplokk[0][0] += 1
            iplokk[1][0] += 2
        elif suund == "W":
            iplokk[0][0] -= 2
            iplokk[1][0] -= 1
    elif iplokk[0][0] != iplokk[1][0]: #orientation east-west
        if suund == "N":
            iplokk[0][1] -= 1
            iplokk[1][1] -= 1
        elif suund == "S":
            iplokk[0][1] += 1
            iplokk[1][1] += 1
        elif suund == "E":
            iplokk[0][0] += 2
            iplokk[1] = iplokk[0]
        elif suund == "W":
            iplokk[0][0] -= 1
            iplokk[1] = iplokk[0]
    else: #orientation north-south
        if suund == "N":
            iplokk[0][1] -= 2
            iplokk[1] = iplokk[0]
        elif suund == "S":
            iplokk[0][1] += 1
            iplokk[1] = iplokk[0]
        elif suund == "E":
            iplokk[0][0] += 1
            iplokk[1][0] += 1
        elif suund == "W":
            iplokk[0][0] -= 1
            iplokk[1][0] -= 1
    return tuple(iplokk)

#Dictionary positsioonidest ja ss käigud mis sellele eelnesid

# def nextMove(path,dir,blokk):
#
#     if blokk[1]=blokk[0]=auk:
#         return True, path
#     else:
#         return nextMove(path,"N",blokk)
#         return nextMove(path,"S",blokk)
#         return nextMove(path,"E",blokk)
#         return nextMove(path,"W",blokk)

while edasi:
    kaigunr += 1
    uued = []
    for uuritav in edasi:
        for kaik in ['N','S','E','W']:
            uus = move(uuritav, kaik)
            if uus[0] == auk and uus[1] == auk:
                win = 1 # kiire fix
                break # kiire fix
            print(uus[0][0])
            print(uus[0][1])
            print(uus[1][0])
            print(uus[1][1])
            print(type(uus))
            if kaart[uus[0][0]][uus[0][1]] == 1 and kaart[uus[1][0]][uus[1][1]] == 1 and uus not in teada.values():
                uued.append(uus)
                print(teada)
                print(uus)
                [k for k, v in teada.items() if v == uus][0] = uuritav
        if win == 1: break # kiire fix
    if win == 1: break # kiire fix
    edasi = set()

koht = [auk,auk]
while koht != plokk:
    print(koht)
    koht = teada[koht]
