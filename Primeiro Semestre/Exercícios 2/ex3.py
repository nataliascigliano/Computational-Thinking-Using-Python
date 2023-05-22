preco = float(input("Digite o preço do produto: R$"))
novo_preco = preco - (preco * 0.05)

print(f"O novo preço do seu produto com desconto é: RS{novo_preco}")


##faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input("Digite o valor do seu salário: "))
salario_aumentado = salario + (salario * 0.15)

print(f"O seu salário de {salario} reais, vai aumentar para {salario_aumentado} reais.")