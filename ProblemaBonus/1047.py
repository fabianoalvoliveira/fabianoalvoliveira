a, b, c, d =map(int, input().split(" ")) 
hora = 0
minutos = 0
if a == c and b == d:
    hora = 24
elif a <= c:
    hora = c - a
    if b <= d:
        minutos = d - b
    else:
        if hora == 0:
            hora = 24
        hora = hora - 1
        minutos = d - b + 60
elif a > c :
    hora = c - a + 24
    if b <= d:
        minutos = d - b
    else:
        if hora == 0:
            hora = 24
        hora = hora - 1
        minutos = d - b + 60
print("O JOGO DUROU", hora, "HORA(S) E", minutos, "MINUTO(S)")
