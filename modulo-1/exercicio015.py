dias = int(input('Por quantos dias o carro foi alugado? '))
kmCorridos = float(input('Quantos km foram corridos? '))
preco = (60 * dias) + (0.15 * kmCorridos)
print('O total a pagar é de R${:.2f}'.format(preco))
