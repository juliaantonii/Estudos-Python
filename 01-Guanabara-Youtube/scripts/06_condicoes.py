# -------------------------------------------------------
# AULA 06 - CONDIÇÕES
# -------------------------------------------------------

# -------------------------------------------------------
# EXEMPLO: Média de notas
# -------------------------------------------------------
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2
print('Sua média foi {:.1f}.'.format(media))

if media >= 6:
    print('Aprovado! :D')
else:
    print('Reprovado! ;-;')

print('------FIM------')

# Operadores de comparação: ==, !=, >, >=, <, <=
# Operadores lógicos: and, or, not

# Boas práticas:
#   - Use max() e min() para simplificar comparações.
#   - Para ano bissexto, use or e and combinados para reduzir if aninhados.
#   - Evite if muito aninhado, tente simplificar com operadores lógicos ou funções como max().

# -------------------------------------------------------
# DESAFIO 01
# -------------------------------------------------------
# Escreva um programa que faça o computador "pensar" em um número
# inteiro entre 0 e 5. Peça para o usuário tentar descobrir qual foi 
# o número escolhido pelo computador. O programa deverá escrever na 
# tela se o usuário venceu ou perdeu.

from random import randint

num_comp = randint(0, 5)  # Computador "pensa" em um número
num_user = int(input('Tente adivinhar o número que o computador pensou (0 a 5): '))

if num_user == num_comp:
    print('Parabéns! Você acertou! :D')
else:
    print('Você errou! O número era {}'.format(num_comp))
print('Tente outra vez!')

# -------------------------------------------------------
# DESAFIO 02
# -------------------------------------------------------
# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 
# 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai 
# custar R$7,00 por cada Km acima do limite.

