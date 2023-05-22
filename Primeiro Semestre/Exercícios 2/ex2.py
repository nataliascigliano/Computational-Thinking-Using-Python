## exercício de conversor de moedas
## crie um programa que mostre quanto de dinheiro a pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real = float(input("Digite quantos reais você tem na carteira: R$"))
dolar = real/5.24
euro = real/5.64
print(f"Você tem {real:.2f} reais. Você pode comprar {dolar:.2f} dólares e {euro:.2f} euros.")