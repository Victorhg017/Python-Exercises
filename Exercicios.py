"""
1 - Conversão de Fahrenheit para Celsius sendo o cálculo para essa conversão (Fahrenheit = celsius * (9/5)+ 32).
2 - Conversão de Celsius para Fahrenheit sendo o cálculo para essa conversão (Celsius = 5 * (fahrenheit- 32) /9).
3 - Conversão de Kelvin para Celsius sendo o cálculo para essa conversão (Celsius = kelvin - 273.15).
4 - Conversão de Celsius para Kelvin sendo o cálculo para essa conversão (Kelvin = Celsius + 273.15).
5 - Conversão de km/h para m/s sendo o cálculo para essa conversão (metros/s = km_h / 3.6).
6 - Conversão de m/s para km/h sendo o cálculo para essa conversão (km/h = km_h * 3.6).
7 - Conversão de milhas para km sendo o cálculo para essa conversão (km = 1.61 * milhas).
8 - Conversão de km para milhas sendo o cálculo para essa conversão (milhas = 1.61 / milhas).
9 - Conversão conversão de ângulo em graus para radianos sendo o cálculo para essa conversão (graus = radianos * math.pi / 180) --> detalhe que nessa operação vamos utilizar o import math para aplicar o valor de pi(math.pi).
10 - Conversão conversão de radianos para graus sendo o cálculo para essa conversão (radianos = graus * 180 / math.pi).
11 - Faça um programa que leia o valor de um produto e imprima o valor com desconto, tendo em vista que você poderá colocar a % do desconto.
12 - Um montante de 780.000 será divido entre3 ganhadores de um concurso, o primeiro ganhador receberá 46%, o segundo 32%, e o terceiro receberá o restante. Calcule e imprima a quantia que cada um ganhará.
"""







'Códigos e resoluções dos problemas devem ser usados apenas para tirar dúvidas'







"""
1- Celsius = input((f'Digite a temperatura em Fahrenheit: '))

# Fahrenheit = celsius * (9/5)+ 32

print(f'Temperatura em Fahrenheit é {9/5 * float(Celsius) + 32}')
---------------------------------------------------------------------------
2 - Fahrenheit = input((f'Digite a temperatura em Celsius: '))

# Celsius = 5 * (fahrenheit- 32) /9

print(f'Temperatura em Celsius é {5 * (float(Fahrenheit) - 32) / 9}')
----------------------------------------------------------------------------
3 - Kelvin = input(f'Digite a temperatura em Kelvin: ')

# C = kelvin - 273.15

print(f'Temperatura em Celsius é {float(Kelvin) - 273.15 }')
----------------------------------------------------------------------------
4 - Celsius = input(f'Digite a temperatura em Celsius: ')

# Kelvin = Celsius + 273.15

print(f'Temperatura em Kelvin é {float(Celsius) + 273.15 }')
----------------------------------------------------------------------------
5 - km_h = input(f'Digite km por hora: ')

# metros/s = km_h / 3.6

print(f'A conversão de km/h para m/s é {float(km_h) / 3.6}')
-----------------------------------------------------------------------------
6 - metros_s = input(f'Digite km por hora: ')

# km/h = km_h * 3.6

print(f'A conversão de m/s para km/h é {float(metros_s) * 3.6}')
-----------------------------------------------------------------------------
7 - milhas = input(f'Digite uma distância em milhas: ')

#km = 1.61 * milhas

print(f'A conversão de milhas para km é {float(milhas) * 1.61}')
-----------------------------------------------------------------------------
8 - km = input(f'Digite uma distância em km: ')

#milhas = 1.61 / milhas

print(f'A conversão de km para milhas é {float(km) / 1.61}')
-----------------------------------------------------------------------------
import math

9 - graus = input(f'Digite o ângulo em graus: ')

# radianos = graus * math.pi / 180 -->  sendo math.pi o resultado de pi(3.14)

print(f'A conversão do ângulo em graus para radianos é {float(graus) * math.pi /180}')
------------------------------------------------------------------------------
import math

10 - radianos = input(f'Digite o ângulo em radianos: ')

# radianos = graus * 180 / math.pi

print(f'A conversão de radianos para graus é {float(radianos) * 180 / math.pi}')
-------------------------------------------------------------------------------
11 - Valor = float(input(f'Valor atual do produto é '))

porcentagem = int(input(f'Digite a % do desconto '))

desconto = Valor * (porcentagem / 100)

valor_desconto = input(f'Valor total do produto aplicado o desconto de {porcentagem}% é {float(Valor) - desconto}')
--------------------------------------------------------------------------------
12 - Prêmio = 780.000

ganhador1 = Prêmio * (46 / 100)
ganhador2 = Prêmio * (32 / 100)
ganhador3 = Prêmio - ganhador1 - ganhador2

print(f'O primeiro ganhador receberá R${ganhador1:_.3f},00')
print(f'O segundo ganhador receberá R${ganhador2:_.3f},00')
print(f'O terceiro ganhador receberá R${ganhador3:_.3f},00')
"""
