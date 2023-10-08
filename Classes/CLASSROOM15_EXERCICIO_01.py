"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome {nome}
        Seu nome invertido é  {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primera letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba "Desculpe, você deixou campos vazios."

"""
nome = input('Digite o seu nome: ')
idade = input('Digite sua idade: ')

if not nome or not idade:
    print('Desculpe, você deixou campos vazios.')
else:
    print(f'Seu nome: {nome}')
    print(f'Seu nome invertido: {nome[::-1]}')
    if ' ' in nome:
        print(f'Seu nome contém espaços')
    else:
        print(f'Seu nome não contém espaços')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')    
    print(f'A última letra do seu nome é {nome[-1]}')    
