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
teada = {plokk:0}
edasi = {plokk}
auk = [10,10]
kaigunr = 0


while edasi:
    kaigunr += 1
    uued = []
    for uuritav in edasi:
        for kaik in ['N','S','E','W']:
            uus = move(uuritav, kaik)
            if 

#0 - up, 1 - down, 2 - left, 3 - right
def move(iplokk, suund):
    if iplokk[0] == iplokk[1]:
        if suund == "N":#match tuleb alles 3.10-s, mul ja mujal ka 3.9
            iplokk[0][1] -= 2
            iplokk[1][1] -= 1
        elif if suund == "S":
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
        elif if suund == "S":
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
        elif if suund == "S":
            iplokk[0][1] += 1
            iplokk[1] = iplokk[0]
        elif suund == "E":
            iplokk[0][0] += 1
            iplokk[1][0] += 1
        elif suund == "W":
            iplokk[0][0] -= 1
            iplokk[1][0] -= 1
    if kaart[iplokk[0][0]] == 0 or kaart[iplokk[1][0]] == 0 or kaart[iplokk[0][1]] == 0 or kaart[iplokk[1][1]] == 0:
        return [[-1,-1],[-1,-1]]#dead
    return iplokk

#Dictionary positsioonidest ja ss käigud mis sellele eelnesid

def nextMove(path,dir,blokk):

    if blokk[1]=blokk[0]=auk:
        return True, path
    else:
        return nextMove(path,"N",blokk)
        return nextMove(path,"S",blokk)
        return nextMove(path,"E",blokk)
        return nextMove(path,"W",blokk)
