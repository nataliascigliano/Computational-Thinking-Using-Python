## exercicio if else aula 06
seu_nome = input("Digite o seu nome: ")
sua_idade = int(input("Digite a sua idade: "))
nome_colega = input("Digite o nome do seu colega: ")
idade_colega = int(input("Digite a idade dele: "))


##a diferença de idade entre vocês, chamando pelo nome, sem que a resposta seja um número negativo.
##quantas vezes a pessoa mais velha é mais velha, limitando a resposta a 2 casas decimais.
if sua_idade > idade_colega:
    diferenca_idade = sua_idade - idade_colega
    vezes_mais_velho = sua_idade / idade_colega
    print(f"{seu_nome} é {diferenca_idade} anos mais velho que {nome_colega}")
    print(f"A pessoa mais velha é {vezes_mais_velho:.2f} vezes mais velha do que a mais nova")
    if sua_idade > 18:
        maior_idade = sua_idade - 18
        idade_aposento = 75 - sua_idade
        print(f"{seu_nome} já é maior de idade há {maior_idade} anos, e faltam {idade_aposento} anos para se aposentar.")
    if sua_idade < 18:
        maior_idade = 18 - sua_idade
        print(f"{seu_nome} ainda faltam {maior_idade} anos para você atingir sua maioridade.")
        if sua_idade >= 12:
            print(f"{seu_nome} você é adolescente.")
        else: print(f"Você ainda é uma criança.")

if sua_idade < idade_colega:
    diferenca_idade = idade_colega - sua_idade
    vezes_mais_velho = idade_colega / sua_idade
    print(f"{nome_colega} é {diferenca_idade} anos mais velhx que {seu_nome}")
    print(f"A pessoa mais velha é {vezes_mais_velho:.2f} vezes mais velha do que a mais nova.")
    if idade_colega > 18:
        maior_idade = idade_colega - 18
        idade_aposento = 75 - idade_colega
        print(f"{nome_colega}, você já é maior de idade há {maior_idade} anos, e faltam {idade_aposento} anos para você se aposentar.")
    if idade_colega < 18:
        maior_idade = 18 - idade_colega
        print(f"{nome_colega}, ainda faltam {maior_idade} anos para você ser maior de idade.")
        if idade_colega >= 12:
            print(f"{nome_colega}, você ainda é adolescente.")
        else: print(f"{nome_colega} você ainda é uma criança.")
