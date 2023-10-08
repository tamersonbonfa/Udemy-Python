#CAPTURA A ENTRADA DO USUÁRIO COMO STRING:
primeiro_valor = input('Digite o primeiro valor: ')
segundo_valor  = input('Digite o segundo valor: ')


#       CONVERTE A ENTRADA DE STRING PARA INTEIRO
#  OBS: CONVERTER APENAS QUANDO FOR FAZER ALGUM CÁLCULO
# int_primeiro_valor = int(primeiro_valor)
# int_segundo_valor  = int(segundo_valor)


#CRIAÇÃO DAS CONDIÇÕES
condicao1 = primeiro_valor > segundo_valor
condicao2 = primeiro_valor < segundo_valor
condicao3 = primeiro_valor == segundo_valor

#SAÍDA DE DADOS DE ACORDO COM AS CONDIÇÕES DADAS PELO USUÁRIO
if condicao1:
    print(f'O primeiro valor "{primeiro_valor}" é maior que o segundo valor "{segundo_valor}"')
elif condicao2:
    print(f'O primeiro valor "{primeiro_valor}" é menor que o segundo valor "{segundo_valor}"')
elif condicao3:
    print(f'O primeiro valor "{primeiro_valor}" é igual que o segundo valor "{segundo_valor}"')
