valor = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05 , 0.01]

print('NOTAS:')
for n in notas:
    qtd = int(valor / n)
    print('{} nota(s) de R$ {:.2f}'.format(qtd, n))
    valor -=  qtd*n
valor = valor*100
print('MOEDAS:')
for m in moedas:
    qtd2 = int(valor /(m*100) )
    print('{} moeda(s) de R$ {:.2f}'.format(qtd2, m))
    valor -= qtd2 * (m*100)
