meu_nome = "Natalia Scigliano"
minha_idade = 30
minha_altura = 1.60
meu_email = "nsqcar@gmail.com"

print("Meu nome é", meu_nome, "e eu tenho", minha_idade, "anos."
        "\nJá a minha altura é", minha_altura, "cm."
        "\nMeu e-mail para contato é:", meu_email)

print(f"Meu nome é {meu_nome}, e a minha idade é {minha_idade} anos.")

numero_inteiro_convertido_em_foat=float(15)
print(numero_inteiro_convertido_em_foat)

numero_float_convertido_em_inteiro = int(27.5)
print(numero_float_convertido_em_inteiro)

print("O tipo da variável ({}) é:"\
.format(numero_float_convertido_em_inteiro),type(numero_float_convertido_em_inteiro))


numero_em_string_convertido_para_float=float("25")
print(numero_em_string_convertido_para_float)


print(type(26))
print(type(9.55))
print(type("8"))
print(type(True))

# obs: caso a string seja em formato de float ex: "25.5", você NÃO vai conseguir converter para inteiro
## primeiro terá que converter para float; e depois para inteiro

