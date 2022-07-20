# Bibliotécas
from time import sleep

# Apresentação
print('=-' * 20)
sleep(0.7)
print('Ordem de Precedência')
sleep(0.7)
print('=-' * 20)
sleep(0.7)

# If e While
validacao = str(input('Você sabe qual a Ordem certa? [S/N]: ')).upper()
sleep(0.7)

while True:
    if validacao == 'N':
        print('=-' * 20)
        sleep(0.7)
        print('Então irei te mostra a Ordem certa!!')
        sleep(0.7)
        print('=-' * 20)
        sleep(0.7)

        # Texto
        print('A Ordem começa assim:')
        sleep(0.5)
        print('-' * 20)
        sleep(0.5)
        print('1° Será tudo que está dentro das parenteses! ()')
        sleep(0.5)
        print('2° Em seguida serão todos os espoentes! **')
        sleep(0.5)
        print('3° Se em um programa tiver todos, resouva o que vier primeiro! *,/,//,%')
        sleep(0.5)
        print('4° Esses são binários! +,-')
        sleep(0.5)
        print('-' * 20)
        sleep(0.5)
        validacao2 = str(input('Compreendeu? [S/N]: ')).upper()
        if validacao2 == 'S':
            print('Assim que se faz!!')
            break
        else:
            print('Irei te mostar novamente!')
            pass
    else:
        break
print('-Fim-')
