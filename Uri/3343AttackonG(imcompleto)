import math
n,x = map(int,input().split(" "))
k = input()
P,M,G = map(int,input().split(" "))
titan = list(k)
muralha = []
posP = list(range(len(titan)))
posM = list(range(len(titan)))
posG = list(range(len(titan)))

for  i in range(n):
    muralha.append(x)
    if titan[i] == 'P': 
       titan[i] = P
    elif titan[i] == 'M':
       titan[i] = M
    if titan[i] == 'G':
        titan[i] = G

cont = 0
for  i in range(n):
    if titan[i] == P:
        muralha[posP[0]] = muralha[posP[0]] - titan[i]
        if posP[0] + 1 > cont: cont = posP[0] + 1

    elif titan[i] == M:
        muralha[posM[0]] = muralha[posM[0]] - titan[i]
        if posM[0] + 1 > cont: cont = posM[0] + 1
                
    elif titan[i] == G:
        muralha[posG[0]] = muralha[posG[0]] - titan[i]
        if posG[0] + 1 > cont: cont = posG[0] + 1
    if(muralha[posG[0]] < G): posG.pop(0)
    if(muralha[posM[0]] < M): posM.pop(0)
    if(muralha[posP[0]] < P): posP.pop(0)

print(cont)
