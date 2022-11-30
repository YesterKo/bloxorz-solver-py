from copy import deepcopy
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
        elif suund == "S":
            iplokk[0][1] += 1
            iplokk[1][1] += 1
        elif suund == "E":
            iplokk[0][0] += 2
            iplokk[1] = deepcopy(iplokk[0])
        elif suund == "W":
            iplokk[0][0] -= 1
            iplokk[1] = deepcopy(iplokk[0])
    elif iplokk[0][1] != iplokk[1][1]: #orientation north-south
        print("NS",iplokk)
        if suund == "N":
            iplokk[0][1] -= 1
            iplokk[1] = deepcopy(iplokk[0])
        elif suund == "S":
            iplokk[0][1] += 2
            iplokk[1] = deepcopy(iplokk[0])
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

def writer(inputstring):
    with open("output.txt","a") as fail:
        fail.write(inputstring+"\n")

oldud = [[[1,1],[1,1]]]

found = []

suunad = "NSEW"
def nextMove(path,blokk):
    print()
    print(path,blokk)
    writer(str(path)+" "+str(blokk))
    liigud = [move(deepcopy(blokk),"N"),move(deepcopy(blokk),"S"),move(deepcopy(blokk),"E"),move(deepcopy(blokk),"W")]
    toimivad = []
    for i in liigud:
        if i[0][0] != -1 and i not in oldud:
            oldud.append(i)
            toimivad.append((i,suunad[liigud.index(i)]))
    print(toimivad," Need toimivad")
    for i in toimivad:
        nextMove(path+i[1],i[0])

    if blokk[0] == blokk[1] == auk:
        writer("We've done it")
        if len(found) == 0: found.append(path)
        elif len(found[0]) > path: found.append(path)

nextMove("",plokk)

print(found)
