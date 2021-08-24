import math
equa = (' ============================== EQUAÇÃO DO 2 GRAU ==============================')
cores = {'limpa':'\033[m',
    'amarelo':'\033[33m'}
print('{}{}{}'.format(cores['amarelo'], equa, cores['limpa']))

# OBS : O VALOR DE X É EQUIVALENTE A 1
# EXEMPLO: x² - 5x + 6 = 0 (1² - 5x + 6 = 0) = A B C #
t1 = 2
t2 = 1
a = int(input('Digite o número equivalente ao "A" : '))
b = int(input('Digite o número equivalente ao "B" : ' ))
c = int(input('Digite o número equivalente ao "C" : '))

# --------------------- FÓRMULA EQUAÇÃO DO SEGUNDO GRAU ------------------- #
# delta: b² - 4 * a * c
four_d_formula = -4
soma1 = b ** 2
soma2 = four_d_formula * (a) * (c)
soma3 = soma1 + soma2
soma4 = math.sqrt(soma3)
#print('{}'.format(soma4))


# --------------------- FÓRMULA DE BHÁSKARA ---------------------- #
# Considere raíz quadrada: →
# Considere delta: ▲
# -b ± →▲/2 * a
pontoevirgula = ';'
soma5 =  - b + soma4
soma6 = soma5/ 2
soma7 =  - b - soma4
soma8 = soma7/ 2
print('O valor de sua equação do segundo grau será de {:.0f}{}{:.0f}'.format(soma8,pontoevirgula,soma6))
