# -------------------------------------------------------
# AULA 05 - MANIPULAÇÃO DE TEXTO
# -------------------------------------------------------

# -------------------------------------------------------
# FUNÇÃO len() → retorna o tamanho de uma string (número de caracteres)
# -------------------------------------------------------
frase = "Curso em Vídeo Python"
print(len(frase))  # Saída: 21 (conta todos os caracteres, inclusive espaços)

# -------------------------------------------------------
# FATIAMENTO DE STRINGS
# -------------------------------------------------------
# [início:fim:passo]
# - início: índice inicial (inclusivo)
# - fim: índice final (exclusivo)
# - passo: intervalo de avanço (opcional)

print(frase[9:14])   # Pega do índice 9 até o 13 → "Vídeo"
print(frase[:5])     # Do início até o índice 4 → "Curso"
print(frase[15:])    # Do índice 15 até o fim → "Python"
print(frase[9::3])   # Do índice 9 até o fim, pulando de 3 em 3 → "VdoPh"

# -------------------------------------------------------
# ANÁLISE DE STRINGS
# -------------------------------------------------------
# count() → conta quantas vezes um caractere aparece
# find() → mostra o índice da primeira ocorrência de um texto

print(frase.count('o'))        # Quantos 'o' tem → 3
print(frase.count('o', 0, 13)) # Conta 'o' entre índices 0 e 12 → 2
print(frase.find('Vídeo'))     # Retorna a posição onde começa → 9
print(frase.find('Android'))   # Se não encontrar → -1 (significa "não existe")

# -------------------------------------------------------
# MODIFICAÇÃO DE STRINGS
# -------------------------------------------------------
# replace() → substitui uma parte do texto por outra

print(frase.replace('Python', 'Android'))  # Troca 'Python' por 'Android'

# -------------------------------------------------------
# DESAFIO 01
# -------------------------------------------------------
# Leia o nome completo de uma pessoa e mostre:
# 1. Nome em maiúsculas
# 2. Nome em minúsculas
# 3. Quantas letras tem (sem contar espaços)
# 4. Quantas letras tem o primeiro nome

nome = input('\nDigite seu nome completo: ').strip()  # strip() remove espaços antes/depois

print('Seu nome em maiúsculas: {}'.format(nome.upper()))
print('Seu nome em minúsculas: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))

# O método split() separa o texto em partes (lista de palavras)
partes = nome.split()
print('Seu primeiro nome é "{}" e ele tem {} letras.'.format(partes[0], len(partes[0])))

# -------------------------------------------------------
# DESAFIO 02
# -------------------------------------------------------
# Leia um número de 0 a 9999 e mostre cada dígito separado.

num = int(input('\nDigite um número de 0 a 9999: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

# -------------------------------------------------------
# DESAFIO 03
# -------------------------------------------------------
# Leia o nome de uma cidade e diga se ela começa com “Santo”.

cidade = str(input('\nDigite o nome de uma cidade: ')).strip()
# .lower() → transforma tudo em minúsculas
# .split()[0] → pega apenas a primeira palavra
print('A cidade começa com "Santo"? {}'.format(cidade.lower().startswith('santo')))

# -------------------------------------------------------
# DESAFIO 04
# -------------------------------------------------------
# Leia o nome de uma pessoa e diga se ela tem "Silva" no nome.

nome = str(input('\nDigite seu nome completo: ')).strip()
print('Seu nome tem "Silva"? {}'.format('silva' in nome.lower()))

# -------------------------------------------------------
# DESAFIO 05
# -------------------------------------------------------
# Leia uma frase e diga:
# - Quantas vezes aparece a letra “A”
# - A posição da primeira e da última ocorrência

frase = str(input('\nDigite uma frase: ')).strip().lower()

print('A letra "A" aparece {} vezes.'.format(frase.count('a')))
print('A primeira letra "A" está na posição {}.'.format(frase.find('a') + 1))
print('A última letra "A" está na posição {}.'.format(frase.rfind('a') + 1))

# -------------------------------------------------------
# DESAFIO 06
# -------------------------------------------------------
# Leia o nome completo e mostre o primeiro e o último nome separadamente.

nome = str(input('\nDigite seu nome completo: ')).strip()
partes = nome.split()

print('Seu primeiro nome é {}.'.format(partes[0]))
print('Seu último nome é {}.'.format(partes[-1]))  # [-1] pega o último item da lista