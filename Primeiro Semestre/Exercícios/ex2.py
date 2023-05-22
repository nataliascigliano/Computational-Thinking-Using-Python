num = 29
##formatação de números inteiros:
print(f'Número: {num:.5f}')
print(f'Número: {num:.2f}')
print(f'Número: {num:<5d}')
print(f'Número: {num:>5d}')
print(f'Número: {num:^5d}')

##formatação de variável inteira:
print(f'Número: {num:0^10}')
print(f'Número: {num:0>10}')
print(f'Número: {num:0<10}')

nome = "Natalia"
##aqui é p/ crescer a qtdade de caracteres da variável nome:
print(f'Nome: {nome:*^30s}')
print(f'Nome: {nome:>25s}')
print(f'Nome: {nome:>025s}')


nome_grande = "Natalia Siqueira Cardoso Scigliano"
##aqui é para limitar quando a string é muito grande
print(f'Nome limitado: {nome_grande:.10}')


num_float = 12.0123456789

print('{:.5f}'.format(num_float))
print('{:*<15f}'.format(num_float))
print('{:*>15f}'.format(num_float))
print('{:>15f}'.format(num_float))
print('{:*^15f}'.format(num_float))