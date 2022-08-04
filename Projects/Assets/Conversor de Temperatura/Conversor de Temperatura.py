# Crie um programa que faça conversão de uma escala de temperatura para a outra, sendo elas: Celsius, Fahrenheit, Kelvin.

# Módulos
from time import sleep

# Apresentação
print('=' * 27)
sleep(0.7)
print('Conversor de temperaturas')
sleep(0.7)
print('=' * 27)
sleep(0.7)
print('''Olá!, este é um programa para a conversão entre as escalas de temperaturas:
[C] Celsius
[F] Fahrenheit
[K] Kelvin''')

# Variáveis
celsius = fahrenheit = kelvin = cont = 0

# Loop While e Converções
while True:

    # Seleção das escalas
    print('=' * 48)
    temperatura_Em_Graus = int(input('Quantos graus serão convertidos?: '))
    temperatura_A_Converter = str(input('De qual temperatura você quer converter?: ')).upper()
    temperatura_Selecionada = str(input('Para qual temperatura você quer converter?: ')).upper()
    print('=' * 48)

    # De Celsius para Fahrenheit
    if temperatura_A_Converter == 'C' and temperatura_Selecionada == 'F':
        celsius = temperatura_Em_Graus
        fahrenheit = celsius * 1.8 + 32
        cont += 1
        print(f'\033[1;32mA temperatura convertida de Celsius {temperatura_Em_Graus}°C!, para Fahrenheit é {fahrenheit:.1f}°F!\033[m')

        # Para mais converções
        condicao = str(input('Deseja fazer mais converções? [S/N]: ')).upper()
        if condicao == 'S':
            pass
        else:
            break
    
    # De Celsius para Kelvin
    elif temperatura_A_Converter == 'C' and temperatura_Selecionada == 'K':
        celsius = temperatura_Em_Graus
        kelvin = celsius + 273
        cont += 1
        print(f'\033[1;32mA temperatura convertida de Celsius {temperatura_Em_Graus}°C!, para Kelvin é {kelvin:.1f}°K!\033[m')

        # Para mais converções
        condicao = str(input('Deseja fazer mais converções? [S/N]: ')).upper()
        if condicao == 'S':
            pass
        else:
            break

    # De Fahrenheit para Celsius
    elif temperatura_A_Converter == 'F' and temperatura_Selecionada == 'C':
        fahrenheit = temperatura_Em_Graus
        celsius = (fahrenheit - 32) / 1.8
        cont += 1
        print(f'\033[1;32mA temperatura convertida de Fahrenhei {temperatura_Em_Graus}°F!, para Celsius é {celsius:.1f}°C!\033[m')

        # Para mais converções
        condicao = str(input('Deseja fazer mais converções? [S/N]: ')).upper()
        if condicao == 'S':
            pass
        else:
            break

    # De Fahrenheit para Kelvin
    elif temperatura_A_Converter == 'F' and temperatura_Selecionada == 'K':
        fahrenheit = temperatura_Em_Graus
        kelvin = (fahrenheit - 32) * 5 / 9 + 273
        cont += 1
        print(f'\033[1;32mA temperatura convertida de Fahrenhei {temperatura_Em_Graus}°F!, para Kelvin é {kelvin:.1f}°K!\033[m')
        
        # Para mais converções
        condicao = str(input('Deseja fazer mais converções? [S/N]: ')).upper()
        if condicao == 'S':
            pass
        else:
            break

    # De Kelvin para Celsius
    elif temperatura_A_Converter == 'K' and temperatura_Selecionada == 'C':
        kelvin = temperatura_Em_Graus
        celsius = kelvin - 273
        cont += 1
        print(f'\033[1;32mA temperatura convertida de Kelvin {temperatura_Em_Graus}°K!, para Celsius é {celsius:.1f}°C!\033[m')

        # Para mais converções
        condicao = str(input('Deseja fazer mais converções? [S/N]: ')).upper()
        if condicao == 'S':
            pass
        else:
            break
    
    # De Kelvin para Fahrenhei
    elif temperatura_A_Converter == 'K' and temperatura_Selecionada == 'F':
        kelvin = temperatura_Em_Graus
        fahrenheit = (kelvin - 273) * 1.8 + 32
        cont += 1
        print(f'\033[1;32mA temperatura convertida de Kelvin {temperatura_Em_Graus}°K!, para Fahrenhei é {fahrenheit:.1f}°F!\033[m')

        # Para mais converções
        condicao = str(input('Deseja fazer mais converções? [S/N]: ')).upper()
        if condicao == 'S':
            pass
        else:
            break
    else:
        print(f'\033[0;31mERRO, tente novamente! \nA conversão entre: {temperatura_Selecionada} e {temperatura_A_Converter}, não existe! \nPor favor digite a temperatura correta!\033[m')
        cont += 1
        cont -= 1

# Finalização
print('=' * 48)
if cont == 1:
    print(f'\033[1;32mForam feitos um total de {cont} converção!\033[m')
else:
    print(f'\033[1;32mForam feitos um total de {cont} converções!\033[m')
print('-FIM-')
