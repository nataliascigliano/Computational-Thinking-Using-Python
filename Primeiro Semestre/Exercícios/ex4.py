nome = "Computational Thinking using Python"
tamanho = len(nome) # Conta os caracteres da string
todas_maiusculas = nome.upper() # Converte tudo em maiúsculo
todas_minusculas = nome.lower() # Converte tudo em minúsculo
iniciais_maiusculas = nome.title() # Somente as iniciais em maiúsculo
print(f"{nome} possui {tamanho} caracteres")
print(f"Tudo maiúsculo: {todas_maiusculas}")
print(f"Tudo minúsculo: {todas_minusculas}")
print(f"Iniciais maiúsculas: { iniciais_maiusculas }")

print("{} possui {} caracteres".format(nome,tamanho))