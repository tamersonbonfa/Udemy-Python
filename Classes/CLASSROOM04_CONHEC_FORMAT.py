"""
CONHECENDO O MÓDULO FORMAT

"""
a = 'A'
b = 'B'
c = 1.1
string = 'a={nome1} b={nome2} c={nome3:.2f}' #2f quantidade de casas decimais
formato = string.format(
    nome1 = a, nome2 = b, nome3 = c
    )


print(formato)#Formato pode ser utilizado para coletar valores