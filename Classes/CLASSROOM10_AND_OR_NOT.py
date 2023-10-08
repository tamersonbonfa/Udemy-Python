"""
Operadores Lógicos
and (e) or (ou) not (não)

and Todas as condições precisam ser
verdadeiras.
Se qualquer valor for considerado falso,
a expressão inteira será avaliada naquele valor

São considerados falsy (que você já viu):
0 0.0 '' False
Também existe o tipo None que é 
usado pare representar um não valor

"""
#PARA NO PRIMEIRO VALOR FALSO E RETORNA FALSO
#avaliação de curto circuito
print(True and True and 1 and 'abc' and 0)

#PARA NO PRIMEIRO VALOR VERDADEIRO
#avaliação de curto circuito
print(0 or False or 0 or 'abc' or True)


 ########### ---- NOT ---- #############
#   UTILIZADO PARA INVERTER EXPRESSÕES, 
# not True = False
# not False = True
print(not True)
print(not False)

senha = input('Senha: ')

if not senha:
     print('Senha incorreta.')
elif senha == '123456':
    print('Senha correta.')
else:
    print('Senha incorreta.')
     
    

 ########### ---- OR ---- #############
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

#if True:
if (entrada == 'E' or 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')



 ########### ---- AND ---- #############
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

#if True:
if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')


