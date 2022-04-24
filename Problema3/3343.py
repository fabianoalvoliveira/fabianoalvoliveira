n,x= map(int,input().split(" "))
k = input()
P,M,G = map(int,input().split(" "))
titan = list(k)
muralha = []
posP = posM = posG = 0
muralha.append(x)

cont = 0
for  i in (range(n)):
    if titan[i] == 'P':
        muralha[posP] = muralha[posP] - P
        if posP + 1 > cont: 
            cont = posP + 1
            muralha.append(x)

    elif titan[i] == 'M':
        muralha[posM] = muralha[posM] - M
        if posM + 1 > cont: 
            cont = posM + 1
            muralha.append(x)
                
    elif titan[i] == 'G':
        muralha[posG] = muralha[posG] - G
        if posG + 1 > cont: 
            cont = posG + 1
            muralha.append(x)
    if(muralha[posG] < G): posG += 1
    while(muralha[posM] < M) :posM += 1
    while(muralha[posP] < P) : posP += 1
print(cont)
