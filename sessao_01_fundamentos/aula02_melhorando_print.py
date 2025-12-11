nome = input('Digite um nome: ')
idade = input('Digite sua idade: ')
# fruta_favorita = input('Qual é sua fruta favorita: ')

print('Olá', nome + ', Você tem', idade, 'anos de idade')


# f-string
# print(f'Olá {nome}, você tem {idade} anos de idade e sua fruta favotita é {fruta_favorita}')
print(f'Olá {nome} daqui 5 anos você terá {idade + 5} de idade')

# TypeError: can only concatenate str (not "int") to str
