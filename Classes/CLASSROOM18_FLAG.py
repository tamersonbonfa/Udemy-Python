"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = identidade
class = tipo
valor = valor

"""
#-------- IDENTIDADES SÃO VALORES NA MEMÓRIA, PARA ECONOMIZAR MEMORIA DUAS VARIAVEIS
#   PODEM TER A MESMA IDENTIDADE DEFINIDA PELO PYTHON
v1 = 'a'
v2 = 'a'
print(id(v1))
print(id(v2))

condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')

print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)
