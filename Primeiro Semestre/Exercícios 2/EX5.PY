## Desenvolva um programa que pergunte a distância de uma viagem em Km.
## Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200km
## e R$0,45 para viagens mais longas.

distancia = float(input("Digite qual vai ser a distância da sua viagem? Km"))

if distancia <= 200:
    passagem = distancia * 0.50
    print(f"Você vai gastar {passagem:.2f} reais de passagem para ir.")
else:
    passagem = distancia * 0.45
    print(f"Você vai gastar {passagem:.2f} reais de passagem para ir.")