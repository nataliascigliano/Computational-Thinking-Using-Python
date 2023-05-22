# Exercício 3. Dado um numero pelo usuário, exibir o anterior e posterior (Ex: input=20, resposta=19 e 21)
# Exercício 4. Dados dois números pelo usuário, calcular a potência entre eles

# numero_usuario = int (input("Digite um número: "))
#
# print("O número que vem antes é o {}, e o que vem depois é o {}.".format(numero_usuario - 1, numero_usuario + 1))

# numero_usuario1 = int (input("Digite um número de 0 a 100: "))
# numero_usuario2 = int (input("Digite outro número: "))
# potencia = int (numero_usuario1 ** numero_usuario2)
#
# print(potencia)


# Exercício 5. Dado um número pelo usuário, exibir o próximo múltiplo de 5

##ler o numero
##calcular o proximo multiplo de 5
##exibir o resultado

numero_usuario = int (input("Digite um número: "))
diferenca = 5 - (numero_usuario % 5)
prox_multiplo = numero_usuario + diferenca
print(f"O próximo número múltiplo de 5 é {prox_multiplo}")

