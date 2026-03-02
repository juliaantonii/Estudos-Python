# -------------------------------------------------------
# AULA 02 - TIPOS PRIMITIVOS E MANIPULAÇÃO DE DADOS
# -------------------------------------------------------

# A função input() lê um valor digitado pelo usuário.
# Por padrão, tudo o que vem do input() é do tipo string (str).
# Por isso, quando queremos trabalhar com números, precisamos converter.

v1 = int(input("Digite um valor inteiro: "))
v2 = float(input("Digite um valor decimal: "))
v3 = bool(input("Digite um valor lógico (pressione Enter para False): "))
v4 = str(input("Digite um texto: "))

print("\nTipos informados:")
print("v1:", type(v1))
print("v2:", type(v2))
print("v3:", type(v3))
print("v4:", type(v4))

# -------------------------------------------------------
# DESAFIO 01
# -------------------------------------------------------
# Crie um programa que leia dois números e mostre a soma deles.

valor1 = int(input("\nInsira um valor inteiro: "))
valor2 = int(input("Insira outro valor inteiro: "))
soma = valor1 + valor2

# O método .format() permite inserir variáveis diretamente no texto
print("A soma dos valores {} e {} é igual a: {}".format(valor1, valor2, soma))

# também poderíamos usar f-strings (forma mais moderna):
# print(f"A soma dos valores {valor1} e {valor2} é igual a: {soma}")

# -------------------------------------------------------
# DESAFIO 02
# -------------------------------------------------------
# Faça um programa que leia algo pelo teclado e mostre na tela
# o seu tipo primitivo e todas as informações possíveis sobre ele.

v1 = input("\nDigite algo: ")

# A seguir, vamos usar vários métodos das strings para analisá-las.
# Cada método retorna True ou False (booleano), dependendo da análise.

print("Só tem letras?          ", v1.isalpha())     # True se tiver apenas letras (sem números ou espaços)
print("É alfanumérico?         ", v1.isalnum())     # True se tiver letras e/ou números (sem símbolos)
print("É decimal?              ", v1.isdecimal())   # True se todos os caracteres forem dígitos (0-9)
print("É numérico?             ", v1.isnumeric())   # True para números (inclusive fracionários e romanos)
print("É imprimível?           ", v1.isprintable()) # True se todos os caracteres puderem ser exibidos (sem \n, \t, etc.)
print("É ASCII?                ", v1.isascii())     # True se todos os caracteres estiverem na tabela ASCII (sem acentos)
print("Está em maiúsculas?     ", v1.isupper())     # True se todas as letras forem maiúsculas
print("Está em minúsculas?     ", v1.islower())     # True se todas as letras forem minúsculas
print("Está capitalizado?      ", v1.istitle())     # True se começar com letra maiúscula e o resto minúsculo
