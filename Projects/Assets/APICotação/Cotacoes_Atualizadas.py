# Módulos
from time import sleep
import requests
import json

# Inicialização
print(' ')
print('=' * 36)
print('|{:^34}|'.format('Moedas Hoje!'))
print('=' * 36)
print('|{:^34}|'.format('Principais Moedas Atualizadas!'))
print('=' * 36)
print(' ')

sleep(0.7)
# Váriaveis
cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes = cotacoes.json()
cotacoes_dolar = cotacoes['USDBRL']['bid']
cotacoes_euro = cotacoes['EURBRL']['bid']
cotacoes_bitcoin = cotacoes['BTCBRL']['bid']
cont = 0

# While e Lógica
while True:
    # Consulta
    moeda_consulta = str(input('Olá! qual moeda deseja consultar? [USD/EUR/BTC]: ')).upper().strip()
    cont += 1
    print('=' * 54)

    # Bloco Dólar
    if moeda_consulta == 'USD':
        print(f'O preço do Dólar hoje é de \033[32mR${cotacoes_dolar}!\033[m')
        print('=' * 54)
        condicao = str(input('Deseja fazer mais consultas? [S/N]: ')).upper().strip()
        print('=' * 54)
        if condicao == 'S':
            pass
        else:
            certo = condicao
            break

    # Bloco Euro
    elif moeda_consulta == 'EUR':
        print(f'O preço do Euro hoje é de \033[32mR${cotacoes_euro}!\033[m')
        print('=' * 54)
        condicao = str(input('Deseja fazer mais consultas? [S/N]: ')).upper().strip()
        print('=' * 54)
        if condicao == 'S':
            pass
        else:
            certo = condicao
            break

    # Bloco Bitcoin
    elif moeda_consulta == 'BTC':
        print(f'O preço do Bitcoin hoje é de \033[32mR${cotacoes_bitcoin}!\033[m')
        print('=' * 54)
        condicao = str(input('Deseja fazer mais consultas? [S/N]: ')).upper().strip()
        print('=' * 54)
        if condicao == 'S':
            pass
        else:
            certo = condicao
            break

            # Bloco de Erro
    else:
        print(f"\033[31mERRO!\033[m A sigla digitada '{moeda_consulta}' não existe! ")
        print('Tente novamente! digite entre \033[33m[USD/EUR/BTC]!\033[m')
        print('=' * 54)
        continue

# Finalização
if certo != 'N':
    print(f'\033[31mPrograma parado! {certo} foi digitado! Acerte o digito JKKK!\033[m')
print(f'\033[32mForam feitas {cont} consultas no total!\033[m')
print('-FIM-')
