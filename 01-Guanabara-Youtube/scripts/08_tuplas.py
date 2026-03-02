# -------------------------------------------------------
# AULA 08 - TUPLAS
# -------------------------------------------------------

# Uma tupla é uma estrutura de dados (coleção) em Python que pode armazenar vários valores em uma única variável.
# Ela é muito parecida com uma lista, porém possui uma característica fundamental:
# As tuplas são IMUTÁVEIS. Ou seja, depois de criadas, seus valores não podem ser alterados, adicionados ou removidos.

# Usamos parênteses () para declarar uma tupla.

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)
print(len(lanche)) # mostra o tamanho | quantidade de elementos da tupla

# Assim como nas listas e strings, podemos acessar os itens por seus índices (a contagem começa em 0).
print(lanche[0])  # Hambúrguer
print(lanche[2])  # Pizza
print(lanche[-1]) # Pudim (último elemento)

# Também é possível fazer "slices" (fatias), pegando apenas partes da tupla.
print(lanche[1:3])  # ('Suco', 'Pizza')
print(lanche[:2])   # ('Hambúrguer', 'Suco')
print(lanche[-2:])  # ('Pizza', 'Pudim')

# Para referenciar TUPLAS, sempre use colchetes ()
# Para referenciar LISTAS, sempre use colchetes []
# Para referenciar DICIONARIO, sempre use colchetes {}

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')

# Outra forma seria também:

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')

# SORTED() -> ORGANIZE | ORDENE
# Quando usamos sorted em uma tupla, ela não deixa de ser IMUTÁVEL, apenas cria uma nova lista
# e retorna os elementos em ordem

print(sorted(lanche))
print(lanche)

# Podemos usar de algumas funções para acessar as referências da tupla, como:

# COUNT() - Usada para contar o número de elementos sinalizados
# Supondo que há a tupla A = (1, 2, 3, 3, 4)
# Se usarmos print(a.count(3)), ele retornara 2, pois há dois 3 na tupla
# Caso usamos print(a.count(5)), retornara 0, pois não há 5

# INDEX() - Usada para retornar a posição do elemento mencionado
# Ainda supondo que ha a tupla A = (1, 2, 3, 3, 4)
# Se usarmos print(a.index(2)), ele retornara 1
# Caso o elemento mensionado seja repetido, o index retornará o primeiro elemento visualizado

# -------------------------------------------------------
# DESAFIO 01
# -------------------------------------------------------
# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, 
# de ZERO até VINTE.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

num = int(input('Digite um valor de 0 a 20: '))

tupla = (0, 'zero', 1, 'um', 2, 'dois', 3, 'três', 4, 'quatro', 5, 'cinco', 6, 'seis', 7, 'sete', 8, 'oito', 9, 'nove', 10, 'dez',  11, 'onze', 12, 'doze', 13, 'treze', 14, 'quatorze', 15, 'quinze', 16, 'dezesseis', 17, 'dezesete', 18, 'dezoito', 19, 'dezenove', 20, 'vinte')

print(f'O valor escolhido foi: {tupla[tupla.index(num) + 1]}')

# -------------------------------------------------------
# DESAFIO 02
# -------------------------------------------------------
# Crie uma tupla preenchida com os 10 primeiros colocados no Campeonato de Futebol, na ordem de colocação.
# Depois mostre:
#
#   A) Apenas os 5 primeiros colocados.
#   B) Os últimos 4 colocados da tabela.
#   C) Uma lista com os times em ordem alfabética.
#   D) Em que posição na tabela está o time D.

times = ('B', 'A', 'E', 'D', 'C', 'J', 'I', 'H', 'G', 'F')

print(f'Os primeiros 5 colocados são: {times[:5]}')
print(f'Os últimos 4 colocados são: {times[-4:]}')
print(f'Os times em ordem alfabetica são: {sorted(times)}')
print(f'O time D esta na posicao {times.index('D') + 1}º')

# -------------------------------------------------------
# DESAFIO 03
# -------------------------------------------------------
# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor
# que estão na tupla.

from random import randint 

n = (randint(1,5), randint(1,5), randint(1,5), randint(1,5), randint(1,5),)

print(f'Os valores sorteados foram: {n}')
print(f'O maior valor sorteado foi: {max(n)}')
print(f'O menor valor sorteado foi: {min(n)}')

# -------------------------------------------------------
# DESAFIO 04
# -------------------------------------------------------
# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
# No final, mostre:
#
#   A) Quantas vezes apareceu o valor 9.
#   B) Em que posição foi digitado o primeiro valor 3.
#   C) Quais foram os números pares.

print('Insira 4 valores: ')
num = (int(input()), int(input()), int(input()), int(input()))

print(f'Os valores escolhidos foram: {num}')
print(f'O valor 9 apareceu: {num.count(9)}')
print(f'O primeiro valor 3 apareceu na posição: {num.index(3)}')
print('Os números pares foram: ')

for i in num:
    if i % 2 == 0:
        print(i)

# -------------------------------------------------------
# DESAFIO 05
# -------------------------------------------------------
# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
# na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

prod = ('Pão', 12.99, 'Leite', 6.90, 'Café', 10.90, 'Queijo', 6.99, 'Mortadela', 7.90)

print('|','-'*45,'|')
print('|',' '*13, 'LISTA DE PRODUTOS', ' '*13, '|',)
print('|','-'*45,'|')

for i in range(0, len(prod), 2):
    print('|', f'{prod[i]:.<35}', f'R$ {prod[i+1]:>6.2f}', '|')
print('|','-'*45,'|')

# -------------------------------------------------------
# DESAFIO 06
# -------------------------------------------------------
# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso,
# você deve mostrar, para cada palavra, quais são as suas vogais.

cor = ('rosa','azul','verde','roxo','branco','preto')
vogais = ('a', 'e', 'i', 'o', 'u')

print(f'Sabemos que existem as vogais: {vogais}')

for palavra in cor:
    print(f'\nNa palavra {palavra.upper()} temos as vogais: ', end='')
    for letra in palavra:
        if letra in vogais:
            print(letra.upper(), end=' ')