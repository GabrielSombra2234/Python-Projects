#Bibliotecas#
from time import sleep
#import math#

#Decoração#
print('=-' * 20)
sleep(0.7)
print('             Calculadora ')
sleep(0.7)
print('=-' * 20)
sleep(0.7)

#Variáveis e if suplementar#
infu = int(input('Quantos numeros você quer calcular: '))
if infu == 0:
    print('Número invalido!, digite novamente.')
    infu = int(input('Quantos numeros você quer calcular: '))

#print e variável suplementar#
print('Lista de ações:')
sleep(0.7)
print('''
[ 1 ] Somar
[ 2 ] Subtrair
[ 3 ] Dividir
[ 4 ] Multiplicar
[ 5 ] Outro Cálculo
''')
atitude = int(input('O que você quer fazer: '))
sleep(0.7)
print('=-' * 15)
sleep(0.7)

#For e Ifs#
for cont in range(0, infu):
    numero_calculavel = float(input('Digite um número: '))
    numero_calculavel_2 = float(input('Digite um número: '))
    if atitude == 1:
        resultado = numero_calculavel + numero_calculavel_2
        print('A soma entre {} e {}, resulta em {:.2f}'.format(numero_calculavel, numero_calculavel_2 ,resultado))
    elif atitude == 2:
        resultado_2 = numero_calculavel - numero_calculavel_2
        print('A subtração entre {} e {}, resulta em {:.2f}'.format(numero_calculavel, numero_calculavel_2 ,resultado_2))
    elif atitude == 3:
        resultado_3 = numero_calculavel / numero_calculavel_2
        print('A divisão entre {} e {}, resulta em {:.2f}'.format(numero_calculavel, numero_calculavel_2 ,resultado_3))
    elif atitude == 4:
        resultado_4 = numero_calculavel * numero_calculavel_2
        print('A multiplicação entre {} e {}, resulta em {:.2f}'.format(numero_calculavel, numero_calculavel_2, resultado_4))
    elif atitude == 5:
        print('''
        [ 1 ] Somar
        [ 2 ] Subtrair
        [ 3 ] Dividir
        [ 4 ] Multiplicar
        [ 5 ] Outro Cálculo
        ''')
        sleep(0.7)
        infu = int(input('Quantos numeros você quer calcular: '))
        sleep(0.7)
        atitude = int(input('O que você quer fazer: '))
        sleep(0.7)    
    else:
        print('Caracter invalido!, digite corretamente por favor.')
print('-FIM-')
