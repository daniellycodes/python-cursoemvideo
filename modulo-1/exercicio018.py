from math import radians, sin, cos, tan

angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo))
print('O ângulo de {} tem SENO de {}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O ângulo de {} tem COSSENO de {}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O ângulo de {} tem TANGENTE de {}'.format(angulo, tangente))
