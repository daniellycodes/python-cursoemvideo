salario = float(input('Digite o valor do seu salário: R$ '))
aumento = salario * 0.15
reajuste = salario + aumento
print('O funcionário que ganhava R${:.2f}, após o reajuste de 15%, passa a receber R${:.2f}'.format(salario, reajuste))
