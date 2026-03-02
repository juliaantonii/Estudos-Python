# -------------------------------------------------------
# AULA 03 - OPERADORES ARITMÉTICOS E PRECEDÊNCIA
# -------------------------------------------------------

# -------------------------------------------------------
# OPERADORES ARITMÉTICOS
# -------------------------------------------------------
# Python usa símbolos simples para representar operações matemáticas:
# +  → adição
# -  → subtração
# *  → multiplicação
# /  → divisão (resultado float)
# // → divisão inteira (descarta as casas decimais)
# ** → exponenciação (potência)
# %  → resto da divisão (módulo)

# Exemplos de cada um:

adicao = 5 + 3
print('Adição: ', adicao)

subtracao = 8 - 4
print('Subtração: ', subtracao)

multiplicacao = 2 * 6
print('Multiplicação: ', multiplicacao)

divisao = 5 / 2
print('Divisão: ', divisao)

divisao_inteira = 10 // 3
print('Divisão Inteira: ', divisao_inteira)

exponenciacao = 2 ** 3
print('Exponenciação: ', exponenciacao)

resto_divisao = 10 % 3
print('Resto da Divisão: ', resto_divisao)

# -------------------------------------------------------
# PRECEDÊNCIA DE OPERADORES
# -------------------------------------------------------
# Assim como na matemática, algumas operações têm prioridade.
# Ordem de execução:
# 1. Parênteses ()
# 2. Exponenciação (**)
# 3. Multiplicação (*), Divisão (/), Divisão Inteira (//), Resto (%)
# 4. Adição (+), Subtração (-)

# Exemplo:
#  resultado = 2 + 3 * 4 ** 2  → resultado será 50 (não 80!)
#  Porque: 4 ** 2 = 16 → 3 * 16 = 48 → 2 + 48 = 50

# -------------------------------------------------------
# DESAFIO 01
# -------------------------------------------------------
# Faça um programa que leia um número inteiro e mostre
# na tela o seu sucessor e o seu antecessor.

n1 = int(input('\nDigite um número inteiro: '))

antecessor = n1 - 1
sucessor = n1 + 1

print('O antecessor de {} é {}.'.format(n1, antecessor))
print('O sucessor de {} é {}.'.format(n1, sucessor))

# -------------------------------------------------------
# DESAFIO 02
# -------------------------------------------------------
# Crie um algoritmo que leia um número e mostre
# o seu dobro, triplo e raiz quadrada.

n1 = int(input('\nDigite um número: '))

dobro = n1 * 2
triplo = n1 * 3
raiz_quadrada = n1 ** 0.5  # Elevação à potência de 0.5 é o mesmo que raiz quadrada

print('O dobro de {} é {}.'.format(n1, dobro))
print('O triplo de {} é {}.'.format(n1, triplo))
print('A raiz quadrada de {} é {:.2f}'.format(n1, raiz_quadrada))

# -------------------------------------------------------
# DESAFIO 03
# -------------------------------------------------------
# Desenvolva um programa que leia as duas notas de um aluno,
# calcule e mostre a sua média.

n1 = float(input('\nDigite a nota 1: '))
n2 = float(input('Digite a nota 2: '))

media = (n1 + n2) / 2

print('A média das notas {:.1f} e {:.1f} é {:.2f}'.format(n1, n2, media))

# -------------------------------------------------------
# DESAFIO 04
# -------------------------------------------------------
# Escreva um programa que leia um valor em metros
# e o exiba convertido em centímetros e milímetros.

m = float(input('\nDigite o valor em metros: '))

c = m * 100   # 1 metro = 100 centímetros
mm = m * 1000 # 1 metro = 1000 milímetros

print('A medida de {}m equivale a {}cm e {}mm.'.format(m, c, mm))

# -------------------------------------------------------
# DESAFIO 05
# -------------------------------------------------------
# Faça um programa que leia um número inteiro e mostre
# na tela a sua tabuada (de 1 a 10).

n = int(input('\nDigite um número para ver sua tabuada: '))

print('-' * 12)
print('{} x {:2} = {}'.format(n, 1, n * 1))
print('{} x {:2} = {}'.format(n, 2, n * 2))
print('{} x {:2} = {}'.format(n, 3, n * 3))
print('{} x {:2} = {}'.format(n, 4, n * 4))
print('{} x {:2} = {}'.format(n, 5, n * 5))
print('{} x {:2} = {}'.format(n, 6, n * 6))
print('{} x {:2} = {}'.format(n, 7, n * 7))
print('{} x {:2} = {}'.format(n, 8, n * 8))
print('{} x {:2} = {}'.format(n, 9, n * 9))
print('{} x {:2} = {}'.format(n, 10, n * 10))
print('-' * 12)

# Dica extra: poderíamos usar um loop for, o que deixaria o código mais simples:
# for i in range(1, 11):
#     print(f"{n} x {i:2} = {n*i}")

# -------------------------------------------------------
# DESAFIO 06
# -------------------------------------------------------
# Crie um programa que leia quanto dinheiro uma pessoa tem
# e mostre quantos dólares ela pode comprar.
# Considere: US$1,00 = R$3,27

r = float(input('\nQual o valor em reais? R$'))

dolar = 3.27
conversao = r / dolar

print('Com R${:.2f} é possível comprar US${:.2f}'.format(r, conversao))

# -------------------------------------------------------
# DESAFIO 07
# -------------------------------------------------------
# Faça um programa que leia a largura e a altura de uma parede,
# calcule a sua área e a quantidade de tinta necessária para pintá-la.
# Considere: 1 litro de tinta cobre 2m².

l = float(input('\nQual a largura da parede (m)? '))
h = float(input('Qual a altura da parede (m)? '))

area = l * h
tinta = area / 2

print('A área total da parede é de {:.2f}m².'.format(area))
print('Será necessário {:.2f} litros de tinta para pintá-la.'.format(tinta))

# -------------------------------------------------------
# DESAFIO 08
# -------------------------------------------------------
# Faça um algoritmo que leia o preço de um produto
# e mostre seu novo preço com 5% de desconto.

v = float(input('\nQual o valor do produto? R$'))

novo_valor = v - (v * 0.05)

print('O novo valor com 5% de desconto é R${:.2f}'.format(novo_valor))

# -------------------------------------------------------
# DESAFIO 09
# -------------------------------------------------------
# Faça um programa que leia o salário de um funcionário
# e mostre o seu novo salário com 15% de aumento.

salario = float(input('\nQual o valor do salário atual? R$'))

novo_salario = salario + (salario * 0.15)

print('O novo salário com aumento de 15% será R${:.2f}'.format(novo_salario))