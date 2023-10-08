#if / elif ..... / else
#se / senãose..... /senão

#   O if pode ser utilizado sozinho (sem o elif ou else) porém o elif e else não podem
# ser executados sem o if. Para cada if será executada a primeira condição que for encontrada como "True"

condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = False

if condicao1:
    print('Condicao1')
elif condicao2:
    print('Condicao2')
elif condicao3:
    print('Condicao2')
elif condicao4:
    print('Condicao2')
else:
    print('Este é o código do primeiro else')
    

if 10 == 10:
    print('Outro if')
    

print('Fora do if')