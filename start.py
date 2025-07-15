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
