# relembrar operações matemáticas ########

# comentar várias linhas = ctrl + /

# operadores lógicos:#########
'''
maior que >
menor que <
menor ou igual <=
maior ou igual >=
diferente !=
igualdade ==
'''

print(0 == 0)
print(0 == 0.0)
print(0 == "0")

##type = diz o tipo da variável que está dentro dele
print(type(0) == type(0.0))

print(type(0 == 0))
print(type(True))

minha_idade = 29
idade_do_colega = 35

print("Eu sou mais velho que meu colega?", minha_idade < idade_do_colega)

# mais opções de formatação/funções em string #####

num = 23
print(f"Número {num}")
print(f"Número {num:5d}")
print(f"Número {num:05d}")
print(f"Número {num:>05d}")
##formas de pular linha: print() ou \n dentro do texto
print()
print(f"Número {num:<05d}")
print("Número\n {:<05d}".format(num))
print()
print(f"Número {num:^06d}") ##esse acento circunflexo é para colocar o numero no centro

nome = 'Natalia'
print(f"Nome = {nome:*>10s}")

Num_float=12.0123456789
print('{:>010f}'.format(Num_float))
print('{:*^16.5f}'.format(Num_float ))
