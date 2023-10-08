"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar

"""

numero_str = input(
    'Digite o número que você quer dobrar: '
    )
try:
    print('STR: ', numero_str)
    numero_float = float(numero_str)
    print('FLOAT: ', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')

except:
    print('Isso não é um número.')

# print(numero_str.isnumeric())

# if numero_str.isnumeric():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
# else:
#     print('Isso não é um número.')