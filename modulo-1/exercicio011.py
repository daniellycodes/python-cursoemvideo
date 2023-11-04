largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
print('Sua parede tem a dimessão de {:.2f}mx{:.2f}m e tem área de {:.2f}m2'.format(largura, altura, area))
tinta = area / 2
print('Para pintar a parede, você precisará de {:.2f}l de tinta'.format(tinta))
