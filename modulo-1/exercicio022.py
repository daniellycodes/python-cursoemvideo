nomecompleto = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nomecompleto.upper()))
print('Seu nome em minúsculas é {}'.format(nomecompleto.lower()))
print('Seu nome tem {} letras'.format(len(nomecompleto) - nomecompleto.count(' ')))

separa = nomecompleto.split()

print('Seu primeiro nome tem {} letras'.format(len(separa[0])))
