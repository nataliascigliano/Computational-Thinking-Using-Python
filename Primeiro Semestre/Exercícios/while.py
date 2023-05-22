### EXERCÍCIOS
# 1) imprima a tabuada do número 5, de 0 e 10, inclusive.
for i in range(11):
    print("5 x", i, "=", 5*i)
# Depois, adapte o programa para receber dois números do usuário: o de início e o de fim
inicio = int(input("Digite o valor de início da tabuada: "))
fim = int(input("Digite o valor de fim da tabuada: "))

# Imprime a tabuada do número digitado pelo usuário
numero = 5
for i in range(inicio, fim+1):
    print(numero, "x", i, "=", numero*i)



# faça este exercício uma vez utilizando o for, e outra utilizando o while

numero = 5
i = inicio
while i <= fim:
    print(numero, "x", i, "=", numero*i)
    i += 1



# 2) faça um programa que imprima a soma dos números inteiros positivos de 1 a 100, inclusive
# faça este exercício uma vez utilizando o for, e outra utilizando o while

soma = 0
for i in range (1,101):
    soma += i
print("A soma dos números inteiros positivos de 1 a 100 é:", soma)

# 3) Solicitar um número obrigatoriamente inteiro positivo
# do usuário,
# e calcular seu fatorial
##fatorial de um número é a multiplicação dele com todos os que vieram antes dele (sem o 0)
## ex: 3! = 3*2*1 = 6
## ex: 0! = 1


# 4) Solicite dois número ao usuário,
# sendo que o segundo deverá ser obrigatoriamente
# maior que o primeiro

# 5) solicite 2 números ao usuário. Para cada número do 1 ao primeiro número, faça a tabuada dele do 0 até o segundo número
