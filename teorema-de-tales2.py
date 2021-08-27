print(" -=-=-=-=-=--=-=-=-=-=-=-=-=- TEOREMA DE TALES -=-=-=-=-=--=-=-=-=-=-=-=-=- ")

print("""
      Esse é um programa para calcular o Teorema de Tales!\n Para calcular,
      preciso que você me passe algumas informações para eu poder te entregar o resultado.\n
      Para isso você deve me dizer onde se encontra o valor x, em "A", "B","C" ou "D"\n
       Por exemplo:\n
   18  / \ 3 
      /   \ 
 x   /     \ 32
  
  O valor x se encontra no índice "C"!\n
  Agora sabendo disso, vamos para oque interessa!""")

posicao = str(input("Onde está o seu valor x? : "))
if posicao == "a":
    b = int(input('Digite o valor de B: '))
    c = int(input('Digite o valor de C: '))
    d = int(input('Digite o valor de D: '))
    soma1 = b*c
    soma2 = soma1/d
    print(f'O resultado da sua expressão é:\n{soma2}')
if posicao == "b":
    a = int(input('Digite o valor de A: '))
    c = int(input('Digite o valor de C: '))
    d = int(input('Digite o valor de D: '))
    soma1 = a * d
    soma2 = soma1 / c
    print(f'O resultado da sua expressão é:\n{soma2}')
if posicao == "c":
    a = int(input('Digite o valor de A: '))
    b = int(input('Digite o valor de B: '))
    d = int(input('Digite o valor de D: '))
    soma1 = a * d / b
    print(f'O resultado da sua expressão é:\n{soma1}')
if posicao == "d":
    a = int(input('Digite o valor de A: '))
    b = int(input('Digite o valor de B: '))
    c = int(input('Digite o valor de C: '))
    soma1 = b * c
    soma2 = soma1 / a
    print(f'O resultado da sua expressão é:\n{soma2}')
