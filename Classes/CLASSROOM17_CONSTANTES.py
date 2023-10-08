"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""

velocidade = 50 # velocidade atual do carro
local_carro = 100 # local em que o carro está na estrada

RADAR_1 = 60 # velocidade máxima do radar1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega

carro_passou_radar = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
    
acima_da_velocidade = velocidade > RADAR_1

if acima_da_velocidade:
    print('O carro ultrapassou a velocidade do RADAR.')
else:
    print('O carro não ultrapassou a velocidade do RADAR.')

if carro_passou_radar and acima_da_velocidade:
        print('O carro foi multado.')
else:
    print('O carro não levou uma multa.')
    
    
        

