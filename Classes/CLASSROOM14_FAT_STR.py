"""
Fatiamento de strings
 012345678
 Ola mundo
-987654321
 
Fatiamento [i:f:p] [::] (I = INICIO    -    F = FIM    -     P = PASSO(Quantos caracteres ira pular) )

obs.: a função len retorna a qtd de caracteres da str

"""
variavel = 'Olá mundo'

print(variavel[0:len(variavel):1])
print(variavel[-1:-10:-1])
print(variavel[::-1])
print(variavel[0:9:2])
print(variavel[-1:-10:-2])
print(len(variavel))

print(variavel[4:])
print(variavel[4:9])
print(variavel[0:3])
print(2 * '\n')
print(variavel[-5:])
print(variavel[-5:-1])
print(variavel[-9:-6])