## Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5
## peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
## O programa deverá escrever na tela se o usuário venceu ou perdeu.

num = int(input("Digite um número de 0 a 5: "))

if num == 3:
    print("Parabéns! Você acertou!")
else: print("Você perdeu!")


##Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar:

num_int = int(input("Digite um número: "))
resultado = num_int % 2

if resultado == 0:
    print("Esse número é PAR")
else: print("Esse número é IMPAR")