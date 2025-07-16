# Aula sobre variáveis e tipos de dados

# Tipos de váriáveis
idade = 20 # Int
peso = 55.6 # Float
nome = 'Matheus' # String
ativo = True # Boolean
resultado = None # NoneType

# Exibindo os tipos de variáveis
print('Meu nome é', nome, 'e tenho', idade, 'anos e peso', peso, 'kg.')


# Aula sobre cálculos com números

# Ordem dos operadores 
# 1. parênteses ()
# 2. exponenciação **
# 3. multiplicação *
# 4. Divisão /
# 5. divisão inteira //
# 6. modulo %
# 7. adição +
# 8. subtração -

# Operações matemáticas
a = 10
b = 5
soma = a + b
print('A soma de', a, 'e', b, 'é', soma)
print(10-5)

# Conversão de tipos
alunos_presente = 23
alunos_ausentes = '17'
total_alunos = alunos_presente + int(alunos_ausentes)
print('Total de alunos:', total_alunos)

# Tipos de funções matemáticas
num1 = 10.56
print(round(num1)) #Arredonda o número para o inteiro mais próximo
print(pow(2, 3)) #Calcula 2 elevado a 3
print(max(2,3,8,213,54,23)) #Encontra o maior número
print(min(2,3,8,213,54,23)) #Encontra o menor número
print(sum([2,3,8,213,54,23])) #Soma todos os números da lista

# Modulo math
import math 

print(math.ceil(10.56)) #Arredonda para cima
print(math.floor(10.56)) #Arredonda para baixo
print(math.pow(2, 3)) #Calcula 2 elevado a 3
print(math.sqrt(16)) #Raiz quadrada


# Aula sobre strings


mensagem = 'Olá, mundo!'
print(mensagem[0:5]) #pega os primeiros 5 caracteres
print(mensagem.upper()) # Converte para maiúsculas
print(mensagem.lower()) # Converte para minúsculas
print(mensagem.replace('mundo', 'Python')) # Substitui uma parte da string

# Formatação de f-strings
nome = 'Matheus'
idade = 20
print(f'Meu nome é {nome} e tenho {idade} anos.')

# Sequencias de escape
print('Ele disse: "Olá, mundo!"') # Aspas duplas dentro de uma string
print('Ele disse: \'Olá, mundo!\'') # Aspas simples dentro de uma string
print('Olá, \\mundo!') # Barra invertida
print('Linha 1\nLinha 2') # Quebra de linha
print('Tab\tEspaço') # Tabulação

#Tabulação
mensagem1 = 'Nome:\tMatheus\nIdade:\t20\nPaís:\tBrasil'
print(mensagem1)

# Aula sobre input
nome1 = input('Qual é o seu nome? ')
print(f'Olá, {nome1}!')

nome = input('Digite seu nome completo: ')
idade = input('Digite sua idade: ')
pais = input('Digite seu país: ')
data_nascimento = input('Digite sua data de nascimento: ')
print(f'Me chamo {nome}, tenho {idade} anos, sou do {pais} e nasci em {data_nascimento}.')

# Os dados recebidos pelo input são do tipo string, então é necessário converter para o tipo desejado
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
soma = num1 + num2
print(f'A soma de {num1} e {num2} é {soma}.')

# Exercício de input
valor = float(input('Digite um valor: '))
soma = valor * 1.10
print(f'O valor com 10% de aumento é: {soma:.2f}')

# Multiplas entradas no mesmo input
dados = input('Digite seu nome e idade: ').split()
nome = dados[0]
idade = int(dados[1])
print(f'Nome: {nome}, Idade: {idade}')

""" Operadores de comparação

X == Y: Igualdade
X != Y: Diferença
X > Y: Maior que
X < Y: Menor que
X >= Y: Maior ou igual a
X <= Y: Menor ou igual a """

# Condições 

idade = int(input('Digite sua idade: '))
if idade < 18:
    print('Você é menor de idade.')
elif idade >= 18 and idade < 30: # 1° Forma de usar o elif
    print('Você é Jovem.')
elif 30 >= idade < 65: # 2° Forma de usar o elif
    print('Você é adulto.')
else:
    print('Você é idoso.')

# Exercícios

# Controle de temperatura 

temperatura = int(input('Digite a temperatura em graus Celsius: '))
if temperatura < 10:
    print('Muito frio!')
elif 10 <= temperatura < 20:
    print('Está fresco.')
else:
    print('Está quente.')

# Saudações

hora = int(input('Que horas são? '))
if hora < 12:
    print('Bom dia!')
elif 12 <= hora < 18:
    print('Boa tarde!')
else:
    print('Boa noite!')

# Descontos

valor = float(input('Digite o valor da compra: R$ '))
if valor > 200:
    desconto = valor * 0.20
elif 200 >= valor > 100:
    desconto = valor * 0.10
else:
    desconto = valor * 0.05

valor_final = valor - desconto
print(f'Você ganhou um desconto de R$ {desconto:.2f}. Valor final: R$ {valor_final:.2f}')

# Login Autenticação

usuario = input('Digite seu usuário: ')
senha = input('Digite sua senha: ')
if usuario == 'admin' and senha == '1234':
    print('Acesso concedido!')
else:
    print('Acesso negado! Usuário ou senha incorretos.')

# Desempenho Escolar

nota = int(input('Digite sua nota: '))
if nota >= 9:
    print('Excelente, você tirou A!')
elif 7 <= nota < 9:
    print('Bom trabalho, você tirou B!')
elif 5 <= nota < 7:
    print('Você passou, mas precisa melhorar. Sua nota é C!')
else:
    print('Infelizmente, você foi reprovado.')