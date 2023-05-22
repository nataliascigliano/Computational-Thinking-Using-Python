# Exercício 1. Dado um numero pelo usuário, calcular o dobro e o quadrado. Depois, printar junto o número origianal.

#numero_usuario = int (input("Digite um número: "))

#print("Você digitou o número {}. O dobro dele é {}, e o quadrado dele é {}.".format(numero_usuario, numero_usuario * 2, numero_usuario **2))



# Exercício 2. Dados três números pelo usuário, calcular sua média, e a razão(divisão) entre o primeiro e o último
## obs.: definir a resposta a 10 caracteres sendo 3 decimais.

n1 = float (input("Digite a sua N1: "))
n2 = float (input("Digite a sua N2: "))
n3 = float (input("Digite a sua N3: "))
razao = ((n1+n3)/2)
print(razao)
media_total = ((n1+n2+n3)/3)
print('{:*^10.3f}'.format(media_total))
