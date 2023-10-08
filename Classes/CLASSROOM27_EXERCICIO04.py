"""
Quantidade de vezes que uma letra aparece em uma frase.

"""

frase = 'O Python é uma linguagem de programação' \
    'multiparadigma.' \
        'Python foi criado por Guido van Rossum.'

# print(frase.count('Python'))

i = 0
qtd_apareceu_mais = 0
letra_apareceu_mais = ''

while i < len(frase):
    letra_atual = frase[i]
    qtd_atual = frase.count(letra_atual)
    if letra_atual == ' ':
        i += 1
        continue
    
    if qtd_apareceu_mais < qtd_atual:
        qtd_apareceu_mais = qtd_atual
        letra_apareceu_mais = letra_atual
    i += 1
    
print('A letra que apareceu mais vezes '
      f'foi "{letra_apareceu_mais}"'
      f' que apareceu {qtd_apareceu_mais}x.')