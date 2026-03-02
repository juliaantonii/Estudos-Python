# -------------------------------------------------------
# AULA 09 - LISTAS
# -------------------------------------------------------

# Uma LISTA é uma estrutura de dados (coleção) em Python que pode armazenar vários valores em uma única variável.
# Diferente das tuplas, as listas são MUTÁVEIS.
# Isso significa que podemos alterar, adicionar ou remover elementos a qualquer momento.

# Usamos colchetes [] para declarar uma lista.

numeros = [10, 20, 30, 40, 50]

print("Lista original:", numeros)

# -------------------------------------------------------
# ALTERANDO ELEMENTOS DE UMA LISTA
# -------------------------------------------------------

# Como as listas são mutáveis, podemos modificar seus valores diretamente:
numeros[0] = 99
print("Após alterar o primeiro elemento:", numeros)

# Também podemos adicionar e remover elementos:
numeros.append(60)      # adiciona um elemento no final
numeros.insert(2, 25)   # insere um elemento na posição 2
numeros.remove(40)      # remove o valor 40
numeros.pop(3)          # remove o valor de acordo com o indice 3
print("Após adicionar e remover elementos:", numeros)

# Podemos utilizar a função list() para criar uma nova lista a partir de valores existentes

valores = list(range(4, 11)) # criará: valores = [4,5,6,7,8,9,10]

# Para ordenar listas, devemos usar SORT() e NÃO SORTED(). Para fazer o inverso de SORT() podemos incluir
# o parametro REVERSE=True

valores.sort(reverse=True) # valores = [10,9,8,7,6,5,4]

# b = a != b = a[:]

# -------------------------------------------------------
# DESAFIO 01
# -------------------------------------------------------
# Faça um programa que leia 5 valores numéricos e guarde os em uma lista.
# No final, mostre qual foi o MAIOR e o MENOR valor digitado e as suas respectivas posições na lista.

valores = []

for i in range(0,5):
    valores.append(int(input('Digite um valor: ')))

maior = valores[0]
menor = valores[0]

for i in range(0,5):
    if valores[i] >= maior:
        maior = valores[i]
    if valores[i] <= menor:
        menor = valores[i]

print(f'A lista de valores é: {valores}')
print(f'O maior valor é {maior} e o menor valor é {menor}')

# -------------------------------------------------------
# DESAFIO 02
# -------------------------------------------------------
# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados,
# em ordem crescente.

lista = []

for i in range(0,5):
    lista.append(int(input('Digite um valor: ')))
    if lista[-1] in lista[0:-1]:
        print(f'O valor {lista[-1]} já existe!')
        lista.pop()

lista.sort()

print(f'A lista é composta por: {lista}')

# -------------------------------------------------------
# DESAFIO 03
# -------------------------------------------------------
# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.

lista = []

for i in range(0,5):
    lista.append(int(input('Digite um valor: ')))
    for i in range(0, len(lista) - 1):
        if lista[-1] < lista[i]:
            lista.insert(i - 1, lista[-1])
            lista.pop()

print(lista)

# -------------------------------------------------------
# DESAFIO 04
# -------------------------------------------------------
# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
#   A) Quantos números foram digitados.
#   B) A lista de valores ordenada de forma decrescente.
#   C) Se o valor 5 foi digitado e está ou não na lista.

valores = []
loop = 1
num = 1
existe = 0

valores.append(int(input('Digite um valor: ')))

while loop != 0:
    resp = input('Gostaria de inserir outro valor? [Y/N]')
    if resp == 'Y':
        valores.append(int(input('Digite um valor: ')))
        num = num + 1
    elif resp == 'N':
        print('Obrigada!')
        loop = 0
    else:
        print('Resposta inválida!')
        loop = 0

print(f'Foram digitados {num} valores')
valores.sort(reverse=True)
print(f'A lista em forma decrescente é: {valores}')

for i in range(0, len(valores)):
    if i == 5:
        existe = existe + 1

if existe > 0:
    print(f'O valor 5 existe na lista de valores, ele apareceu {existe} vezes.')
else:
    print('O valor 5 não existe na lista de valores.')

# -------------------------------------------------------
# DESAFIO 05
# -------------------------------------------------------
# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares
# digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

valores = []
pares = []
impares = []
loop = 1

valores.append(int(input('Digite um valor: ')))

while loop != 0:
    resp = input('Gostaria de inserir outro valor? [Y/N]').strip().upper()
    if resp == 'Y':
        valores.append(int(input('Digite outro valor: ')))
    elif resp == 'N':
        print('Obrigada! Lista fechada!')
        loop = 0
    else:
        print('Resposta inválida!')
        loop = 0

for v in valores:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

valores.sort()
print(f'A lista é formada pelos valores: {valores}')
print(f'Os valores pares são: {pares}')
print(f'Os valores impares são: {impares}')

# -------------------------------------------------------
# DESAFIO 06
# -------------------------------------------------------
# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados
# na ordem correta.

expr = str(input('Digite a expressão: '))
pilha = []

for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida.')
else:
    print('Sua expressão esta errada.')

# Ainda dentro do conteúdo de listas, também encontramos as listas compostas, isto é, listas dentro
# de listas. Podendo ser representado da seguinte forma:

pessoas = [['Pedro',25],['Maria',19],['João',32]]

# Para consultar seus dados, usamos dois indices, como:

