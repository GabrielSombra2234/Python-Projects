#Bibliotéca
from time import sleep

#Escopo variaveis
#avanco
#nota_1
#nota_2
#nota_3
#nota_4
#nota_5
#n1, n2, n3, n4, n5

#Prints
print('=' * 35)
sleep(0.7)
print('Gravador de notas!')
sleep(0.7)
print('5 Nótas Disponíveis!')
sleep(0.7)
print('=' * 35)
sleep(0.7)

#Condição: While e Ifs
while True:

    #Nota 1
    nota_1 = str(input('Digite a 1° nota: '))
    titulo_1 = str(input('Digite um título para essa nota salva: '))
    print('/' * 30)
    print('4 Nótas disponíveis!')
    print('/' * 30)
    avanco_1 = str(input('Quer salvar mais notas ? [S/N]: ')).upper()
    print('=-' * 25)
    if avanco_1 == 'N':
        n1 = str(input('Deseja visualizar essa nota salva ? [S/N]: ')).upper()
        print('=-' * 25)
        if n1 == 'S':
            print('-' * 35)
            print(nota_1)
            print('-' * 35)
        else:
            pass
    elif avanco_1 == 'S':
        n1 = str(input('Quer visualizar essa nota salva ? [S/N]: ')).upper()
        print('=-' * 25)
        if n1 == 'S':
            print('-' * 35)
            print(nota_1)
            print('-' * 35)
        else:
            pass
    else:
        print(f'Comando {avanco_1} não reconhecido!, tente novamente!')
        break

    #Nota 2
    nota_2 = str(input('Digite a 2° nota: '))
    titulo_2 = str(input('Digite um título para essa nota salva: '))
    print('/' * 30)
    print('3 Nótas disponíveis!')
    print('/' * 30)
    avanco_2 = str(input('Quer salvar mais notas ? [S/N]: ')).upper()
    print('=-' * 25)
    if avanco_2 == 'N':
        n2 = str(input('Quer visualizar essa nota salva ? [S/N]: ')).upper()
        print('=-' * 25)
        if n2 == 'S':
            print('-' * 35)
            print(nota_2)
            print('-' * 35)
        else:
            pass
    elif avanco_2 == 'S':
        n2 = str(input('Quer visualizar essa nota salva ? [S/N]: ')).upper()
        print('=-' * 25)
        if n2 == 'S':
            print('-' * 35)
            print(nota_2)
            print('-' * 35)
        else:
            pass
    else:
        print(f'Comando {avanco_2} não reconhecido!, tente novamente!')
        break

    #Nota 3
    nota_3 = str(input('Digite a 3° nota: '))
    titulo_3 = str(input('Digite um título para essa nota salva: '))
    print('/' * 30)
    print('2 Notas disponíveis!')
    print('/' * 30)
    avanco_3 = str(input('Quer salvar mais notas ? [S/N]: ')).upper()
    print('=-' * 25)
    if avanco_3 == 'N':
        n3 = str(input('Deseja visualizar essa nota salva ? [S/N]: ')).upper()
        print('=-' * 25)
        if n3 == 'S':
            print('-' * 35)
            print(nota_3)
            print('-' * 35)
        else:
            pass
    elif avanco_3 == 'S':
        n3 = str(input('Deseja visualizar essa nota salva ? [S/N]: ')).upper()
        print('=-' * 25)
        if n3 == 'S':
            print('-' * 35)
            print(nota_3)
            print('-' * 35)
        else:
            pass
    else:
        print(f'Comando {avanco_3} não reconhecido!, tente novamente!')
        break
    
    #Nota_4
    nota_4 = str(input('Digite a 4° nota: '))
    titulo_4 = str(input('Digite um título para essa nota salva: '))
    print('/' * 30)
    print('1 Nota disponíveis!')
    print('/' * 30)
    avanco_4 = str(input('Quer salvar mais notas ? [S/N]: ')).upper()
    print('=-' * 25)
    if avanco_4 == 'N':
        n4 = str(input('Deseja visualizar essa nota salva ? [S/N]: ')).upper()
        print('=-' * 25)
        if n4 == 'S':
            print('-' * 35)
            print(nota_4)
            print('-' * 35)
        else:
            pass
    elif avanco_4 == 'S':
        n4 = str(input('Deseja visualizar essa nota salva ? [S/N]: ')).upper()
        print('=-' * 25)
        if n4 == 'S':
            print('-' * 35)
            print(nota_4)
            print('-' * 35)
        else:
            pass
    else:
        print(f'Comando {avanco_4} não reconhecido!, tente novamente!')
        break
    
    #Nota_5
    nota_5 = str(input('Digite a 5° nota: '))
    titulo_5 = str(input('Digite um título para essa nota salva: '))
    print('/' * 30)
    print('0 Notas disponíveis!')
    print('/' * 30)
    n5 = str(input('Deseja visualizar essa nota salva ? [S/N]: ')).upper()
    print('=-' * 25)
    if n5 == 'S':
        print('-' * 35)
        print(nota_5)
        print('-' * 35)
    elif n5 == 'N':
        pass
    else:
        print(f'Comando {n5} não reconhecido!, tente novamente!')
    break

#Lista de Notas
lista = str(input('Deseja ver a suas notas salvas ? [S/N]: ')).upper()
if lista == 'S':
    print('=-' * 30)
    print(f'''
    [ 1 ]: {titulo_1}
    [ 2 ]: {titulo_2}
    [ 3 ]: {titulo_3}
    [ 4 ]: {titulo_4}
    [ 5 ]: {titulo_5}
    ''')
    print('=-' * 30)
    print('Digite 6, para mostrar a lista novamente!')
    escolha = int(input('Digite a nota que deseja ver: '))

while True:

    #Exibição: Nota 1
    if escolha == 1:
        print('-' * 30)
        print(f'''
        {titulo_1}:
        {nota_1}
        ''')
        print('-' * 30)

    #Exibição: Nota 2
    elif escolha == 2:
        print('-' * 30)
        print(f'''
        {titulo_2}:
        {nota_2}
        ''')
        print('-' * 30)

    #Exibição: Nota 3
    elif escolha == 3:
        print('-' * 30)
        print(f'''
        {titulo_3}:
        {nota_3}
        ''')
        print('-' * 30)

    #Exibição: Nota 4
    elif escolha == 4:
        print('-' * 30)
        print(f'''
        {titulo_4}:
        {nota_4}
        ''')
        print('-' * 30)

    #Exibição: Nota 5
    elif escolha == 5:
        print('-' * 30)
        print(f'''
        {titulo_5}:
        {nota_5}
        ''')
        print('-' * 30)

    #Exibição: Lista
    elif escolha == 6:
        print('=-' * 30)
        print(f'''
        [ 1 ]: {titulo_1}
        [ 2 ]: {titulo_2}
        [ 3 ]: {titulo_3}
        [ 4 ]: {titulo_4}
        [ 5 ]: {titulo_5}
        ''')
        print('=-' * 30)
        print('Digite 6, para mostrar a lista novamente!')
        escolha = int(input('Digite a nota que deseja ver: '))

    #Sair
    else:
        print('=-' * 30)
        sleep(1)
        print('saindo...')
        sleep(1)
        print('=-' * 30)
        sleep(1)
else:
    print('=-' * 30)
    sleep(1)
    print('saindo...')
    sleep(1)
    print('=-' * 30)
    sleep(1)
print('-FIM-')
