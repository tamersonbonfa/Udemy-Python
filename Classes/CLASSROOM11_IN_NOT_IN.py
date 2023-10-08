# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5 6 7
#  T A M E R S O N
# -8-7-6-5-4-3-2-1

# nome = 'TAMERSON'
# print(nome[0])
# print(nome[-4])
# print('TA' in nome)
# print('ONA' in nome)
# print(50 * '-')
# print('TA' not in nome)
# print('ONA' not in nome)

nome = input('Digite o seu nome: ')
encontrar = input('Digite oque deseja encontrar: ')

if not encontrar:
    print(f'{encontrar} não está em {nome}')
elif encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')