print(pessoas[0][0]) # saida: Pedro
print(pessoas[1][1]) # saida: 19
print(pessoas[2][0]) # saida: João
print(pessoas[1])    # saida: ['Maria',19]

# -------------------------------------------------------
# DESAFIO 07
# -------------------------------------------------------
# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
# No final, mostre:
#   A) Quantas pessoas foram cadastradas.
#   B) Uma listagem com as pessoas mais pesadas.
#   C) Uma listagem com as pessoas mais leves.

galera = []
loop = 1
pessoa = []

pessoa.append(input('Digite um nome: '))
pessoa.append(int(input('Seu respectivo peso: ')))
galera.append(pessoa[:])

while loop != 0:
    resp = input('Gostaria de inserir outro valor? [Y/N]').strip().upper()
    if resp == 'Y':
        pessoa = []
        pessoa.append(input('Digite um nome: '))
        pessoa.append(int(input('Seu respectivo peso: ')))
        galera.append(pessoa[:])
    elif resp == 'N':
        print('Obrigada! Lista fechada!')
        loop = 0
    else:
        print('Resposta inválida!')
        loop = 0

maior = menor = galera[0][1]
pesado = []
leve = []

for i in range(0,len(galera)):
    if galera[i][1] >= maior:
        maior = galera[i][1]
    elif galera[i][1] < menor:
        menor = galera[i][1]

for j in range(0, len(galera)):
    if galera[j][1] == maior:
        pesado.append(galera[j][0])
    elif galera[j][1] == menor:
        leve.append(galera[j][0])

print(f'Foram cadastradas {len(galera)} pessoas')
print(f'O maior peso foi {maior} do/da {pesado} ')
print(f'O menor peso foi {menor} do/da {leve}')

# -------------------------------------------------------
# DESAFIO 08
# -------------------------------------------------------
# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista
# única que mantenha separados os valores PARES e IMPARES. No final, mostre os valores pares e ímpares
# em ordem crescente.

numeros = []
pares = []
impares = []

for i in range(0,7):
    numeros.append(int(input('Digite um valor: ')))
    if numeros[i] % 2 == 0:
        pares.append(numeros[i])
    else:
        impares.append(numeros[i])

print(f'A lista de valores pares é: {pares}')
print(f'A lista de valores impares é: {impares}')

# -------------------------------------------------------
# DESAFIO 09
# -------------------------------------------------------
# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input(f'Digite um valor para [{i}, {j}]: ')))
    matriz.append(linha[:])

print('\nMatriz digitada:')
print('-'*23)
for i in range(3):
    for j in range(3):
        print(f'| {matriz[i][j]:^5}', end='')
    print(' |')
print('-'*23)

# -------------------------------------------------------
# DESAFIO 10
# -------------------------------------------------------
# Aprimore o desafio anterior, mostrando no final:
#   A) A soma de todos os valores pares digitados.
#   B) A soma dos valores da terceira coluna.
#   C) O maior valor da segunda linha.

matriz = []
pares = []
soma = 0

for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input(f'Digite um valor para [{i}, {j}]: ')))
        if linha[j] % 2 == 0:
            pares.append(linha[j])
        if i == 2:
            soma = soma + linha[j]
        if i == 1:
            maior = max(linha)
            
    matriz.append(linha[:])

print('\nMatriz digitada:')
print('-'*23)
for i in range(3):
    for j in range(3):
        print(f'| {matriz[i][j]:^5}', end='')
    print(' |')
print('-'*23)

print(f'\nOs valores pares são: {pares}')

print(f'\nO maior valor da linha 2: {maior}')

# -------------------------------------------------------
# DESAFIO 11
# -------------------------------------------------------
# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar
# quantos jogos seráo gerados e vai sortear 6 números entre 1 e 60 para casa jogo, 
# cadastrando tudo em uma lista composta.

from random import randint
jogos = []
num = []

qtd = int(input('Quantos jogos serão criados? '))

for i in range(0,qtd):
    num = []
    for j in range(0,6):
        num.append(randint(1,61))
    jogos.append(num[:])

for k in range(0,len(jogos)):
    print(f'JOGO {k + 1}: {jogos[k]}')

# -------------------------------------------------------
# DESAFIO 12
# -------------------------------------------------------
# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar
# as notas de cada aluno individualmente.

turma = []
aluno = []

qtd = int(input('Quantos alunos tem na turma? '))

for i in range(0, qtd):
    aluno = []
    aluno.append(str(input('\nNome: ')).strip().upper())
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))
    turma.append(aluno[:])

print('\nAs médias dos alunos da turma são:')
print('-'*36)
for k in range(0, len(turma)):
    print(f'| Nome: {turma[k][0]:<8} | ', end='')
    print(f'Média: {((turma[k][1] + turma[k][2])/2):>5.2f}pts |')
print('-'*36)

qa = str(input('\nGostaria de ver as notas de um aluno específico? [Y/N] ')).strip().upper()

existe = 0
if qa == 'Y':
    nome = str(input('Qual o nome do aluno? ')).strip().upper()
    print('\nForam encontrados estes dados:')
    print('-'*56)
    for m in range(0, len(turma)):
        if turma[m][0] == nome:
            print(f'| Nome: {turma[m][0]:<8} | ', end='')
            print(f'Nota 1: {turma[m][1]:>5.2f}pts | ', end='')
            print(f'Nota 2: {turma[m][2]:>5.2f}pts |')
else:
    print('Não existe esse aluno em nossa turma!')
print('-'*56)