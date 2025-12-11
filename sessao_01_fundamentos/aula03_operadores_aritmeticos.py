nome = input('Digite um nome: ')
idade = int(input('Digite sua idade: '))


# f-string
print(f'Olá {nome} daqui 5 anos você terá {idade + 5} amos de idade')

# erro
# TypeError: can only concatenate str (not "int") to str

# print(type(nome))
# print(type(idade))