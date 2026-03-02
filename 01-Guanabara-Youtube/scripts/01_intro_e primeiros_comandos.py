# -------------------------------------------------------
# AULA 01 - INTRODUÇÃO AO PYTHON
# -------------------------------------------------------

# Primeiro comando clássico
print('Olá, Mundo!')

# -------------------------------------------------------
# ENTRADA DE DADOS
# -------------------------------------------------------
# A função input() lê uma entrada do usuário como string.

nome = input('Qual é o seu nome? ')
idade = input('Quantos anos você tem? ')
peso = input('Qual é o seu peso? ')

print('Nome:', nome, '| Idade:', idade, '| Peso:', peso)

# -------------------------------------------------------
# DESAFIO 01
# -------------------------------------------------------
# Escreva um programa que pergunte o nome do usuário e mostre uma saudação.

nome = input('Qual é o seu nome? ')
print('Olá,', nome, '! Prazer em te conhecer!')
print('Olá, {}! Prazer em te conhecer!'.format(nome))

# -------------------------------------------------------
# DESAFIO 02
# -------------------------------------------------------
# Faça um programa que pergunte a data de nascimento do usuário
# e mostre uma frase com os dados formatados.

dia = input('Em que dia você nasceu? ')
mes = input('Em que mês você nasceu? ')
ano = input('Em que ano você nasceu? ')


print('Você nasceu no dia', dia, 'de', mes, 'de', ano, '. Correto?')
print('Você nasceu no dia {} de {} de {}. Correto?'.format(dia, mes, ano))

# -------------------------------------------------------
# DESAFIO 03
# -------------------------------------------------------
# Crie um programa que leia dois números e mostre a soma entre eles.

valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor: '))
soma = valor1 + valor2

print('A soma entre os valores é:', soma)
print('A soma entre os valores é: {}!'.format(soma))

# -------------------------------------------------------
# EXPLICAÇÃO: TIPOS PRIMITIVOS
# -------------------------------------------------------
# int   -> números inteiros (ex: 7, -3, 0)
# float -> números reais, com casas decimais (ex: 4.5, -0.7)
# bool  -> valores lógicos (True / False)
# str   -> cadeias de caracteres (textos)

# Dica: use type() para descobrir o tipo de uma variável
# Exemplo:
# print(type(valor1))
