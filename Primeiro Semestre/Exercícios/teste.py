meu_nome = input("Qual o seu nome? ")
minha_idade = int(input("Qual a sua idade? "))
nome_colega = input("Qual o nome do seu colega? ")
idade_colega = int(input("Qual a idade do seu colega? "))
if minha_idade > idade_colega:
    dif = minha_idade - idade_colega
    vezes_mais_velho = minha_idade / idade_colega
    print("{} é {} anos mais velho que {}".format(meu_nome, dif, nome_colega))
    print("A pessoa mais velha é {:.2f} vezes mais velha que a mais nova".format(vezes_mais_velho))
    if minha_idade > 18:
        maior = minha_idade - 18
        aposentar = 75 - minha_idade
        print("{} fez 18 anos há {} anos, além disso faltam {} anos para se aposentar".format(meu_nome, maior, aposentar))
    if minha_idade < 18:
        tmp_fzr18 = 18 - minha_idade
        print("{} é menor de idade e falta(m) {} ano(s) para fazer 18 anos".format(meu_nome, tmp_fzr18))
        if minha_idade <= 12:
            print("{} ainda é uma criança".format(meu_nome))
        else:
            print("{} ja é adolescente".format(meu_nome))
if minha_idade < idade_colega:
    dif = idade_colega - minha_idade
    vezes_mais_velho = idade_colega / minha_idade
    print("{} é {} anos mais velho que {}".format(nome_colega, dif, meu_nome))
    print("A pessoa mais velha é {:.2f} vezes mais velha que a mais nova".format(vezes_mais_velho))
    if idade_colega > 18:
        maior = idade_colega - 18
        aposentar = 75 - idade_colega
        print("{} fez 18 anos há {} anos, além disso faltam {} anos para se aposentar".format(nome_colega, maior, aposentar))
    if idade_colega < 18:
        tmp_fzr18 = 18 - idade_colega
        print("{} é menor de idade e falta(m) {} ano(s) para fazer 18 anos".format(nome_colega, tmp_fzr18))
        if idade_colega < 12:
            print("{} ainda é uma criança".format(nome_colega))
        else:
            print("{} ja é adolescente".format(nome_colega))