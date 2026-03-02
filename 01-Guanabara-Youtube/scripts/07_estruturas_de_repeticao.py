# -------------------------------------------------------
# AULA 07 - ESTRUTURAS DE REPETIÇÃO
# -------------------------------------------------------

# As estruturas de repetição (também conhecidas como "loops") permitem executar um bloco de código
# várias vezes, de forma controlada.
# Em Python, temos principalmente dois tipos de laços:
#
#   ➜ for    -> percorre uma sequência (como listas, tuplas, strings, ranges, etc.)
#   ➜ while  -> repete enquanto uma condição for verdadeira

# -------------------------------------------------------
# O laço for é utilizado quando sabemos exatamente quantas vezes queremos repetir algo.
# Ele percorre uma sequência de valores (por exemplo, um range).

for i in range(1, 6):
    print(f'Contando... {i}')
print('Fim do laço for!')

# -------------------------------------------------------
# Personalizando o range()
# -------------------------------------------------------
# A função range() pode ter até três parâmetros:
# range(início, fim, passo)

# ➜ início → valor inicial (inclusivo)
# ➜ fim → valor final (exclusivo, ou seja, o loop para antes dele)
# ➜ passo → de quanto em quanto vai pular

# Exemplos:

# Contando de 0 a 10 (de 1 em 1)
for i in range(0, 11):
    print(i)

# Contando de 0 a 10, pulando de 2 em 2
for i in range(0, 11, 2):
    print(i)

# Contando de 10 até 0 (de trás pra frente)
for i in range(10, -1, -1):
    print(i)

# Exemplo simples de laço while:
# Enquanto a variável 'contador' for menor ou igual a 5, o código dentro do bloco será executado.

contador = 1
while contador <= 5:
    print(f'Contando... {contador}')
    contador += 1  # importante! sem isso, o loop seria infinito
print('Fim do laço while!')

# -------------------------------------------------------
# DESAFIO 01
# -------------------------------------------------------
# Faça um programa que mostre na tela uma contagem regressiva para
# o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de
# 1 segundo entre eles.

from emoji import emojize

for i in range(10,0,-1):
    print(i)
print(emojize('BOOM! :firecracker:'))

# -------------------------------------------------------
# DESAFIO 02
# -------------------------------------------------------
# Crie um programa que mostre na tela todos os números pares que estão
# no intervalo entre 1 e 50.

for i in range(1,51):
    if i % 2 == 0:
        print(i)

# -------------------------------------------------------
# DESAFIO 03
# -------------------------------------------------------
# Faça um programa que calcule a soma entre todos os número ímpares que são
# múltiplos de três e que se encontram no intervalo de 1 até 500

soma = 0
for i in range(1,501):
    if i % 2 != 0 and i % 3 == 0:
        soma = soma + i
print(soma)

# -------------------------------------------------------
# DESAFIO 04
# -------------------------------------------------------
# Refaça o DESAFIO 05 de OPERADORES ARITMÉTICOS, mostrando a tabuada de um número que o
# usuário escolher, só que agora utilizando um laço FOR.

num = int(input('Digite um valor: '))

for i in range(1, 11):
    print('{} x {:2} = {}'.format(num, i, num * i))

# -------------------------------------------------------
# DESAFIO 05
# -------------------------------------------------------
# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que
# forem pares. Se o valor digitado for impar, desconsidere-o.

soma = 0
for i in range(0,6):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        soma = soma + num
print('A soma dos valores pares é: {}'.format(soma))

# -------------------------------------------------------
# DESAFIO 06
# -------------------------------------------------------
# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10
# primeiros termos dessa progressão.

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão PA:'))
termo = primeirocont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')

# -------------------------------------------------------
# DESAFIO 07
# -------------------------------------------------------
# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um valor: '))

primo = 1
for i in range(1, num + 1):
    if i != num and i != 1:
        if num % i == 0:
            print('Não é primo! É divisível por {}'.format(i))
            primo = 0
if primo == 1:
    print('É primo! É divisível apenas por 1 e {}'.format(num))

# -------------------------------------------------------
# DESAFIO 08
# -------------------------------------------------------
# Crie um programa que leia uma frase qualquer e informe se ela é palíndromo, desconsiderando
# os espaços.
# Ex: Apos a sopa
#     O lobo ama bolo

# -------------------------------------------------------
# DESAFIO 09
# -------------------------------------------------------
# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas
# ainda não atingiram a maioridade e quantas já são maiores.
# Obs: Considere 21 anos como maioridade.

maior = 0
menor = 0
for i in range(0,7):
    idade = int(input('Digite sua idade: '))
    if idade >= 21:
        maior = maior + 1
    else:
        menor = menor + 1
print('Entre as 7 pessoas, {} são de maior e {} são de menor.'.format(maior, menor))

# -------------------------------------------------------
# DESAFIO 10
# -------------------------------------------------------
# Faça um programa que leia o peso de cinco pessoas. No final mostre qual foi o maior e o
# menor peso lidos.

for i in range(0,5):
    peso = float(input('Digite seu peso: '))
    if i == 0:
        maior = peso
        menor = peso
    else:
        if peso >= maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi {}Kg e o menor peso foi {}Kg'.format(maior, menor))

# -------------------------------------------------------
# DESAFIO 11
# -------------------------------------------------------
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
#   - A média de idade do grupo.
#   - Qual é o nome do homem mais velho.
#   - Quantas mulheres têm menos de 20 anos.

tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1    
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados')
print(f'E temos {totM20} mulheres com menos de 20 anos')