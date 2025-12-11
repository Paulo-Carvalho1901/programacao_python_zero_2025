# nome = input('Digite um nome: ')
# idade = int(input('Digite sua idade: '))


# f-string
# print(f'Olá {nome} daqui 5 anos você terá {idade + 5} amos de idade')

# erro
# TypeError: can only concatenate str (not "int") to str

# print(type(nome))
# print(type(idade))


# Operadores aritimeticos
num1 = 10
num2 = 3

print(num1 + num2) # soma
print(num1 - num2) # subtração
print(num1 * num2) # multiplicação
print(num1 / num2) # divisao todo divisao simples retorna um float
print(num1 // num2) # divisao inteira retona um int
print(num1 % num2) # resto da divisao
print(num1 ** num2) # potencia


# criando calculo de desconto
# preco = 50 # Valor em Real
# desconto = 10 # desconto em porcentagem

preco = float(input('Digite o preço do produto: '))
desconto = float(input('Digite o total do desconto: '))

# calculo
# preco - preco * desconto / 100
novo_preco = preco - (preco * desconto / 100)
print(f'O valor com desconto é de R$ {novo_preco} reais')