velocidade = float(input('\nInforme a velocidade do carro (Km/h): '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Você foi multado! Valor da multa: R${:.2f}'.format(multa))
else:
    print('Velocidade segura. Bom passeio!')

# -------------------------------------------------------
# DESAFIO 03
# -------------------------------------------------------
# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input('\nDigite um número: '))

if num % 2 == 0:
    print('Número PAR')
else:
    print('Número ÍMPAR')

# -------------------------------------------------------
# DESAFIO 04
# -------------------------------------------------------
# Desenvolva um programa que pergunte a distância de uma viagem
# em Km. # Calcule o preço da passagem, cobrando R$0,50 por Km para
# viagens de até 200Km # e R$0,45 para viagens mais longas.

dist = float(input('\nDistância da viagem em Km: '))

if dist <= 200:
    preco = dist * 0.50
else:
    preco = dist * 0.45

print('Preço da passagem: R${:.2f}'.format(preco))

# -------------------------------------------------------
# DESAFIO 05
# -------------------------------------------------------
# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

ano = int(input('\nDigite um ano (ou 0 para ano atual): '))

# Condição simplificada para ano bissexto
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('O ano {} é BISSEXTO!'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO!'.format(ano))

# -------------------------------------------------------
# DESAFIO 06
# -------------------------------------------------------
# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num1 = int(input('\nDigite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

# Maior número
maior = max(num1, num2, num3)
# Menor número
menor = min(num1, num2, num3)

print('O maior número é {}'.format(maior))
print('O menor número é {}'.format(menor))

# -------------------------------------------------------
# DESAFIO 07
# -------------------------------------------------------
# Escreva um programa que pergunte o salário de um funcionário e calcule o 
# valor do seu aumento. Para salários superiores a R$1250,00, calcule um 
# aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('\nDigite o salário do funcionário: R$'))

if salario > 1250:
    novo_salario = salario * 1.10  # aumento de 10%
else:
    novo_salario = salario * 1.15  # aumento de 15%

print('Salário atualizado: R${:.2f}'.format(novo_salario))

# -------------------------------------------------------
# DESAFIO 08
# -------------------------------------------------------
# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário 
# se elas podem ou não formar um triângulo.

r1 = float(input('\nComprimento da primeira reta: '))
r2 = float(input('Comprimento da segunda reta: '))
r3 = float(input('Comprimento da terceira reta: '))

# Regra do triângulo: soma de dois lados > terceiro lado
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas PODEM formar um triângulo!')
else:
    print('As retas NÃO podem formar um triângulo!')

# -------------------------------------------------------
# DESAFIO 09
# -------------------------------------------------------
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos 
# ele vai pagar.
#
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário 
# ou então o empréstimo será negado.

emprestimo = float(input('Digite o valor da casa: '))
salario = float(input('Agora informe o valor do salário: '))
anos = int(input('Gostaria de pagar em quantos anos? '))

print('- - '*15)

parcelas = emprestimo / (anos * 12)
print('Pagando durante {} anos, suas parcelas serão de R${:.2f}.'.format(anos, parcelas))

if parcelas > salario * 0.3:
    print('Infelizmente, seu empréstimo foi negado!')
else:
    print('Parabéns! Empréstimo aprovado!')

# -------------------------------------------------------
# DESAFIO 10
# -------------------------------------------------------
# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher 
# qual será a base de conversão.
#
#   - 1 para BINÁRIO
#   - 2 para OCTAL
#   - 3 para HEXADECIMAL

num = int(input('Digite um numero qualquer: '))
base = int(input('Qual a base para conversão? '))

if base == 1:
    print('Vamos converter para BINÁRIO!')
    print('O decimal {} em BINÁRIO é: {}'.format(num, bin(num)))
elif base == 2:
    print('Vamos converter para OCTAL!')
    print('O decimal {} em OCTAL é: {}'.format(num, oct(num)))
if base == 3:
    print('Vamos converter para HEXADECIMAL!')
    print('O decimal {} em HEXADECIMAL é: {}'.format(num, hex(num)))

# -------------------------------------------------------
# DESAFIO 11
# -------------------------------------------------------
# Escreva um programa que leia dois números inteiros e compare-os, mostrando
# na tela uma mensagem:
#
#   - O primeiro valor é maior
#   - O segundo valor é maior
#   - Não existe valor maior, os dois são iguais

num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))

if num1 > num2:
    print('O valor {} é maior.'.format(num1))
elif num2 > num1:
    print('O valor {} é maior.'.format(num2))
else:
    print('Ambos são iguais')

# -------------------------------------------------------
# DESAFIO 12
# -------------------------------------------------------
# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# 
#   - Se ele ainda vai alistar ao serviço militar.
#   - Se é a hora de se alistar.
#   - Se já passou do tempo de alistamento.
#
# Seu programa tambpem deverá mostrar o tempo que falta ou que passou do prazo.

ano = int(input('Digite o seu ano de nascimento: '))

idade = 2025 - ano

if idade < 18:
    print('Você ainda vai se alistar. Falta {} anos para se alistar.'.format(18 - idade))
elif idade == 18:
    print('Você esta na idade certa para se alistar.')
else:
    print('Já passou do tempo de alistamento. Se passou {} anos do alistamento.'.format(idade - 18))

# -------------------------------------------------------
# DESAFIO 13
# -------------------------------------------------------
# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem 
# no final, de acordo com a média atingida:
#
#   - Média abaixo de 5.0: REPROVADO
#   - Média entre 5.0 e 6.9: RECUPERAÇÃO
#   - Média 7.0 ou superior: APROVADO

nota1 = float(input('Digite o valor da primeira nota: '))
nota2 = float(input('Digite o valor da segunda nota: '))

media = (nota1 + nota2)/2

if media < 5:
    print('REPROVADO!')
elif media >= 5 and media < 6.9:
    print('RECUPERAÇÃO!')
else:
    print('APROVADO!')

# -------------------------------------------------------
# DESAFIO 14
# -------------------------------------------------------
# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atléta
# e mostre sua categoria, de acordo com a idade:
#
#   - Até 9 anos: MIRIM
#   - Até 14 anos: INFANTIL
#   - Até 19 anos: JUNIOR
#   - Até 20 anos: SENIOR
#   - Acima: MASTER

ano = int(input('Digite seu ano de nascimento: '))

idade = 2025 - ano

if idade <= 9:
    print('MIRIM')
elif idade > 9 and idade <= 14:
    print('INFANTIL')
elif idade > 14 and idade <= 19:
    print('JUNIOR')
elif idade > 19 and idade <= 20:
    print('SENIOR')
else:
    print('MASTER')

# -------------------------------------------------------
# DESAFIO 15
# -------------------------------------------------------
# Refaça o DESAFIO 08 dos triângulos, acrescentando o recurso de mostrar que tipo
# de triângulo será formado:
#
#   - Equilátero: todos os lados iguais
#   - Isósceles: dois lados iguais
#   - Escaleno: todos os lados diferentes

r1 = float(input('\nComprimento da primeira reta: '))
r2 = float(input('Comprimento da segunda reta: '))
r3 = float(input('Comprimento da terceira reta: '))

# Regra do triângulo: soma de dois lados > terceiro lado
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas PODEM formar um triângulo!')
    if ( r1 == r2 == r3 ):
        print('Equilátero.')
    elif ( r1 != r2 != r3 != r1 ):
        print('Escaleno.')
    else:
        print('Isósceles.')
else:
    print('As retas NÃO podem formar um triângulo!')

# -------------------------------------------------------
# DESAFIO 16
# -------------------------------------------------------
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status
# de acordo com a tabela abaixo:
#
#   - Abaixo de 18.5: Abaixo do Peso
#   - Entre 18.5 e 25: Peso ideal
#   - 25 até 30: Sobrepeso
#   - 30 até 40: Obesidade
#   - Acima de 40: Obesidade mórbida

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura (em m): '))

imc = peso/(altura * altura)

print('Seu IMC é de {:.2f}'.format(imc))

if imc < 18.5:
    print('Abaixo do peso.')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal.')
elif imc >= 25 and imc < 30:
    print('Sobrepeso.')
elif imc >= 30 and imc < 40:
    print('Obesidade.')
elif imc >= 40:
    print('Obesidade mórbida.')

# -------------------------------------------------------
# DESAFIO 17
# -------------------------------------------------------
# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço 
# normal e condição de pagamento:
#
#   - À vista dinheiro/cheque: 10% de desconto
#   - À vista no cartão: 5% de desconto
#   - Em até 2x no cartão: preço normal
#   - 3x ou mais no cartão: 20% de juros

preco = float(input('Digite o valor do produto: '))
pagamento = int(input('Digite a forma de pagamento: \n'
'\n'
'1 - À vista no dinheiro \n'
'2 - À vista no cartão \n'
'3 - 2x no cartão \n'
'4 - 3x no cartão ou mais \n'
'\n'))

if pagamento == 1:
    print('O valor do produto será R${}.'.format(preco * 0.9))
elif pagamento == 2:
    print('O valor do produto será R${}.'.format(preco * 0.95))
elif pagamento == 3:
    print('O valor do produto será R${}.'.format(preco))
elif pagamento == 4:
    print('O valor do produto será R${}.'.format(preco * 1.2))

# -------------------------------------------------------
# DESAFIO 18
# -------------------------------------------------------
# Crie um programa que faça o computador jogar Jokenpô (Pedra | Papel | Tesoura) com você

from random import randint

print('Vamos jogar JOKENPÔ!')
print('Já escolhi minha mão, escolha a sua: \n'
'1 - Pedra \n'
'2 - Papel \n'
'3 - Tesoura \n'
'\n')

mao_user = int(input('Sua mão será: '))
mao_comp = randint(1,3)
print('Minha mão é {}!'.format(mao_comp))

if ((mao_user == 1) and (mao_comp == 3)) or ((mao_user == 2) and (mao_comp == 1)) or ((mao_user == 3) and (mao_comp == 2)):
    print('Você venceu! Parabêns!')
elif ((mao_user == 3) and (mao_comp == 1)) or ((mao_user == 1) and (mao_comp == 2)) or ((mao_user == 2) and (mao_comp == 3)):
    print('Você perdeu! Sinto muito!')
elif mao_user == mao_comp:
    print('Empaaate!')