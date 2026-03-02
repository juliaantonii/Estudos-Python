# -------------------------------------------------------
# AULA 10 - DICIONÁRIOS
# -------------------------------------------------------

# Um dicionário em Python é uma estrutura de dados que armazena informações
# no formato "chave: valor". Diferente das listas (que usam índices numéricos),
# os dicionários usam CHAVES nomeadas para acessar seus valores.

# Exemplo de dicionário com três pares de chave:valor
filme = {'titulo':'Star Wars',
         'ano':1977,
         'diretor':'George Lucas'
        }

# .values() retorna todos os valores do dicionário
print(filme.values())   # saída: dict_values(['Star Wars', 1977, 'George Lucas'])

# .keys() retorna todas as chaves do dicionário
print(filme.keys())     # saída: dict_keys(['titulo', 'ano', 'diretor'])

# .items() retorna pares (chave, valor)
print(filme.items())    # saída: dict_items([('titulo', 'Star Wars'), ('ano', 1977), ('diretor', 'George Lucas')])

# Podemos percorrer um dicionário com um loop for
# usando o método .items() para obter chave e valor simultaneamente
for k, v in filme.items():
    print(f'O {k} é {v}.')
# Saída:
# O titulo é Star Wars.
# O ano é 1977.
# O diretor é George Lucas.

# -------------------------------------------------------
# LISTA DE DICIONÁRIOS
# -------------------------------------------------------

# Também é possível criar uma lista contendo vários dicionários.
# Cada dicionário pode representar um "registro" (ex: um filme).
# Isso é muito usado para armazenar vários itens com o mesmo formato de dados.

# locadora é uma LISTA que contém dois DICIONÁRIOS dentro
locadora = [
    {
        'titulo': 'Star Wars',
        'ano': 1977,
        'diretor': 'George Lucas'
    },
    {
        'titulo': 'Avengers',
        'ano': 2012,
        'diretor': 'Joss Whedon'
    }
]

# Exemplo: percorrendo a lista de dicionários
for filme in locadora:
    # Para cada dicionário dentro da lista, mostramos seus valores
    print(f"Título: {filme['titulo']} | Ano: {filme['ano']} | Diretor: {filme['diretor']}")

# Saída esperada:
# Título: Star Wars | Ano: 1977 | Diretor: George Lucas
# Título: Avengers | Ano: 2012 | Diretor: Joss Whedon

# NÃO podemos usar 'estado[:]' como faríamos com listas,
# pois dicionários não suportam fatiamento.
# Em vez disso, usamos o método .copy() para criar uma cópia independente.

estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)

# -------------------------------------------------------
# DESAFIO 01
# -------------------------------------------------------
# Faça um programa que leia nome e média de um aluno guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

turma = list()
aluno = dict()
status = dict()

qtd = int(input('Informe quantos alunos tem: '))

for i in range(qtd):
    aluno['nome'] = str(input(f'\nNome do {i + 1}º aluno: ')).strip().upper()
    aluno['media'] = float(input(f'A média de {aluno['nome']} é: '))
    if aluno['media'] >= 6:
        aluno['status'] = 'APROVADO'
    else:
        aluno['status'] = 'REPROVADO'
    turma.append(aluno.copy())

print('\nRESULTADOS:')
print('-'*59)
for j in turma:
    print(f'| Nome: {j['nome']:>10} | Média: {j['media']:>5.2f}pts | Status: {j['status']:>10} |')

print('-'*59)

# -------------------------------------------------------
# DESAFIO 02
# -------------------------------------------------------
# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses
# resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor
# tirou o maior número no dado.

from random import randint
from operator import itemgetter

resultados = []
pessoa = dict()
ranking = []

for i in range(0,4):
    pessoa['nome'] = str(input(f'\nQual seu nome, jogador {i+1}? '))
    pessoa['dado'] = randint(1,6)
    print(f'Seu dado foi: {pessoa['dado']}')
    resultados.append(pessoa.copy())

ranking = sorted(resultados, key=itemgetter('dado'), reverse=True) # conceito novo
# A função itemgetter('chave') serve para "pegar" o valor de uma chave específica
# dentro de cada dicionário, e usar esse valor como base para ordenação.

print('\nRESULTADOS')
print('-'*30)
for pos, pessoa in enumerate(ranking):
    print(f'| {pos + 1}º | {pessoa['nome']:<10} com dado: {pessoa['dado']:>3} |')
print('-'*30)

# -------------------------------------------------------
# DESAFIO 03
# -------------------------------------------------------
# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade)
# em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de 
# contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date
carteira = dict()
bd = []

qtd = int(input('Quantas pessoas serão cadastradas? '))

for i in range(qtd):
    carteira['nome'] = str(input('\nNome: '))
    carteira['ano_nasc'] = int(input('Ano de nascimento: '))
    carteira['idade'] = (date.today().year - carteira['ano_nasc'])
    carteira['id'] = int(input('Nº CTPS (Caso não tenha, digite 0): '))
    if carteira['id'] != 0:
        carteira['ano_cont'] = int(input('Ano de contratação: '))
        carteira['salario'] = float(input('Salário: '))
    else:
        carteira['ano_cont'] = 'NULL'
        carteira['salario'] = 'NULL'
    carteira['ano_aposentadoria'] = (carteira['ano_cont'] + 35)
    carteira['idade_aposentadoria'] = (carteira['ano_aposentadoria'] - carteira['ano_nasc'])
    bd.append(carteira.copy())

print('-'*105)
print(f'|   Nome   |   Nasc   |   Idade   |   CPTS   |  Ano Cont  |  Salário  |  Ano Aposent  |  Idade Aposent  |')
print('-'*105)
for func, carteira in enumerate(bd):
    print(f'| {carteira['nome']:<8} | {carteira['ano_nasc']:<8} ', end='')
    print(f'| {carteira['idade']:<9} | {carteira['id']:<8} | {carteira['ano_cont']:<10} ', end='')
    print(f'| {carteira['salario']:<9} | {carteira['ano_aposentadoria']:<13} | {carteira['idade_aposentadoria']:<15} |')
print('-'*105)

# -------------------------------------------------------
# DESAFIO 04
# -------------------------------------------------------
# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome
# do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

# -------------------------------------------------------
# DESAFIO 05
# -------------------------------------------------------
# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um
# dicionário e todos os dicionários em uma lista. No final, mostre:
#   A) Quantas pessoas foram cadastradas.
#   B) A média de idade do grupo.
#   C) Uma lista com todas as mulheres.
#   D) Uma lista com todas as pessoas com idade acima da média.

# -------------------------------------------------------
# DESAFIO 06
# -------------------------------------------------------
# Aprimore o DESAFIO 04 para que ele funcione com vários jogadores, incluindo um sistema de visualização
# de detalhes do aproveitamento de cada jogador.