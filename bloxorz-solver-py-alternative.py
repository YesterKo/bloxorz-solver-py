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

plokk = [[1,1],[1,1]] #0 alati vasakul üleval, 1 paremal all
auk = [10,10]

#0 - up, 1 - down, 2 - left, 3 - right
def move(iplokk, suund):
    if iplokk[0] == iplokk[1]:
        print("võrdne",iplokk)
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
        print("EW",iplokk)
        if suund == "N":
            iplokk[0][1] -= 1
            iplokk[1][1] -= 1
        elif suund == "S":2
            iplokk[0][1] += 1
            iplokk[1][1] += 1
        elif suund == "E":
            iplokk[0][0] += 2
            iplokk[1] = iplokk[0]
        elif suund == "W":
            iplokk[0][0] -= 1
            iplokk[1] = iplokk[0]
    else: #orientation north-south
        print("NS",iplokk)
        if suund == "N":
            iplokk[0][1] -= 2
            iplokk[1] = iplokk[0]
        elif suund == "S":
            iplokk[0][1] += 2
            iplokk[1] = iplokk[0]
        elif suund == "E":
            iplokk[0][0] += 1
            iplokk[1][0] += 1
        elif suund == "W":
            iplokk[0][0] -= 1
            iplokk[1][0] -= 1
    #eraldi statement et erroreid neks
    print(iplokk,suund)
    if kaart[iplokk[0][1]][iplokk[0][0]] == 0:
        return [[-1,-1],[-1,-1]]#dead
    if kaart[iplokk[1][1]][iplokk[1][0]] == 0:
        return [[-1,-1],[-1,-1]]#dead
    #if kaart[iplokk[0][1]] == 0:
    #    return [[-1,-1],[-1,-1]]#dead
    #if kaart[iplokk[1][1]] == 0:
    #    return [[-1,-1],[-1,-1]]#dead
    return iplokk

#Dictionary positsioonidest ja ss käigud mis sellele eelnesid

def nextMove(path,dir,blokk):
    a = move(blokk,dir)
    if a[0][0] == -1:
        print("Staamal")
        return False, path
    if blokk[1]==blokk[0]==auk:
        print("Seal")
        return True, path+dir
    else:
        print("Siin")
        N = nextMove(path+dir,"N",blokk)
        S = nextMove(path+dir,"S",blokk)
        E = nextMove(path+dir,"E",blokk)
        W = nextMove(path+dir,"W",blokk)
        if N[0]:
            return N[1]
        if S[0]:
            return S[1]
        if E[0]:
            return E[1]
        if W[0]:
            return W[1]

print(nextMove("","",plokk))
