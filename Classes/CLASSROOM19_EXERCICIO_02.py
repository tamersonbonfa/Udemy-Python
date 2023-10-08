"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero_str = input('Digite um número inteiro: ')
try:
    numero_int = int(numero_str)
    if numero_int % 2 == 0:
        print('Este é um número PAR.')
    else:
        print('Este é um número IMPAR.')
except:
    print(f'Este valor "{numero_str}" não é um número inteiro.')



"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora_str = input('Digite a hora atual(números inteiros): ')
try:
    hora_int = int(hora_str)
    manha = hora_int <= 11
    tarde = hora_int >= 12 and hora_int <= 17
    noite = hora_int >= 18 and hora_int <=23
    if hora_int < 24:    
        if   manha:
            print('Bom dia')
        elif tarde:
            print('Boa tarde')
        elif noite:
            print('Boa noite')
    else:
        print(f'Este valor "{hora_str}" não é uma hora válida.')

except:
    print(f'Este valor "{hora_str}" não é um numero inteiro.')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Digite seu Primeiro nome: ')
tamanho_nome = len(nome)
curto = tamanho_nome <= 4 
normal = tamanho_nome >= 4 and tamanho_nome <= 6
grande = tamanho_nome >= 7

if tamanho_nome >= 1:
    if curto:
        print('Seu nome é curto')
    elif normal:
        print('Seu nome é normal')
    elif grande:
        print('Seu nome é muito grande')
else:
    print('Por favor digite um nome.')
