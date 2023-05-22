#DOCUMENTAÇÃO

def print_formatado(numero):
#digita três aspas ''' e dá enter, que essa documentação entra automaticamente
    '''
    função que imprime o número com exatamente 3 casas decimais.
    :param numero: float ou int
    :return: none (apenas imprime
    '''
    print(f"{numero:.3f}")

def calcula_dobro(n):
    '''
    Função que calcula e retorna o dobro do número
    :param n: Numeral
    :return: o dobro de N
    '''
    dobro = 2*n
    return dobro

print_formatado(2.462562)
valor = calcula_dobro(10)
print(valor)

# *ARGS **KWARGS (Keywords Args)

#se esrecreve com o asterístico (*args), no lugar do "args" pode escrever qualquer coisa, mas tem que ter * antes.
#essa função possibilita ao usuário escrever quantos parâmetros ele quiser.

def soma_todos_numeros(*args)
    soma=0
    for i in args:
        soma+=1
    return soma

def cadastro_interesses(**kwargs)
    print(kwargs)

def procura_livro(**kwargs):
    '''
    função que busca por autor e/ou ano da publicação
    :param kwargs:
    :return:
    '''

    if type(kwargs) == int:
    elif type(kwargs) == "string":

procura_livro(autor = "edgar alan poe")
procura_livro(ano_publicacao = 1985)



soma = soma_todos_numeros(1,2,3,4,5)
print(soma)

#ARGUMENTOS PRÉ-DEFINIDOS

def calcula_dobro(n=0):
## def calcula_dobro(n=float(input("Digite um número")))
    dobro = 2*n
    return dobro

valor = calcula_dobro()
print(valor)


#VER EXERCICIOS FEITOS DESSA AULA