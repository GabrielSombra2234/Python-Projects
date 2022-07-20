#Bibliotecas
from time import sleep

#Decoração
print('=-' * 20)
sleep(0.7)
print('             Calculadora ')
sleep(0.7)
print('=-' * 20)
sleep(0.7)

#print
print('Lista de ações:')
sleep(0.7)
print('''
[ 1 ] Somar
[ 2 ] Subtrair
[ 3 ] Dividir
[ 4 ] Multiplicar
[ 5 ] Outro Cálculo
[ 6 ] Sair
''')

#váriaveis
numero_1 = float(input('Digite um número: '))
sleep(0.3)
numero_2 = float(input('Digite outro número: '))
sleep(0.3)
print('=-' * 20)
decisao = int(input('O que você deseja fazer: '))
print('=-' * 20)

#while
while True:

    #soma
    if decisao == 1:
        valor_1 = numero_1 + numero_2
        print('==' * 24)
        print(f'A soma entre {numero_1:.2f} e {numero_2:.2f} é igual a {valor_1:.2f}.')
        print('==' * 24)
        avanco = str(input('Desejá continuar [S/N]: ')).upper()
        if avanco == 'N':
            break
        else:
            print('''
                    [ 1 ] Somar
                    [ 2 ] Subtrair
                    [ 3 ] Dividir
                    [ 4 ] Multiplicar
                    [ 5 ] Outro Cálculo
                    [ 6 ] Sair
                    ''')
            decisao  = int(input('O que deseja fazer: '))

    #subtração
    elif decisao == 2:
        valor_2 = numero_1 - numero_2
        print('==' * 24)
        print(f'A subtração entre {numero_1:.2f} e {numero_2:.2f} é igual a {valor_2:.2f}.')
        print('==' * 24)
        avanco = str(input('Desejá continuar [S/N]: ')).upper()
        if avanco == 'N':
            break
        else:
            print('''
                    [ 1 ] Somar
                    [ 2 ] Subtrair
                    [ 3 ] Dividir
                    [ 4 ] Multiplicar
                    [ 5 ] Outro Cálculo
                    [ 6 ] Sair
                    ''')
            decisao = int(input('O que deseja fazer: '))

    #divisão
    elif decisao == 3:
        valor_3 = numero_1 / numero_2
        print('==' * 24)
        print(f'A divisão entre {numero_1:.2f} e {numero_2:.2f} é igual a {valor_3:.2f}.')
        print('==' * 24)
        avanco = str(input('Desejá continuar [S/N]: ')).upper()
        if avanco == 'N':
            break
        else:
            print('''
                    [ 1 ] Somar
                    [ 2 ] Subtrair
                    [ 3 ] Dividir
                    [ 4 ] Multiplicar
                    [ 5 ] Outro Cálculo
                    [ 6 ] Sair
                    ''')
            decisao = int(input('O que deseja fazer: '))

    #multiplicação
    elif decisao == 4:
        valor_4 = numero_1 * numero_2
        print('==' * 24)
        print(f'A divisão entre {numero_1:.2f} e {numero_2:.2f} é igual a {valor_4:.2f}.')
        print('==' * 24)
        avanco = str(input('Desejá continuar [S/N]: ')).upper()
        if avanco == 'N':
            break
        else:
            print('''
                    [ 1 ] Somar
                    [ 2 ] Subtrair
                    [ 3 ] Dividir
                    [ 4 ] Multiplicar
                    [ 5 ] Outro Cálculo
                    [ 6 ] Sair
                    ''')
            decisao = int(input('O que deseja fazer: '))

    #Outro Cálculo
    elif decisao == 5:
        numero_1 = float(input('Digite um novo número: '))
        sleep(0.3)
        numero_2 = float(input('Digite outro novo número: '))
        sleep(0.3)
        if avanco == 'N':
            break
        else:
            print('''
                    [ 1 ] Somar
                    [ 2 ] Subtrair
                    [ 3 ] Dividir
                    [ 4 ] Multiplicar
                    [ 5 ] Outro Cálculo
                    [ 6 ] Sair
                    ''')
            decisao = int(input('O que deseja fazer: '))

    #Sair
    elif decisao == 6:
        break

    #Número Errado
    else:
        print('Digito não reconhecido!, tente novamente!')
        print('''
                [ 1 ] Somar
                [ 2 ] Subtrair
                [ 3 ] Dividir
                [ 4 ] Multiplicar
                [ 5 ] Outro Cálculo
                [ 6 ] Sair
                ''')
        decisao = int(input('O que deseja fazer: '))        
print('-FIM-')
