preco = float(input('Digite o preço do produto: '))
desconto = preco * 0.05
novopreco = preco - desconto
print('O produto que custava R${:.1f}, na promoção de 5% custará R${:.1f}. Você poupou {:.1f}'.format(preco, novopreco, desconto))
