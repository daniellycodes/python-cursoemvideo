distancia = float(input('Digite a distância em Km: '))
if distancia <= 200:
    preco = 0.50 * distancia
    print('Sua passagem custa R${:.2f}'.format(preco))
else:
    preco = 0.45 * distancia
    print('Sua passagem custa R${:.2f}'.format(preco))
