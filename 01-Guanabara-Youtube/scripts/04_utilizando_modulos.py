# -------------------------------------------------------
# AULA 04 - UTILIZANDO MÓDULOS EM PYTHON
# -------------------------------------------------------

# -------------------------------------------------------
# O QUE É UM MÓDULO?
# -------------------------------------------------------
# Um módulo é um arquivo Python (.py) que contém definições — funções,
# classes e variáveis — que podem ser reutilizadas em outros programas.

# Podemos realizar as importações de módulos utilizando a palavra-chave 'import' 
# seguida do nome do módulo. Ou, podemos importar partes específicas de um módulo 
# utilizando 'from' seguido do nome do módulo e 'import' seguido do nome da parte específica.

# Exemplo:
#   import bebida
#   -> importa tudo do módulo "bebida"
#
#   from bebida import refrigerante
#   -> importa apenas a função/classe/variável "refrigerante" do módulo
#
# Isso ajuda a **organizar o código** e **evitar repetições**.

# Uma das bibliotecas utilizadas em Python é a 'math', que fornace funções matemáticas.

# -------------------------------------------------------
# MÓDULO 'math' — FUNÇÕES MATEMÁTICAS
# -------------------------------------------------------
# O módulo math fornece várias funções matemáticas úteis:
#   ceil(x)   → arredonda para cima
#   floor(x)  → arredonda para baixo
#   trunc(x)  → remove a parte decimal (trunca)
#   pow(x, y) → potência (x elevado a y)
#   sqrt(x)   → raiz quadrada
#   factorial(x) → fatorial de um número

# Vamos praticar calculando a raiz quadrada arredondada pra cima de um número utilizando a biblioteca 'math':

import math

num = int(input('Digite um valor: '))
raiz = math.sqrt(num)

print('A raiz quadrada de {} é igual a {:.1f}'.format(num, math.floor(raiz)))

# Importando apenas funções específicas do módulo 'math'
# Isso torna o código mais limpo e evita usar "math." toda hora.

from math import sqrt, floor

num = int(input('\nDigite outro valor: '))
raiz = sqrt(num)

print('A raiz quadrada de {} é igual a {:.1f}'.format(num, floor(raiz)))

# -------------------------------------------------------
# MÓDULO 'random' — GERAÇÃO DE NÚMEROS ALEATÓRIOS
# -------------------------------------------------------
# O módulo random permite gerar números pseudoaleatórios.
# - random() → gera um número entre 0.0 e 1.0
# - randint(a, b) → gera um número inteiro entre 'a' e 'b'

import random

num1 = random.random()
num2 = random.randint(1, 10)

print('\nNúmero aleatório entre 0 e 1: {:.2f}'.format(num1))
print('Número aleatório entre 1 e 10: {}'.format(num2))

# -------------------------------------------------------
# MÓDULO 'emoji' — INSERINDO EMOJIS EM STRINGS
# -------------------------------------------------------
# Este módulo precisa ser instalado separadamente:
#   pip install emoji
#
# Site oficial e documentação:
#   https://pypi.org/project/emoji/

import emoji

print('\nUsando o módulo emoji:')
print(emoji.emojize('Olá, Mundo! :two_hearts:'))

# -------------------------------------------------------
# DESAFIO 01
# -------------------------------------------------------
# Leia um número real e mostre apenas sua parte inteira.
# Exemplo: 6.127 → parte inteira 6

from math import trunc

num = float(input('\nDigite um número decimal: '))
print('O número {} tem a parte inteira {}.'.format(num, trunc(num)))

# -------------------------------------------------------
# DESAFIO 02
# -------------------------------------------------------
# Calcule a hipotenusa de um triângulo retângulo.
# Fórmula: hipotenusa = sqrt(oposto² + adjacente²)

from math import hypot

oposto = float(input('\nDigite o valor do cateto oposto: '))
adjacente = float(input('Digite o valor do cateto adjacente: '))

print('O valor da hipotenusa é {:.2f}'.format(hypot(oposto, adjacente)))

# -------------------------------------------------------
# DESAFIO 03
# -------------------------------------------------------
# Dado um ângulo, mostre o seno, cosseno e tangente.
# Observação: as funções trigonométricas em Python trabalham
# com **radianos**, não com graus.

from math import sin, cos, tan, radians

angulo = float(input('\nDigite o valor do ângulo em graus: '))
rad = radians(angulo)  # Converte graus → radianos

print('-' * 25)
print('O seno de {:.1f}° é {:.3f}'.format(angulo, sin(rad)))
print('O cosseno de {:.1f}° é {:.3f}'.format(angulo, cos(rad)))
print('A tangente de {:.1f}° é {:.3f}'.format(angulo, tan(rad)))
print('-' * 25)

# -------------------------------------------------------
# DESAFIO 04
# -------------------------------------------------------
# Sorteie um aluno para apagar o quadro.

from random import choice

alunos = [
    input('\nDigite o primeiro nome: '),
    input('Digite o segundo nome: '),
    input('Digite o terceiro nome: '),
    input('Digite o quarto nome: ')
]

print('O aluno sorteado foi: {}'.format(choice(alunos)))

# -------------------------------------------------------
# DESAFIO 05
# -------------------------------------------------------
# Sorteie a ordem de apresentação dos alunos.

from random import shuffle

alunos = [
    input('\nDigite o primeiro nome: '),
    input('Digite o segundo nome: '),
    input('Digite o terceiro nome: '),
    input('Digite o quarto nome: ')
]

shuffle(alunos)
print('A ordem de apresentação será:')
for i, nome in enumerate(alunos, start=1):
    print(f'{i}º → {nome}')

# -------------------------------------------------------
# DESAFIO 06
# -------------------------------------------------------
# Reproduza um arquivo de áudio MP3 com pygame.
# O arquivo MP3 precisa estar na mesma pasta do script.

import pygame
pygame.init()

pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()  # Mantém o programa rodando até o áudio terminar