"""
    Aspas triplas são:
    DocString (NÃO É UM COMENTÁRIO)
    
    Usar para escrever notas.
    
"""
#\r\n -> CRLF
#\n -> LF

#Argumento "END" colocar caracter no fim da linha

# Cerquilhas permitem escrever um comentário
# Print codigo para imprimir
print(1 + 1, 2*4, 5/2, sep = " - ", end= '\n\r') # Comentários podem ser utilizados na frente;
print(2 + 1, 4*4, 8/2, sep = " . ", end= '\n') # SEP é um argumento para utilizar separadores;
print(2 + 1, 4*4, 8/2, sep = " ", end= '') # Comentários podem ser utilizados na frente;
