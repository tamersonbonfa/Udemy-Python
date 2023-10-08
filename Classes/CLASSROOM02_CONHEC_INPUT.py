#Input é utilizado na coleta de dados e sempre retorna uma string


nome = input("Digite seu nome: ") 
sobrenome = input("Digite seu sobrenome: ")
idade = input("Digite sua idade: ")
ano_nascimento = input("Digite o ano do seu nascimento: ")
if int(idade) >= 18:
    maior_de_idade = "Sim" 
else:
    maior_de_idade = "Não"  

    
altura_metros = input('Digite sua altura em metros(Utilize "."): ')



print('\n\n\n\n\n\n')
print("Nome: ", nome)
print("Sobrenome: ", sobrenome)
print("Idade: ", idade)
print("Ano de nascimento: ", ano_nascimento)
print("É maior de idade: ", maior_de_idade)
print("Altura em metros: ", altura_metros)

