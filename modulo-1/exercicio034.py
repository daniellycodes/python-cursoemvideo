salario = float(input('Digite seu salário: '))
if salario > 1250:
    salario = salario * 1.1
if salario <= 1250:
    salario = salario * 1.15
print('Seu salário, após o aumento, é R${:.2f}'.format(salario))
