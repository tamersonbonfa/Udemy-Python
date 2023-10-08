"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - esquerda
< - direita
^ - centro
= - Força o número a aparecer antes do ZERO
Sinal + ou -
Ex.: 0>100,.1f
Conversion flags - !r !s !a

"""

variavel = 'abc'
print(f'{variavel}.')
print(f'{variavel: >10}.')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{100.05469584546:0=+10.1f}')
print(f'O hexadecimal de 1500 é {1510:08X}')