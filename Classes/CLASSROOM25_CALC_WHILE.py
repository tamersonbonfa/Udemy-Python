"""         CALCULADORA COM WHILE       """

while True:
    print(' \n\n Operadores \n "+" - Somar \n "-" - Subtrair \n "*" - Multiplicar \n "/" - Dividir \n "**" - Potencia')
    conta = input('\n\n Digite sua conta:')
    tamanho_conta = len(conta)
    i = 0
    operadores = ['+','-','*','/','**']
    numero1 = ''
    operador = ''
    numero2 = ''
    resultado = 0
    
    while i < tamanho_conta:
        if (conta[i] not in operadores) and operador != '':
            numero2 += conta[i]
            i += 1
        elif conta[i] in operadores:
            operador += conta[i]
            i += 1
        elif conta[i] not in operadores:
            numero1 += conta[i]
            i += 1
    try:        
        numero1 = float(numero1)              
        numero2 = float(numero2)
        
        if operador not in operadores:
            print('\n ATENÇÃO \n Operador inválido.')
        elif operador == '+':
            resultado = numero1 + numero2 
        elif operador == '-':
            resultado = numero1 - numero2 
        elif operador == '*':
            resultado = numero1 * numero2 
        elif operador == '/':
            resultado = numero1 / numero2 
        elif operador == '**':
            resultado = numero1 ** numero2
        else:
            print('\n ATENÇÃO \n Nunca deveria chegar aqui.')
                    
    except:
        resultado = '\n ATENÇÃO \n Números inválidos, tente novamente.'            
            
    
    print(f'\n ATENÇÃO \n O resultado foi:  {resultado}')
    
    sair = input('\n\n Quer sair? [s]im: ').lower().startswith('s')
    
    
    if sair is True:
        break